# Quality creator submission packet

Status: prepared, not submitted. The existing shared creator account and first supplier template remain the first queue item. The owner previously described it as in review; the paired chat's current read-only portal inspection reports creator **Pending** and literal **Finalize submission** for that template. Acceptance/eligibility is not verified. Do not submit overlapping quality templates until the shared queue permits it.

Current primary guidance: [n8n creator help](https://support.n8n.io/article/becoming-an-n8n-template-creator-and-getting-help). Eligibility and review state can change; recheck the signed-in connected Opera portal before submission.

## First quality template

Title: **Check an entire lead CSV before CRM writes with Data Quality Gate**

Audience: automation agencies and agent builders with recurring file imports.

Asset: `lead-preflight.n8n.json` (inactive). Later queue: `baseline-preflight.n8n.json`, then `correction-replay.n8n.json`.

Description for review:

> Upload the original lead CSV/JSONL and evaluate its complete bounded file against a contract you explicitly reviewed and approved. The workflow proceeds only on continue, downloads the exact checked original, verifies SHA256 against its receipt and sends those bytes to your configured destination. Warnings, blocks, errors and timeouts stop for review. It does not repair or remap data.
>
> Verify an organization email and create an API key. Configure Header Auth, approved contract ID, actual source file, stable retry key and separate destination credentials. Five trials once per verified organization. The offer is $20 plus applicable tax prepaid for 100 completed checks; a completed block or warning uses one credit. Unsupported inputs/platform failures release the reserved credit. No subscription or automatic replenishment.
>
> Input limits: flat UTF-8 CSV/JSONL, 10 MiB, 50,000 records, 100 fields. Original files last 24 hours; reports seven days; operational receipts 30 days. Configure n8n's built-in crypto permission for SHA256 verification. Use the original quote/key on retries; corrected data requires a new upload/quote/key.

External accounts: verified quality organization, n8n instance, CRM/database destination credentials. No SMTP/reviewer credential is required for the stopping review node. Replace the synthetic Config file with your actual source.

## Submission gates

- Record intended source fingerprint, actual pinned n8n runtime, local Compose run and deployed HTTPS runs. Test all default stopping paths and exact destination bytes; include timeout/unexpected-state/download fault injection explicitly.
- Review exact new product claims and template text. Confirm deployed feature/offer state and live billing status accurately.
- Verify creator eligibility and sequential shared queue state. Preserve the supplier template's existing submission identity.
- Submit through the connected signed-in Opera session only when these gates pass. Record submission ID/time/review outcome; no acceptance/adoption claims from a form completion alone.

## Campaign attribution and contact

Use the existing verified ContentSweep creator account and its @contentsweep.ai address/alias. Recheck its current eligibility and the single-template review queue before submitting; do not create a duplicate account.

Trial link: https://mcp.contentsweep.ai/account/sign-in?product=data-quality-gate&source=n8n&channel=template-library&asset=lead-preflight&campaign=quality-lead-preflight-60d

Supporting integration: https://mcp.contentsweep.ai/quality/integrate?source=n8n&channel=template-library&asset=lead-preflight&campaign=quality-lead-preflight-60d
