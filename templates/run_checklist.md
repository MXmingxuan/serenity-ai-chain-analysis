# Prompt Chain Run Checklist

研究对象：
运行目录：

## 启动前

- [ ] 已确认研究对象。
- [ ] 已读取 `AGENT_FRAMEWORK.md` 和 `FRAMEWORK_ADDENDUM_CROSS_MARKET.md`。
- [ ] 已区分 `primary_focus` 和 `required_comparison_markets`。
- [ ] 如果用户说“以某市场为重点”，已确认这不是“只研究该市场”。
- [ ] 已创建 `research_runs/YYYY-MM-DD-研究对象/`。
- [ ] 已复制或创建 `state/research_state.yaml`。
- [ ] 已复制或创建 `state/evidence_ledger.csv`。
- [ ] 已确认本轮是否需要联网搜索。

## 逐轮执行

- [ ] `000.md`：对象定义、初始假设、研究路线。
- [ ] `001.md`：产业链位置、N 阶传导、利润分配初判。
- [ ] `002.md`：需求源头、需求加速证据、需求持续性。
- [ ] `003.md`：供给弹性、瓶颈评分、利润转化。
- [ ] `004.md`：标的映射、A/B/C 分类、利润兑现路径。
- [ ] 第 004 步质量门槛：候选清单已覆盖美股、港股、A 股和其他相关市场，或明确写出某市场无直接标的/数据不可得的原因。
- [ ] 第 004 步质量门槛：海外龙头、区域供应商、下游需求方已作为竞争/对标宇宙记录。
- [ ] `005.md`：证据分级、事实/推理/叙事拆分。
- [ ] 第 006 步前：更新 `market_data/symbol_universe.csv`，且覆盖 004 的 A/B 候选和关键海外对标。
- [ ] 第 006 步前：拉取或生成 `market_data/price_snapshot.csv`。
- [ ] 第 006 步前：拉取或生成 `market_data/valuation_snapshot.csv`。
- [ ] 第 006 步前：拉取或生成 `market_data/liquidity_snapshot.csv`。
- [ ] 第 006 步前：记录 `market_data/market_data_notes.md`。
- [ ] 第 006 步质量门槛：所有 `coverage_required=yes` 的标的都有数据，或在缺口表中说明原因。
- [ ] `006.md`：市场定价、估值、拥挤度、交易风险。
- [ ] `007.md`：风险、反证条件、退出信号。
- [ ] `008.md`：综合研究报告。
- [ ] `009.md`：个人投资研究卡片。

## 每轮质量门槛

- [ ] 报告包含本轮任务边界。
- [ ] 报告说明使用了哪些上一轮上下文。
- [ ] 搜索证据已进入 `evidence_ledger.csv`。
- [ ] 关键结论有证据等级。
- [ ] 明确区分事实、推理、叙事和假设。
- [ ] 保留负面证据和反证。
- [ ] 输出“本轮结论”。
- [ ] 输出“下一步需要继续验证的问题”。

## 收尾

- [ ] `008_final_report.md` 不引入大量新信息，只整合前序报告。
- [ ] `009_research_card.md` 足够短，适合进入 Obsidian / Logseq / Notion。
- [ ] `source_index.md` 能追溯主要来源。
- [ ] 已运行 `python scripts/validate_run.py research_runs/YYYY-MM-DD-研究对象`。
- [ ] 最终动作只从框架允许的动作中选择。
