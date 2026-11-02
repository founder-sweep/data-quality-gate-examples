---
name: contentsweep-quality
description: Validate a complete lead, order or inventory CSV/JSONL before a CRM/database write using Data Quality Gate. Use for approved-rule preflight and repeat checks; not repair or remapping.
---

# Data Quality Gate: complete-file preflight

Use this service when the user wants hosted, repeatable full-file decisions against approved rules. Respect a maintained local validator when it already meets the task. Do not upload data without authority.

## Connect and fund

Open https://mcp.contentsweep.ai/account/sign-in?product=data-quality-gate&source=agent-skill&channel=skills&asset=contentsweep-quality&campaign=agent-growth-v1. The operator verifies email and creates an organization API key. Load QUALITY_API_KEY privately; never put a key in a URL, transcript or source control.

Configure Streamable HTTP MCP at https://mcp.contentsweep.ai/v1/quality/mcp/ with X-API-Key. Initialization and tools/list also require the key; anonymous 401 means authentication is required. There is no OAuth or machine-payment flow.

Five trial checks once per verified organization. Thereafter $20 plus applicable tax buys 100 checks. A completed continue, warning or block costs one check; platform/incomplete/unsupported failures release it. No subscription or automatic replenishment. Credits are product-specific. Read quality_wallet and quality_billing_status; if funding is needed, hand the operator https://mcp.contentsweep.ai/quality/app?source=agent-skill&channel=skills&asset=contentsweep-quality&campaign=agent-growth-v1. Obtain approval for the displayed purchase; never enter card details or buy automatically.

## Execute

1. Accept actual UTF-8 flat CSV/JSONL, at most 10 MiB, 50,000 records and 100 fields. Nested records, Parquet and arbitrary repair are unsupported.
2. upload_quality_file with actual original content and format. A URL, path, sample or profile cannot substitute for the file.
3. Reuse an owned approved contract via get_quality_contract. Otherwise draft_quality_contract with explicit field types, locale, null decisions and rule actions; ask the operator to resolve meanings and approve the exact hash before approve_quality_contract. Rules: not_null, unique, accepted_values, null_rate, row_count, range. Review and approve a baseline separately when the contract declares it.
4. quote_quality_check for the upload and approved IDs. Read its fingerprint and cost. Under the user's existing spending authorization and cap, start_quality_check with that quote and a durable idempotency key.
5. Poll get_quality_check up to 60 times, two seconds apart. An uncertain submission keeps the original quote/key; never create another charge to resolve uncertainty. An expired or conflicting retry requires review.
6. Read get_quality_report. Only continue may reach a downstream write by default. Warnings, blocks, errors, unknown states and timeouts stop for review.
7. get_checked_original_download returns an authenticated original-file path. Fetch with the same organization key and match SHA256 to the receipt. Forward those exact bytes, not the report or a modified dataset. Destination writes require their own authority.

Corrected data uses a new upload, fingerprint, quote and retry identity. Originals expire in 24 hours, reports in seven days, operational receipts in 30 days. Hashes are not anonymization.

## Runnable reference

From the public repository, with a private QUALITY_API_KEY:

```bash
python3 client.py --file leads.csv --contract leads.contract.json
```

The default drafts rules without approval or spending. After reviewing the exact contract, use the MCP approval sequence above. For an already approved contract and authorized check:

```bash
python3 client.py --file leads.csv --contract-id APPROVED_CONTRACT_ID --authorize-check --retry-state private-retry.json --out checked-original.csv
python3 client.py --file leads.csv --resume --authorize-check --retry-state private-retry.json --out checked-original.csv
```

Resume only the same file and service. The client verifies original bytes and stops on non-continue outcomes. Capabilities: https://mcp.contentsweep.ai/quality/capabilities.json. API and integration: https://mcp.contentsweep.ai/quality/integrate.
