# Catch a duplicate at row 12,002 before a CRM write

Check original lead files against reviewed rules. Compare continue, block and warning outcomes; only continue produces a local destination preview.

Owned synthetic example. Recorded results are clearly separated from live execution. Installing a skill does not install its runtime or authorize spending or uploads.

## Inspect the evidence

Read `manifest.json`, `expected.json`, and the fixtures before running. The walkthrough covers continue, block, warning. Results come from actual product MCP calls, not simulated responses. The free public page and downloads require no sign-in.

## Reproduce with your agent

Read the existing `quality-preflight` skill and its companion setup/tool references. Then follow `AGENT_PROMPT.md`. Create a dedicated Python 3.12+ environment and install `mcp>=2.3,<3`. Configure CONTENTSWEEP_QUALITY_API_KEY privately in your environment; never paste its value into prompts, command arguments, URLs or source control.

These commands are qualified on macOS and Linux. Follow [client setup](https://github.com/founder-sweep/data-quality-gate-examples/blob/main/CLIENTS.md) for runtime installation. Use that environment’s Python to run the demo.

For deterministic verification from this repository root:

```sh
python demo/run.py --mode hosted --max-units 3 --output demo-results
```

The hosted allowance explicitly authorizes at most 3 evaluations of these named synthetic cases. Review the supplied field decisions before approving them. It grants no permission for customer files, purchases, destination writes, source edits or cloud actions. Hosted keys are your own; local analysis needs no hosted key.

Reuse the same output directory and allowance after an uncertain response. `resume.private.json` preserves quote/key/job identities before dispatch. Keep it private. Never start a new run merely because polling timed out. Changed customer data needs its own review and authorization. A completed rejection, block or warning can be billable as documented for this product.

## Interpret the result

Inspect `result.json` for assertions, complete reports and actual tool discovery. Expected stop cases are part of a passing demo. A deterministic runner is not a native agent completion. Machine-generated IDs, timestamps and local paths may differ; business values, coverage and accounting must agree.

Original flat CSV/JSONL, approved rules, 10 MiB, 50,000 records, 100 fields. No mapping or repair; preserve original bytes.

## Price and next step

Five trials per verified organization; $20 plus applicable tax/100 checks, with no subscription.

[Read the full walkthrough and setup](https://mcp.contentsweep.ai/quality/demos/crm-preflight) · [Product and current terms](https://mcp.contentsweep.ai/quality)

Keep local/free options separate from optional hosted purchases. This example performs no purchase. Reports are bounded evidence, not runtime certification or proof of customer outcomes.

## Preserve original bytes in a native agent session

Some clients reconstruct file contents or rewrite object keys. Use this reviewed helper through the agent’s native shell tool to upload the exact checksum-bound fixtures, then continue with the product’s native MCP review, approval, quote, evaluation, report and retry tools:

```sh
python demo/transfer.py --confirm-upload --output demo-uploads/uploads.private.json
```

It uploads only the bundled synthetic files and prints owned upload IDs. It performs no approval, evaluation, purchase or destination write. Keep its identity file private and reuse it after an interruption. This mixed file-transfer/MCP workflow is disclosed in the native evidence.

<!-- demo-specific-walkthrough -->
## Destination boundary

Only `continue` creates the [local destination preview](https://mcp.contentsweep.ai/quality/demos/crm-preflight/destination-preview.json); no CRM write occurs. `block` identifies the duplicate at record 12,002 and `continue_with_warnings` also stops this demonstration before a destination. The [checked original CSV](https://mcp.contentsweep.ai/quality/demos/crm-preflight/continue-original.csv) is the actual original input, downloaded and byte-compared. Each completed outcome consumes one check; retrying the original quote/key consumes no additional check.
