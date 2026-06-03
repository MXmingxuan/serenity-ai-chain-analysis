# Memory Taxonomy

This project treats memory as structured research infrastructure. Memory must not become a bucket of model guesses.

## Memory Layers

| layer | purpose | examples | write rule |
|---|---|---|---|
| project rules | durable operating constraints |重点市场不等于唯一市场; Markdown is source, HTML is display | human-approved or framework-level only |
| run state | current research object state | current step, open questions, market scope | update during the run |
| entity memory | canonical facts about companies/products/nodes | company tickers, chain roles, product exposure | source-backed; overwrite when facts change |
| evidence memory | source-backed claims | evidence ledger rows, source index entries | must include source and confidence |
| execution memory | what the agent tried | failed search, missing data, validation warnings | append-only trace |
| preference memory | user style and output preferences | reusable Markdown assets, preserve negative evidence | user-confirmed or repeated pattern |

## Write Rules

- Facts require sources.
- Inferences must be labeled as inferences.
- Narratives must not be promoted to facts.
- If evidence changes, overwrite the canonical entity fact and preserve the old evidence in the ledger.
- Do not store secrets, tokens, private credentials, or raw sensitive prompts.
- Memory writes that will affect future runs should be visible in `research_state.yaml`, `run_trace.jsonl`, or a framework document.

## Retrieval Rules

- Load project rules at the start of a run.
- Load run state every step.
- Load entity memory only for related companies or chain nodes.
- Load evidence memory when auditing or citing.
- Load execution memory when debugging, resuming, or comparing agent behavior.
