# Source Index - 液冷二级零部件

Run: 2026-06-03-液冷二级零部件  
Research object: AI 数据中心液冷系统中的二级/三级零部件，重点关注中国上市公司股票。

## Platform And Demand Sources

| id | source | type | use in chain | url |
|---|---|---|---|---|
| S001 | NVIDIA Technical Blog: GB200 NVL72 rack-scale design | OEM technical source | GB200/NVL72 明确采用液冷 compute tray，确认高功率 AI rack 对液冷架构的需求 | https://developer.nvidia.com/blog/nvidia-gb200-nvl72-delivers-trillion-parameter-llm-training-and-real-time-inference/ |
| S002 | NVIDIA Technical Blog: GB200 NVL72 designs contributed to OCP | OEM/open-standard source | OCP 贡献范围包括 rack、compute/switch tray liquid-cooled designs，用于判断标准化与供应链扩散 | https://developer.nvidia.com/blog/?p=90182 |
| S003 | NVIDIA Newsroom: Blackwell platform design to open hardware ecosystem | OEM official source | 提到 rack architecture、liquid-cooling and thermal environment specifications 等关键设计开放 | https://nvidianews.nvidia.com/news/nvidia-contributes-blackwell-platform-design-to-open-hardware-ecosystem-accelerating-ai-infrastructure-innovation/ |
| S004 | NVIDIA Blog: Blackwell liquid cooling improves water efficiency | OEM official source | 支持“液冷提高 AI 基础设施效率”的需求端叙事 | https://blogs.nvidia.com/blog/blackwell-platform-water-efficiency-liquid-cooling-data-centers-ai-factories/ |
| S005 | NVIDIA DGX GB Rack Scale Systems user guide | OEM documentation | 支持 rack 内 liquid cooling manifolds、compute trays 等结构拆分 | https://docs.nvidia.com/dgx/dgxgb200-user-guide/dgxgb200-user-guide.pdf |
| S006 | arXiv: Glacierware hotspot-aware microfluidic cooling | Academic paper | 支持冷板/微通道设计影响热点控制与压降权衡 | https://arxiv.org/abs/2408.15024 |
| S007 | arXiv: Generative Design for Direct-to-Chip Liquid Cooling for Data Centers | Academic paper | 支持 GB200 级别 direct-to-chip cooling 设计复杂度与优化空间 | https://arxiv.org/abs/2604.10941 |

## Component And Company Sources

| id | source | type | use in chain | url |
|---|---|---|---|---|
| S101 | 川环科技液冷管路系统批量供货 | Media / company interactive summary | 支持川环科技已有数据中心/服务器液冷管路批量供货线索 | https://www.yicai.com/news/102207749.html |
| S102 | 证券时报: 川环科技半年报更新液冷业务进展 | Media / filing digest | 支持“客户验证合格、批量供货、V0/UL、进入多个供应商体系”等关键证据 | https://stcn.com/article/detail/3091482.html |
| S103 | 华尔街见闻: 川环科技 60,000 套服务器液冷管路订单 | Media / order report | 支持川环科技液冷管路订单线索，但仍需公告原文复核交付与收入确认 | https://wallstreetcn.com/articles/3737821 |
| S104 | 中航光电 2024 年年度报告 | Company filing | 支持液冷解决方案及其他产品、流体连接器、流体传输管路、液冷板、液冷源等产品口径 | https://pdf.dfcfw.com/pdf/H2_AN202503281648753204_1.pdf |
| S105 | 通信世界网: 中航光电液冷技术 | Industry media | 支持中航光电产品覆盖冷板、流体连接器、Manifold、CDU 等液冷链条 | https://www.cww.net.cn/article?id=590260 |
| S106 | 洛阳网: 中航光电液冷业务近五年复合增长 | Local media / company feature | 支持冷板、液冷源、管路、流体连接器应用于数据中心等领域 | https://news.lyd.com.cn/system/2024/09/19/032465671.shtml |
| S107 | 大元泵业 2024 年年度报告 | Company filing | 支持屏蔽泵/液冷泵作为液冷可靠性环节，同时提示热管理价值量占比低 | https://www.100est.com/res/financial-report/r2024/SH603757_202504271663302654.pdf |
| S108 | 每日经济新闻: 大元泵业数据中心液冷收入占比披露 | Media / company interview | 用于负面约束：一季度可识别直接用于数据中心液冷产品销售收入占比很小 | https://www.nbd.com.cn/articles/2025-08-26/4030074.html |
| S109 | 瑞可达 2024 年年度报告 | Company filing | 支持连接器技术储备，但数据中心 UQD 更强证据仍待后续年报/公告确认 | https://static.cninfo.com.cn/finalpage/2025-04-15/1223095502.PDF |
| S110 | Molex data center cold plate liquid cooling | Supplier technical source | 用于理解冷板、歧管、管路工厂密封/压力测试的供应链约束 | https://www.molex.com/zh-cn/industries-applications/data-center-thermal-management/cold-plate-liquid-cooling |
| S111 | Amphenol / Mouser UQD/UQDB/BMQC connector product page | Supplier technical source | 用于验证液冷连接器规格、OCP ORv3、盲插、快断等技术门槛 | https://www.mouser.cn/new/amphenol/amphenol-uqd-uqdb-bmqc-lqc-mqd-connectors/ |

## Structured Market Data Sources

| id | source | type | files |
|---|---|---|---|
| D001 | Tushare pro.daily | Structured market data | `market_data/price_snapshot.csv` |
| D002 | Tushare pro.daily_basic | Structured valuation/liquidity data | `market_data/valuation_snapshot.csv`, `market_data/liquidity_snapshot.csv` |

## Source Quality Notes

- Highest-weight evidence: NVIDIA/OCP/OEM documentation, company filings, Tushare structured data.
- Medium-weight evidence: reputable financial media summarizing filings, interactive-platform responses, industry media.
- Lower-weight evidence: sell-side notes and narrative media. Use only for lead generation unless validated by filings or company disclosures.
- Key unresolved issue: many A-share companies disclose liquid-cooling capability but not data-center-specific revenue. Names without revenue/order proof remain `needs exposure attribution`.
