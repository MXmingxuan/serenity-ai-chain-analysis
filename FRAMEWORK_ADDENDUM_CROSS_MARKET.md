# Framework Addendum: Cross-Market Control Layer

本文件是 `AGENT_FRAMEWORK.md` 的补充控制层。后续运行 000-009 prompt chain 时，必须同时读取本文件。

## 1. 重点市场不等于唯一市场

如果用户说“以中国上市公司为重点”或“重点看 A 股”，主控 agent 必须解释为：

- 结论和深挖对象以中国上市公司为重点；
- 需求源头、竞争格局、全球龙头、海外可投资对标仍然必须覆盖；
- 004 候选公司清单和 006 市场定价必须尽量覆盖美股、港股、A 股和其他相关市场。

不得把“重点研究中国上市公司”执行成“只研究中国上市公司”。

## 2. 000 阶段必须写市场范围

`state/research_state.yaml` 必须维护：

- `market_scope.primary_focus`
- `market_scope.required_comparison_markets`
- `market_scope.optional_markets`
- `competitive_universe`
- `market_data_coverage`

示例：

```yaml
market_scope:
  primary_focus: ["CN_A"]
  required_comparison_markets: ["US", "HK", "TW", "EU", "JP"]
  optional_markets: []
```

## 3. 004 阶段候选宇宙要求

`004_targets.md` 必须同时包含：

- 中国重点标的；
- 美国/欧洲/日本/台湾等海外龙头或竞争对标；
- 港股和其他市场的可投资映射；
- 下游需求方或系统集成商，用于验证谁真正掌握订单和议价权。

如果某市场没有直接标的，必须显式写入“无直接标的/暂未发现/数据不可得/与本瓶颈关系弱”的原因。空表不合格。

## 4. 006 阶段市场数据要求

运行 `006.md` 前必须读取 `market_data/symbol_universe.csv`。该表字段为：

```csv
symbol,market,name,currency,source_step,priority,market_role,coverage_required,data_provider,coverage_status,gap_reason,notes
```

规则：

- `coverage_required=yes` 的标的必须尝试拉取结构化行情和估值。
- A 股使用 Tushare。
- 美股、港股、ETF、台股和部分其他市场优先使用 Yahoo Finance CLI：`uv run --script tools/yf ...`。
- 如果数据缺失，必须写入 `market_data/market_data_notes.md` 的缺失数据表。
- 不得把“没有拉数据”解释成“该市场不重要”。

## 5. 最终报告必须有全球对标约束

当最终报告重点讨论 A 股时，`008_final_report.md` 必须包含一段“全球竞争与对标约束”，至少回答：

- 海外龙头是否更直接受益？
- 中国公司相对海外公司是成本优势、产能优势、认证优势，还是仅主题映射？
- 海外标的涨幅和估值是否已经给出了全球定价锚？
- 如果海外供应商拿走主要份额，中国标的结论是否需要降级？

## 6. 新增校验

每次运行结束前执行：

```powershell
python scripts/validate_run.py research_runs/YYYY-MM-DD-研究对象
```

校验不替代研究判断，但用于发现以下机械问题：

- 000-009 报告缺失；
- evidence ledger 或 market data CSV 无法解析；
- 004 未覆盖跨市场候选；
- `symbol_universe.csv` 只有单一市场且没有缺口说明；
- 研究目录里误写入 Tushare token。
