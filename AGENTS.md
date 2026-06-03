# Serenity 分析项目 Agent 指南

在本项目执行 000-009 prompt chain 时，必须先读取：

1. `AGENT_FRAMEWORK.md`
2. `FRAMEWORK_ADDENDUM_CROSS_MARKET.md`
3. `AGENT_CAPABILITY_MATRIX.md`
4. `SEARCH_PROTOCOL.md`
5. `CONTEXT_PACK_PROTOCOL.md`
6. `RUN_TRACE_SCHEMA.md`
7. `MEMORY_TAXONOMY.md`
8. `COMPONENT_DECOMPOSITION_PROTOCOL.md`
9. `templates/run_checklist.md`

## 跨 Agent 入口

- Codex、Claude Code、OpenClaw 或其他 agent 都应以本文件作为项目入口。
- Claude Code 会优先读取项目根目录的 `CLAUDE.md`；该文件只做轻量入口适配，真实规则仍以本文件和协议文档为准。
- 如果某个 agent 有自己的记忆文件、skill、MCP 或浏览器工具，不得覆盖本项目协议；只能作为能力实现方式写入 `state/capability_report.json` 和 `state/run_trace.jsonl`。
- 搜索工具、浏览器工具和行情数据源在不同 agent 中会有差异，因此最终报告必须以 source index、evidence ledger、market data notes 和 run trace 为可复盘依据，而不是以“模型记得/模型判断”为依据。

## 强制规则

- “以中国上市公司为重点”不等于“只研究中国上市公司”。
- 004 的候选公司清单必须覆盖美股、港股、A 股和其他相关市场，或写明某市场缺失原因。
- 003 中出现的海外龙头、区域供应商、下游需求方，必须传递到 004 的竞争/对标宇宙。
- 006 前必须根据 `market_data/symbol_universe.csv` 拉取结构化行情和估值；A 股用 Tushare，海外市场优先用 `uv run --script tools/yf ...`。
- 所有 `coverage_required=yes` 的标的，如果没有行情数据，必须在 `market_data/market_data_notes.md` 记录缺口。
- 008 最终报告如果重点讨论 A 股，必须有“全球竞争与对标约束”段落。
- 008 Markdown 报告仍是源文件；如需要更好展示效果，应在 `html/008_final_report.html` 额外输出静态 HTML 页面。
- HTML 页面必须链接回 Markdown 报告和 source index，并保留证据边界、数据日期和“不构成投资建议”提示。
- 启动前必须运行或手工填写 capability preflight；没有 web search 且没有用户提供 source pack 时，不得独立执行 `002` 到 `005`。
- 搜索密集步骤必须创建或更新 search packet，重要来源必须进入 source index 或 evidence ledger。
- 设备、主机、系统、材料、制造工艺类主题必须执行 component decomposition；不得只停留在龙头、主机厂或系统集成商层面。
- component decomposition 应输出 `reports/003_component_decomposition.md`，并把二级/三级零部件、关键材料、工艺设备、后市场和认证壁垒传递到 `004_targets.md`。
- 每个 run 应维护 `state/run_trace.jsonl`，记录搜索、数据拉取、报告生成、校验和 HTML 输出等事件。
- 每次运行结束前执行：

```powershell
python scripts/validate_run.py research_runs/YYYY-MM-DD-研究对象
```

## 输出边界

- 本项目产物是研究雷达和证据资产，不是自动交易系统。
- 不得把主题相关性写成利润受益。
- 不得把重点研究优先级写成买入建议。
- 不得把 Tushare token 或其他密钥写入 Markdown、CSV、YAML 或脚本。
