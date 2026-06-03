# 006 市场定价、拥挤度与交易风险（上游拆解版）

本轮使用结构化 market data，并把系统/OEM 与上游热端件/材料/工艺公司一起纳入比较。数据文件包括：

- `market_data/symbol_universe.csv`
- `market_data/price_snapshot.csv`
- `market_data/valuation_snapshot.csv`
- `market_data/liquidity_snapshot.csv`
- `market_data/market_data_notes.md`

## 1. 股价表现

| 公司 | 层级 | 1 个月 | 3 个月 | 6 个月 | 12 个月 | 是否已明显定价 |
|---|---|--:|--:|--:|--:|---|
| Jereh Group | system/module | 4.41% | 14.44% | 181.08% | 313.89% | 极高 |
| Yingliu | hot-section parts/process | -15.49% | -4.84% | 76.10% | 197.21% | 极高 |
| Dongfang Electric H | system/OEM | -17.81% | -17.69% | 64.63% | 169.26% | 高 |
| Caterpillar | system/OEM | 2.26% | 25.98% | 58.02% | 160.39% | 高 |
| Weichai Power H | module | -7.94% | 22.26% | 115.22% | 157.29% | 高 |
| Generac | system/OEM | 9.73% | 28.65% | 87.68% | 123.67% | 高但证据弱 |
| Weichai Power A | module | 3.43% | 16.41% | 93.70% | 116.43% | 高 |
| Cummins | system/OEM | 2.32% | 20.10% | 35.08% | 107.31% | 高 |
| Dongfang Electric A | system/OEM | -14.36% | -10.93% | 64.58% | 107.00% | 高 |
| Wanze | superalloy blades | -21.98% | -22.08% | 52.22% | 105.33% | 高 |
| Wartsila | system/OEM | -1.15% | -2.14% | 31.12% | 97.31% | 高 |
| GE Vernova | system/OEM | -8.78% | 15.16% | 61.67% | 96.70% | 高 |
| Siemens Energy | system/OEM | -12.17% | 3.18% | 40.16% | 81.13% | 高 |
| Shanghai Electric H | system/OEM | 3.51% | -12.68% | 3.77% | 52.96% | 中 |
| Tunan | superalloy materials | -13.03% | -24.84% | 25.40% | 49.82% | 中高 |
| Howmet | hot-section components | 4.68% | -3.14% | 22.55% | 45.25% | 中 |
| Kawasaki Heavy | system/OEM | -11.83% | -22.31% | 41.88% | 31.02% | 中 |
| Western Superconducting | advanced materials | -1.27% | -29.79% | -0.02% | 29.72% | 中但证据弱 |
| Gangyan Gaona | superalloy materials | -8.40% | -23.70% | 14.07% | 13.42% | 中低 |
| Shanghai Electric A | system/OEM | -1.73% | -10.99% | -4.68% | 7.73% | 低中 |
| Mitsubishi Heavy | system/OEM/service | -22.58% | -28.74% | -7.32% | 6.21% | 中低，近期回调 |
| Oerlikon | coating/process | 9.37% | -11.70% | 24.09% | 0.95% | 低中 |
| Ketopower | backup power | -17.34% | -32.27% | -10.38% | -10.47% | 低但证据弱 |
| Fushun Special Steel | materials | -16.64% | -41.46% | -13.14% | -12.98% | 低但证据间接 |

## 2. 估值状态

| 公司 | 当前估值 | 备注 |
|---|---|---|
| Yingliu | PE 115.1x, PB 8.75x, PS 13.79x | 热端件映射最清晰之一，但估值非常高 |
| Wanze | PE 77.9x, PB 9.15x, PS 11.95x | 单晶叶片能力相关，价格和估值都不便宜 |
| Gangyan Gaona | PE 143.8x, PB 3.72x, PS 3.81x | 材料龙头映射，但 PE 高且燃机拆分不足 |
| Tunan | PE 64.6x, PB 6.42x, PS 11.43x | 高温合金材料映射，估值中高 |
| Jereh Group | PE 52.2x, PB 6.23x, PS 8.70x | 数据中心燃气发电机组产品映射强，12m 涨幅极端 |
| Western Superconducting | PE 58.2x, PB 5.79x, PS 7.93x | 高端材料远端映射，证据弱 |
| Ketopower | PE 145.8x, PB 9.15x | 备用电源证据弱，估值高 |
| GE Vernova | PE 28.3x, PB 18.7x, PS 6.6x | 主机证据强，但 PB 高 |
| Caterpillar | PE 45.2x, PB 22.5x | 电力系统和周期双重定价 |
| Howmet | Yahoo fast-path估值字段不完整 | 需进一步用财报拆工业燃机热端件占比 |
| Oerlikon | Yahoo fast-path估值字段不完整 | 需拆涂层和燃机热端业务占比 |

## 3. 拥挤度判断

| 标的 | 拥挤度 | 判断 |
|---|---|---|
| Jereh Group | 极高 | 12 个月 +313.89%，产品映射强但直接订单仍需验证 |
| Yingliu | 极高 | 12 个月 +197.21%，热端件映射强，估值已很满 |
| Wanze | 高 | 12 个月 +105.33%，估值高，燃机/航发收入拆分需跟踪 |
| CAT / CMI / GNRC / GEV / Wartsila / Siemens Energy | 高 | AI 电力链或燃机景气已被市场关注 |
| Howmet | 中 | 组件层更纯，但 12 个月也已上涨 45.25%，估值需补 |
| Oerlikon / Mitsubishi Heavy / Gangyan Gaona / Shanghai Electric A | 中低 | 价格相对不极端，但证据或业务占比不够直接 |
| Fushun Special Steel / Ketopower | 低到中 | 价格弱，但不代表逻辑强 |

## 4. 上游拆解后的定价结论

- 上游 component layer 比系统/OEM 更值得研究，但并不等于更便宜。
- A 股热端件和高温合金标的已经明显被市场关注，尤其应流股份、万泽股份、杰瑞股份。
- Howmet/Oerlikon提供了海外组件层对标，但需要进一步拆工业燃机业务占比和估值。
- 价格相对不极端的公司往往证据也更间接，例如 Oerlikon、Gangyan Gaona、Fushun Special Steel、Shanghai Electric A。

## 5. 本轮小结

- 最有吸引力的标的：Howmet、Mitsubishi Heavy、Oerlikon、Gangyan Gaona，但都需要进一步验证业务占比；不是直接买入结论。
- 逻辑好但价格贵的标的：Yingliu、Wanze、GEV、Wartsila、Cummins、Jereh。
- 明显拥挤的标的：Jereh、Yingliu、CAT、Weichai H/A、Dongfang H/A、Wanze。
- 下一步需要建立反证条件：尤其是 component 订单传导、OEM 认证、热端件收入占比和估值回落。
