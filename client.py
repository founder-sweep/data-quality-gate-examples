#!/usr/bin/env python3
"""Standalone full-file HTTP client; only continue returns checked original data."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import time
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url', default='https://mcp.contentsweep.ai')
    parser.add_argument('--file', type=Path, default=Path(__file__).with_name('leads.csv'))
    parser.add_argument('--contract', type=Path, default=Path(__file__).with_name('leads.contract.json'))
    parser.add_argument('--contract-id')
    parser.add_argument('--baseline-id')
    parser.add_argument('--approve-contract', action='store_true')
    parser.add_argument('--authorize-check', action='store_true')
    parser.add_argument('--retry-state', type=Path, default=Path('.quality-retry.json'))
    parser.add_argument('--resume', action='store_true')
    parser.add_argument('--out', type=Path, default=Path('checked-original.csv'))
    args = parser.parse_args()
    base = args.base_url.rstrip('/')
    parsed = urlparse(base)
    if parsed.scheme != 'https' and not (parsed.scheme == 'http' and parsed.hostname in {'localhost', '127.0.0.1'}):
        raise ValueError('HTTPS required except local qualification')
    key = os.environ.get('QUALITY_API_KEY')
    if not key:
        raise ValueError('Set QUALITY_API_KEY from your verified account; never store it in examples')

    def request(path, method='GET', value=None, raw=False):
        headers = {'X-API-Key': key}
        data = value if raw else json.dumps(value).encode() if value is not None else None
        if data is not None:
            headers['Content-Type'] = 'application/octet-stream' if raw else 'application/json'
        try:
            with urlopen(Request(base + path, method=method, data=data, headers=headers), timeout=30) as response:
                body = response.read(11 * 1024 * 1024)
                return body if raw and method == 'GET' else json.loads(body)
        except HTTPError as exc:
            raise RuntimeError('Quality request failed with HTTP ' + str(exc.code)) from None

    raw = args.file.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if args.resume:
        state = json.loads(args.retry_state.read_text())
        if state['input_fingerprint'] != sha or state['base_url'] != base:
            raise ValueError('Retry state belongs to different input or service')
    else:
        upload = request('/v1/quality/uploads?format=' + ('jsonl' if args.file.suffix == '.jsonl' else 'csv'), 'POST', raw, raw=True)
        if upload['sha256'] != sha:
            raise ValueError('Uploaded fingerprint differs')
        contract_id = args.contract_id
        if not contract_id:
            decision = request('/v1/quality/contracts', 'POST', {'upload_id': upload['id'], 'contract': json.loads(args.contract.read_text())})
            print(json.dumps({'draft': decision, 'next': 'Review exact decisions before --approve-contract'}))
            if not args.approve_contract:
                return 0
            request('/v1/quality/contracts/' + decision['id'] + '/approve', 'POST', {'approve': True, 'expected_hash': decision['hash']})
            contract_id = decision['id']
        quote = request('/v1/quality/quotes', 'POST', {'upload_id': upload['id'], 'contract_id': contract_id, 'baseline_id': args.baseline_id})
        print(json.dumps({'quote': quote}))
        if quote['status'] != 'quoted' or not args.authorize_check:
            return 2
        state = {'base_url': base, 'input_fingerprint': sha, 'quote_id': quote['id'], 'idempotency_key': secrets.token_urlsafe(24)}
        args.retry_state.write_text(json.dumps(state))
        args.retry_state.chmod(0o600)
    if not args.authorize_check:
        raise ValueError('Execution requires explicit --authorize-check; completed blocks/warnings use one quality credit')
    job = request('/v1/quality/jobs', 'POST', {'quote_id': state['quote_id'], 'idempotency_key': state['idempotency_key']})
    for _ in range(60):
        if job['status'] in {'completed', 'failed'}:
            break
        if job['status'] not in {'queued', 'running'}:
            raise RuntimeError('Unexpected job state; stop downstream writes')
        time.sleep(2)
        job = request('/v1/quality/jobs/' + job['id'])
    if job['status'] != 'completed':
        print(json.dumps({'job': job, 'downstream': 'review_required'}))
        return 5
    report = request('/v1/quality/jobs/' + job['id'] + '/report')
    print(json.dumps({'report': report, 'receipt': job['receipt']}))
    if report['verdict'] != 'continue' or report['full_file_validation'] is not True or report['input_fingerprint'] != sha:
        return 2
    original = request('/v1/quality/jobs/' + job['id'] + '/original', raw=True)
    if hashlib.sha256(original).hexdigest() != sha or job['receipt']['input_fingerprint'] != sha:
        raise ValueError('Original data fingerprint mismatch; stop downstream writes')
    args.out.write_bytes(original)
    args.out.chmod(0o600)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
