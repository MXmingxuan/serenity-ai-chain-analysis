# 两个案例后的问题清单与优化方向

本文档基于两次已完成的 prompt-chain 运行复盘：

- `research_runs/2026-06-03-数据中心电力设备中国上市公司`
- `research_runs/2026-06-03-液冷二级零部件`

目标不是评价单次报告写得是否完整，而是把执行过程中暴露出来的系统问题沉淀成后续 agent 必须遵守的控制规则。

## 1. 已遇到的问题清单

### P1. 研究对象被“重点市场”过度收窄

现象：用户说“以中国上市公司为重点”，执行时被理解成“只研究中国上市公司”。在数据中心电力设备案例中，004 的候选公司清单实际只覆盖 A 股，006 的行情估值数据也只覆盖 A 股。

源头：

- `000` 的对象定义没有把“重点研究市场”和“完整竞争宇宙”拆开。
- `004.md` 虽然要求按美股、港股、A 股、其他市场整理，但框架没有把它做成硬性质量门槛。
- 结构化数据层先接入了 Tushare，导致执行路径天然偏向 A 股。

优化方向：

- 在 `research_state.yaml` 中新增 `market_scope`：区分 `primary_focus`、`required_comparison_markets`、`market_data_coverage`。
- 004 前必须先做跨市场候选宇宙，不允许只有 A 股，除非写明“无直接标的/数据不可得/与主题无关”的证据理由。
- 006 前必须为美股、港股、A 股分别说明行情数据是否覆盖；不能覆盖时要进入缺口表。

### P2. 竞争格局和可投资标的混在一起

现象：报告会提到海外龙头、台湾供应链或系统集成商，但候选股票和行情数据没有同步纳入。结果容易变成“中国公司内部横向比较”，缺少全球竞争坐标。

源头：

- 003 的供给格局写了海外公司，但没有把它传递给 004 的候选公司清单。
- 004 的“标的映射”被理解成“只找用户最关心的市场”，而不是“先完整映射，再筛出重点市场”。

优化方向：

- 增加 `competitive_universe`：海外龙头、台湾/日本/欧洲关键供应商、系统集成商、下游客户。
- 增加 `investable_universe`：可交易股票、市场、代码、币种、数据源。
- A 股重点结论必须带一个“海外竞争/对标约束”段落。

### P3. 结构化数据覆盖不足时没有强制降级

现象：两个案例都能拉取 A 股 Tushare 数据，但美股和港股数据没有被系统性拉取。报告中虽然有“未覆盖”备注，但没有影响最终质量门槛。

源头：

- `market_data_notes.md` 是记录文件，不是 gate。
- `run_checklist.md` 只要求生成 CSV，没有要求覆盖 004 中的全部 A/B 候选。

优化方向：

- 新增校验脚本检查 004 是否存在跨市场候选，检查 `symbol_universe.csv` 是否覆盖多个市场或写明缺口。
- `006_pricing.md` 必须列出“已覆盖标的”和“未覆盖标的”。

### P4. 搜索证据和结构化数据之间缺少统一候选主表

现象：004 报告里有候选公司，market_data 里也有 symbol universe，但两者没有强约束。后续容易出现报告写了公司、数据没拉，或者数据拉了但报告没有解释的情况。

源头：`symbol_universe.csv` 字段太少，无法记录候选来源、市场角色、是否需要行情、是否缺数据。

优化方向：

- 扩展 `symbol_universe.csv` 字段：`market_role`、`coverage_required`、`data_provider`、`coverage_status`、`gap_reason`。
- 所有 004 的 A/B 候选都必须进 universe；C 类可选。

### P5. “产业真”和“价格贵”的关系表达还不够产品化

现象：两个案例都识别了主题拥挤，但结论仍容易写成“高优先级研究”。如果没有动作分级，读者可能误解成“买入优先级”。

源头：

- 最终动作选项不够标准化。
- 研究优先级、交易吸引力、估值风险、证据强度没有拆成独立字段。

优化方向：最终结论必须同时给出 `research_priority`、`valuation_gate`、`exposure_proof`、`next_evidence_needed`、`not_investment_advice`。

### P6. 证据台账存在人工维护成本和格式风险

现象：CSV 里如果出现英文逗号，容易造成列错位。不同报告对 evidence level 的写法也不完全一致。

源头：

- `evidence_ledger.csv` 是通用 CSV，但没有校验脚本。
- 字段枚举没有强制。

优化方向：

- 新增校验脚本检查 CSV 是否可解析、列数是否正确。
- 后续可考虑把证据台账迁移为 JSONL 或 YAML，但短期先保留 CSV 并加强校验。

### P7. PowerShell 终端编码导致中文显示乱码

现象：`Get-Content` 在当前 PowerShell 输出中会出现中文 mojibake，但文件本身不一定损坏。

源头：Windows 控制台编码与 UTF-8 文件读取显示不一致。

优化方向：

- 判断文件是否损坏时，以 Python UTF-8 读取、CSV 解析、Markdown 文件实际内容为准，不只看终端显示。
- 校验脚本使用 Python 读取文件。

## 2. 新增控制规则

### R1. 市场范围三分法

每次研究必须在 000 阶段写清楚：

- `primary_focus`: 用户最关心的市场或公司群体，例如中国 A 股。
- `required_comparison_markets`: 为理解竞争、需求和估值必须纳入的市场，例如美股、港股、台股、欧洲、日本。
- `optional_markets`: 可能相关但暂不强制覆盖的市场。

### R2. 004 候选公司清单不得只剩重点市场

即使用户说“以中国上市公司为重点”，004 也必须至少完成：

- 美国/欧洲/日本/台股等海外龙头或对标公司的竞争清单；
- 港股/A 股/其他市场的可投资映射；
- 如果某市场没有直接标的，必须写明理由。

### R3. 006 数据覆盖必须跟随 004

006 不能只拉最方便的数据源。必须先读取 `symbol_universe.csv`：

- `coverage_required = yes` 的标的必须尝试拉取结构化行情；
- 无法拉取的标的必须进入 `market_data_notes.md` 的缺口表；
- 报告中不得把“没拉数据”写成“市场不重要”。

### R4. 重点市场结论必须被全球竞争校准

如果最终报告重点讨论 A 股，则必须包含：

- 海外龙头或供应商是否更直接受益；
- 中国公司的竞争位置、替代空间、认证/客户限制；
- 海外标的涨幅和估值是否已经给出全球定价锚。

## 3. 后续优化路线

已立即优化：

- 新增 `FRAMEWORK_ADDENDUM_CROSS_MARKET.md`，加入跨市场控制层。
- 更新模板，增加市场覆盖字段。
- 新增 `scripts/validate_run.py`，用于检查报告、CSV、市场覆盖和 token 泄露。

下一阶段可做：

- 写一个 `scripts/build_market_data.py`，自动根据 `symbol_universe.csv` 调 Tushare/Yahoo。
- 把 `evidence_ledger.csv` 迁移为 JSONL，降低 CSV 转义风险。
- 为每个行业建立“全球对标公司库”，比如电力设备、液冷、光模块、封装、PCB。
# 追加优化：Component Decomposition 质量门槛

在【数据中心燃气发电机】案例中，流程虽然覆盖了需求、主机/OEM、跨市场候选和结构化市场数据，但研究粒度停在系统/OEM 层，未继续拆解燃机热端部件、叶片、燃烧室、热障涂层、高温合金、精密铸造、后市场服务等更上游环节。

根因：

- prompt chain 原本支持“供给瓶颈”和“标的映射”，但没有强制设备类主题做二级/三级零部件拆解；
- search packet 容易围绕主题词和龙头公司，而漏掉 component/material/process/service 关键词；
- validator 之前只检查跨市场和 market data，不检查拆解深度。

已采取的架构优化：

- 新增 `COMPONENT_DECOMPOSITION_PROTOCOL.md`；
- 新增 `templates/component_decomposition.md`；
- 更新 `AGENTS.md`、`SEARCH_PROTOCOL.md`、`CONTEXT_PACK_PROTOCOL.md`、`templates/run_checklist.md`、`templates/research_state.yaml`；
- 扩展 `scripts/validate_run.py`，对设备/主机/系统/材料/工艺类主题缺少 component decomposition 的情况给出 warning。

后续要求：

- 设备类主题在 `003_supply.md` 之后、`004_targets.md` 之前，应新增 `reports/003_component_decomposition.md`；
- `004_targets.md` 必须把主机/OEM、一级模块、二级零部件、关键材料、工艺设备、后市场/耗材、认证壁垒分开；
- 最终报告必须说明真实瓶颈是在主机层，还是更上游的零部件/材料/工艺层。
