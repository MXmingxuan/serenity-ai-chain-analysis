# Agent Capability Matrix

This project can be run by Codex, Claude Code, OpenClaw, or another coding/research agent, but only if the agent's capabilities are made explicit before the run starts.

## Capability Levels

| level | meaning | handling |
|---|---|---|
| `required` | The capability is necessary for the step. | Do not run the step independently if missing. |
| `optional` | Improves quality but is not required. | Record absence in `capability_report.json`. |
| `missing-with-fallback` | Missing, but the run can continue with reduced scope. | Record the fallback and downgrade confidence where relevant. |

## Required Capabilities By Step

| step | required capabilities | fallback if missing |
|---|---|---|
| `000` | file read/write, Markdown output | none |
| `001` | file read/write, basic search optional | use prior reports only |
| `002` | web search or user-provided source pack | do not independently validate demand; mark as source-limited |
| `003` | web search, source reading, evidence ledger updates | do not independently validate supply constraints |
| `004` | web search, company filing access, cross-market ticker resolution | candidate list must be labeled incomplete |
| `005` | evidence ledger, source index, file read/write | none |
| `006` | Tushare for A-shares, Yahoo CLI for overseas stocks, market data files | write explicit market-data gap; do not infer missing valuation |
| `007` | prior reports and evidence ledger | none |
| `008` | prior reports, evidence ledger, source index | do not introduce large new research |
| `009` | final report | none |
| HTML output | static HTML write capability | keep Markdown only |

## Tool Expectations

| capability | preferred implementation | notes |
|---|---|---|
| web search | agent-native web search or configured MCP search | Required for current industry/company facts. |
| browser/source reading | browser tool, web reader, or MCP browser | Needed to verify pages and PDFs. |
| Python | local Python 3.11+ | Needed for validators and data scripts. |
| Tushare | `tushare` package + `TUSHARE_TOKEN` env var | Never write token values to files. |
| Yahoo CLI | `uv run --script tools/yf ...` | Used for US/HK/overseas market data. |
| git | local git CLI | Needed for clean handoff and sync. |
| HTML validation | static checks; browser screenshot optional | Browser rendering differs by agent environment. |

## Hard Gate

If `web_search` is not available and the user has not supplied a source pack, the agent may not independently execute `002` through `005`. It may only:

- organize existing reports;
- convert Markdown to HTML;
- run validation;
- analyze user-provided sources;
- prepare search packets for a better-equipped agent.
