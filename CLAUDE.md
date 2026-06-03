# Claude Code Entry Instructions

This project is a research agent harness for the `000.md` to `009.md` prompt chain. Before starting any research run, read `AGENTS.md` first, then follow the protocol documents listed there.

## Required Startup Sequence

1. Read `AGENTS.md`.
2. Read the protocol files referenced by `AGENTS.md`, especially:
   - `AGENT_CAPABILITY_MATRIX.md`
   - `SEARCH_PROTOCOL.md`
   - `CONTEXT_PACK_PROTOCOL.md`
   - `RUN_TRACE_SCHEMA.md`
   - `MEMORY_TAXONOMY.md`
   - `COMPONENT_DECOMPOSITION_PROTOCOL.md`
   - `templates/run_checklist.md`
3. Run or manually fill capability preflight before executing the prompt chain:

```powershell
python scripts\capability_preflight.py --run-dir "research_runs\YYYY-MM-DD-研究对象" --agent-name "Claude Code" --web-search yes --browser yes
```

If web search is unavailable, set `--web-search no` and do not independently execute `002` through `005` unless the user has provided a source pack.

## Research Discipline

- Markdown reports are the source of truth; HTML is a presentation layer.
- Every search-heavy step must update `sources/search_packet.md`.
- Important sources must be recorded in `sources/source_index.md` or `state/evidence_ledger.csv`.
- Equipment, system, machinery, material, and manufacturing-process themes must create `reports/003_component_decomposition.md`.
- "Focus on Chinese listed companies" never means "ignore overseas competitors, customers, or valuation anchors."
- A-shares use Tushare when available; overseas stocks use `uv run --script tools/yf ...` or an explicitly recorded fallback.
- Never write Tushare tokens, API keys, passwords, bearer tokens, or local secrets into repository files.

## Completion Gate

Before saying a run is complete:

```powershell
python scripts\validate_run.py "research_runs\YYYY-MM-DD-研究对象"
```

Also scan staged changes for secrets if committing:

```powershell
git diff --cached | rg -n "ts\.set_token\(|Bearer |api_key|apikey|password|passwd"
```

The expected output for a healthy run is `PASSED: 0 error(s), 0 warning(s)`, or explicit warnings documented in the run trace and final handoff.
