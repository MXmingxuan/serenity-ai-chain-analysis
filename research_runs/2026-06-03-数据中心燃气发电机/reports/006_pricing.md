# 006 市场定价、拥挤度与交易风险

本轮使用结构化 market data，而不是通过搜索估计股价和估值。数据文件包括：

- `market_data/symbol_universe.csv`
- `market_data/price_snapshot.csv`
- `market_data/valuation_snapshot.csv`
- `market_data/liquidity_snapshot.csv`
- `market_data/market_data_notes.md`

## 1. 股价表现

| 公司 | 1 个月 | 3 个月 | 6 个月 | 12 个月 | 是否已明显定价 |
|---|--:|--:|--:|--:|---|
| GE Vernova | -8.78% | 15.16% | 61.67% | 96.70% | 是，AI 电力链已显著定价 |
| Caterpillar | 2.26% | 25.98% | 58.02% | 160.39% | 是 |
| Cummins | 2.32% | 20.10% | 35.08% | 107.31% | 是 |
| Generac | 9.73% | 28.65% | 87.68% | 123.67% | 是，但直接证据弱 |
| Siemens Energy | -12.82% | 2.42% | 39.13% | 79.80% | 是 |
| Wartsila | -1.38% | -2.36% | 30.82% | 96.86% | 是 |
| Mitsubishi Heavy | -22.58% | -28.74% | -7.32% | 6.21% | 相对不拥挤，但需结合长期涨幅 |
| Kawasaki Heavy | -11.83% | -22.31% | 41.88% | 31.02% | 中等 |
| Shanghai Electric H | 3.51% | -12.68% | 3.77% | 52.96% | 中等 |
| Dongfang Electric H | -17.81% | -17.69% | 64.63% | 169.26% | 是 |
| Weichai Power H | -7.94% | 22.26% | 115.22% | 157.29% | 是 |
| Shanghai Electric A | -1.73% | -10.99% | -4.68% | 7.73% | 低中 |
| Dongfang Electric A | -14.36% | -10.93% | 64.58% | 107.00% | 是 |
| Jereh Group | 4.41% | 14.44% | 181.08% | 313.89% | 极高 |
| Weichai Power A | 3.43% | 16.41% | 93.70% | 116.43% | 是 |
| Ketopower | -17.34% | -32.27% | -10.38% | -10.47% | 低，但基本面证据弱 |

## 2. 估值状态

| 公司 | 当前估值 | 同业比较 | 是否合理 | 备注 |
|---|---|---|---|---|
| GE Vernova | PE 28.3x, PB 18.7x, PS 6.6x | 相对高质量电力设备龙头 | 偏贵 | 订单和服务弹性强，但 PB 很高 |
| Caterpillar | PE 45.2x, PB 22.5x | 工程机械/电力系统龙头 | 偏贵 | 涨幅大，主题和周期双重定价 |
| Cummins | PE 35.0x, PB 7.5x | 发动机/电力系统 | 偏贵 | 经营证据较强但估值已抬升 |
| Generac | PE 89.2x | 备用电源 | 很贵 | 直接 hyperscale gas 证据弱 |
| Siemens Energy | PE 62.7x | 欧洲电力设备 | 偏贵 | 叙事强，订单转化待验证 |
| Wartsila | PE 31.9x | 燃气发动机/灵活电源 | 中高 | 有 S 级订单证据，估值仍需跟踪 |
| Mitsubishi Heavy | PE 34.1x, PS 2.4x | 日本重工/燃机 | 中高 | 近期回调明显，直接项目证据强 |
| Shanghai Electric A/H | A 股 PE 95.3x，H 股 PE 41.3x | 中国电力设备 | 偏贵/中高 | 直接数据中心证据弱 |
| Dongfang Electric A/H | A 股 PE 27.1x，H 股 PE 22.6x | 中国电力设备 | 中等 | 涨幅已大，直接证据弱 |
| Jereh Group | PE 52.2x, PS 8.7x | 油气设备/燃气发电映射 | 很贵 | 产品映射强但价格极度拥挤 |
| Weichai Power A/H | PE 24.7x / 26.2x | 动力系统 | 中高 | 12 个月涨幅大，数据中心直接性不足 |
| Ketopower | PE 145.8x | 备用电源 | 很贵 | 价格弱但估值仍高，证据弱 |

## 3. 拥挤度判断

| 标的 | 拥挤度 | 判断 |
|---|---|---|
| Jereh Group | 极高 | 12 个月 +313.89%，估值高，且直接订单证据仍需验证 |
| CAT / CMI / GNRC | 高 | 12 个月涨幅均超过 100%，估值不便宜 |
| GEV / Siemens Energy / Wartsila | 高 | 证据强但市场已明显定价 |
| Dongfang Electric H/A、Weichai H/A | 高 | 6-12 个月涨幅显著，直接数据中心证据不足 |
| Mitsubishi Heavy | 中等 | 有直接项目证据，近期回调，拥挤度低于 GEV/Wartsila |
| Shanghai Electric A/H | 中低到中等 | 价格相对不极端，但订单证据弱 |
| Ketopower | 中等偏高 | 股价不强，但估值高且证据弱 |

## 4. 预期收益与回撤风险

- 如果产业逻辑正确，未来上涨空间主要来自订单落地、backlog 披露、数据中心收入占比提高和服务合同利润率提升。
- 如果只是业绩符合预期，已经大涨的标的可能不再上涨，因为市场已提前定价。
- 如果业绩低于预期，可能同时杀估值和杀主题逻辑，尤其是证据弱但涨幅大的 A/H 股映射标的。
- 最大回撤风险来自：AI 电力 capex 降温、燃气项目许可受阻、数据中心转向 utility/PPA/核电/储能、直接订单未兑现、估值过高。

## 5. 本轮小结

- 最有吸引力的标的：Mitsubishi Heavy、Wartsila、Cummins、GE Vernova，但都需要估值门槛；其中 Mitsubishi Heavy 近期回调后相对没那么拥挤。
- 逻辑好但价格贵的标的：GE Vernova、Caterpillar、Cummins、Siemens Energy、Wartsila、Jereh Group。
- 明显拥挤的标的：Jereh Group、CAT、CMI、GNRC、Dongfang Electric H、Weichai H/A。
- 下一步需要建立反证条件：尤其是订单、项目许可、估值反应和 AI capex 变化。
