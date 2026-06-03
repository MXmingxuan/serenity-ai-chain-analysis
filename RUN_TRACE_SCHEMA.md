# Run Trace Schema

Each research run may include an append-only execution log:

```text
state/run_trace.jsonl
```

Each line is one JSON object. Do not store secrets, full private prompts, full web pages, or raw API credentials.

## Required Fields

| field | type | description |
|---|---|---|
| `timestamp` | string | ISO-8601 timestamp. |
| `step` | string | Prompt-chain step such as `002_demand`, `006_pricing`, `html_output`. |
| `agent` | string | Agent/tool name, for example `Codex`. |
| `action_type` | string | `read`, `search`, `data_fetch`, `write_report`, `validate`, `html_output`, `handoff`, `error`. |
| `tool_or_source` | string | Tool, script, source, or file involved. |
| `input_summary` | string | Short non-sensitive summary of input. |
| `output_summary` | string | Short summary of result. |
| `status` | string | `success`, `warning`, `failed`, or `skipped`. |
| `error` | string | Error text or empty string. |
| `artifacts_changed` | array | Paths created or modified by this event. |

## Recommended Event Boundaries

- run setup;
- each search packet;
- each structured data pull;
- each report write;
- validation run;
- HTML output;
- GitHub sync or handoff.

## Example

```json
{"timestamp":"2026-06-03T20:00:00+08:00","step":"006_pricing","agent":"Codex","action_type":"data_fetch","tool_or_source":"Tushare pro.daily/pro.daily_basic","input_summary":"A-share liquid-cooling candidate universe","output_summary":"Generated price, valuation, and liquidity snapshots","status":"success","error":"","artifacts_changed":["market_data/price_snapshot.csv","market_data/valuation_snapshot.csv","market_data/liquidity_snapshot.csv"]}
```
