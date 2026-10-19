# Check lead CSV files before your agent writes to a CRM

**Data Quality Gate** checks every row of an original lead, order or inventory CSV/JSONL against explicit contracts you review and approve. The workflow proceeds only on `continue`, then downloads and verifies the exact checked original before a destination write.

[Try five checks free](https://mcp.contentsweep.ai/account/sign-in?product=data-quality-gate&source=github&channel=repository&asset=readme&campaign=quality-lead-preflight-60d) · [Integration guide](https://mcp.contentsweep.ai/quality/integrate?source=github&channel=repository&asset=readme&campaign=quality-lead-preflight-60d) · [Reproducible lead guides](https://mcp.contentsweep.ai/quality/guides?source=github&channel=repository&asset=readme&campaign=quality-lead-preflight-60d)

Five trial checks once per verified organization, then **100 prepaid checks for $20 plus applicable tax**. No quality subscription, automatic overages or replenishment. A supported completed block or warning uses one check. Unsupported or incomplete evaluations and platform failures do not; duplicate retries reuse the original job.

The fixtures here are synthetic, generated and checked by the maintained engine. No customer files, credentials or private execution logs belong in this repository. Internal qualification and synthetic examples do not establish independent customer adoption, customer ROI or comparative superiority. Qualification evidence is bound to the intended installed source before publication.

## Reference client

From this examples repository, use Python 3.12 or later and the standard-library client:

```bash
export QUALITY_API_KEY=... # from your verified account; keep it private
python client.py --file leads.csv
# Review the exact preset before approving and authorizing a check:
python client.py --approve-contract --authorize-check
# Resume the original quote/key after an uncertain response:
python client.py --resume --authorize-check
```

The retry file contains no API key but is private; keep it and customer outputs out of version control. `--contract-id` reuses an existing approved contract; `--baseline-id` supplies its reviewed reference. Exit 0 returns the exact checked original; exit 2 stops for constraint/quote review; exit 5 stops for failed/unfinished evaluation. A timeout never authorizes writing. Delete local customer outputs according to your policy.

## n8n setup

Import an inactive workflow, then:

1. Verify your organization and create a key. In HTTP Header Auth configure header `X-API-Key` with that key, named **Quality organization X-API-Key**. Select it on quality HTTP nodes.
2. In `/quality/app`, edit/save/review/approve a contract. Baseline recipe also needs an explicitly approved reference and threshold/action.
3. Set Config `baseUrl`, `contractId`, `baselineId` when needed, the **actual original** `fileContent`, its format and a fresh stable `idempotencyKey`. For a binary upstream file, supply its original UTF-8 bytes to Upload; do not substitute the parsed report. Configure the incoming trigger yourself for your account/service.
4. Review the workflow and set `operatorConfigured: true`. Configure a separate destination credential named **Your CRM/database destination** and an endpoint accepting the original CSV/JSONL. Set `destinationEnabled: true` only after destination review. A real CRM adapter may parse the checked file after fingerprint verification; preserve identifiers and decimal strings.
5. Enable n8n's built-in `crypto` module for the runner (`NODE_FUNCTION_ALLOW_BUILTIN=crypto`). The SHA256 verification node fails closed if it is unavailable. Never disable fingerprint verification to bypass this setup.

Recipes:

| File | Workflow |
| --- | --- |
| `lead-preflight.n8n.json` | Original lead file → approved contract → quoted check → `continue` → exact original download → SHA256 verification → destination |
| `baseline-preflight.n8n.json` | Order/inventory file → exact approved baseline → drift check → destination or review |
| `correction-replay.n8n.json` | Original rejected receipt → genuinely changed corrected file → new quote/key → check → destination or review |

Polling stops after 25 status reads. HTTP errors/timeouts, warnings, blocks, unknown states, incomplete reports and changed original downloads reach **Review required**. That node stops the execution; it does not send external notifications. Configure reviewer notification separately with your own account/authorization. Only `continue` reaches a destination automatically.

The destination receives downloaded original file bytes. Validation report JSON is never sent as the dataset. Source retention is 24 hours even though reports last seven days; obtain the original promptly. Keep the same quote/key on retries; new corrected bytes require a new key and quote.

## Discovery and publishing

`server.json` prepares `ai.contentsweep/data-quality-gate` at `/v1/quality/mcp/`, with a required secret organization key. `capabilities.json`, `llms.txt` and `ard.json` describe bounded implemented capabilities. Registry publication requires actual qualified HTTPS API/worker/MCP and n8n evidence matching the installed source fingerprint, exact descriptor review and owned DNS authentication. A prepared descriptor is not a registry listing.

Use [the creator submission packet](N8N_SUBMISSION.md) after shared creator eligibility and the existing first-template queue are verified. Do not overwrite supplier-feed examples or publish private prospect packets, customer files, API keys or raw n8n execution logs.

`scripts/publish-quality-examples.py` prepares a separate allowlisted payload for `founder-sweep/data-quality-gate-examples` without network mutation. `--publish` requires exact owner-reviewed repository/payload/source hashes and matching deployed HTTPS runtime proof; customer/private/unmanaged material is rejected. It checks remote HEAD even after an uncertain push. `scripts/publish-quality-registry.py` has a separate exact descriptor/namespace/HTTPS qualification gate. Neither publication was performed in local qualification.

## Tutorial series

Start with lead CSV preflight, a duplicate at record 12,002, and warning review. The owned website then covers missing identifiers, unexpected statuses, exact numeric ranges, approved row-count drift and correction replay. Each guide offers full synthetic inputs, explicit rules, observed output and local reproduction instructions. Publication follows a finite reviewed backlog; exhausted weeks maintain existing material.
