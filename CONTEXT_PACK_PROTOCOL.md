# Context Pack Protocol

The prompt chain should use just-in-time context. Load the minimum useful context for the current step, then retrieve more only when needed.

## Context Layers

| layer | examples | load policy |
|---|---|---|
| project rules | `AGENTS.md`, framework addenda, templates | load at run start |
| current state | `state/research_state.yaml`, `state/evidence_ledger.csv` | load every step |
| previous report | immediately previous report | load every step |
| source index | `sources/source_index.md` | load when citing or auditing |
| market data | `market_data/*.csv` | load before and during `006` |
| full historical reports | all prior reports | load only for `008`/`009` or if needed |
| external sources | webpages, PDFs, filings | load only as needed and summarize into evidence |

## Step Context Map

| step | required context | avoid |
|---|---|---|
| `000` | project rules, user object | old run details unless reused intentionally |
| `001` | `000_scope.md`, current state | market data |
| `002` | `001_value_chain.md`, demand search packet | full candidate tables |
| `003` | `002_demand.md`, supply sources | all market pricing files |
| `003_component_decomposition` | `003_supply.md`, source index, component search packet | market pricing files unless mapping listed suppliers |
| `004` | `003_supply.md`, cross-market rules | running `006` data before candidates are stable |
| `005` | reports `000-004`, evidence ledger, source index | introducing unsupported new thesis |
| `006` | `004_targets.md`, symbol universe, market data | inferring missing prices or valuations |
| `007` | reports `000-006`, evidence gaps | removing negative evidence |
| `008` | reports `000-007`, source index, state | large new research unless fixing a gap |
| `009` | final report | overlong evidence dumps |

## Compression Rules

- Keep full source text out of working context once summarized into evidence.
- Keep source URLs, filing names, dates, and evidence grade.
- If a report is long, load headings and tables first, then full sections only as needed.
- Do not carry stale assumptions forward without checking `open_questions` and `disconfirmation`.
- For equipment-heavy themes, carry `reports/003_component_decomposition.md` into `004_targets.md`, `005_evidence_audit.md`, and `008_final_report.md`.
