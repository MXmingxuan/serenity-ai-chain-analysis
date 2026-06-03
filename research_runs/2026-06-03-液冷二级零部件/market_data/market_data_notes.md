# Market Data Notes - 液冷二级零部件

Data timestamp: 2026-06-02 latest available A-share trading day from Tushare at collection time.  
Provider: Tushare `pro.daily` for prices and returns; Tushare `pro.daily_basic` for PE/PB/PS, turnover, volume ratio and amount.

## Universe

The market snapshot covers 14 A-share names mapped to liquid-cooling component pathways:

- A-class research candidates: 川环科技、中航光电、华丰科技、大元泵业
- B-class watchlist: 瑞可达、永贵电器、科创新源、同飞股份、三花智控、银轮股份、飞荣达
- Reference/system leaders: 英维克、高澜股份、申菱环境

## Interpretation Rules

- Price strength is treated as expectations evidence, not business proof.
- A name with strong returns but weak revenue attribution is labeled `valuation-gated` or `needs exposure attribution`.
- A name with filing/order evidence but moderate valuation is preferred for deeper research over a pure theme mover.
- `crowded` is not used as a hard label unless direct positioning/flow evidence exists. This run uses `expectations-heavy` where evidence is mainly price and valuation.

## Headline Market Read

- Expectations-heavy names: 华丰科技、大元泵业、瑞可达、科创新源、申菱环境、高澜股份、飞荣达 all have large 12-month gains and/or high valuation multiples.
- More balanced starting points: 川环科技 and 中航光电 have stronger business-exposure evidence relative to their market-data profile.
- System leaders: 英维克、高澜、申菱 remain important reference points, but their prices already embed broad liquid-cooling narrative attention.

## Caveats

- Tushare valuation fields are provider-reported market multiples, not normalized model valuations.
- `return_1m/3m/6m/12m` are point-to-point close-price returns over approximate trading-day windows.
- Sell-side coverage, social-media heat, customer concentration and order conversion were not fully quantified in this pass.
- The research conclusion is a research-priority funnel, not investment advice or a buy/sell recommendation.

## Missing Market Coverage

This first-pass run used A-share structured data only. US, HK, Taiwan, Japan and Europe listed competitors were discussed qualitatively in supply-chain analysis but were not included in `symbol_universe.csv` or market-data snapshots.

Handling: later reruns must add overseas component and system comparables, then use Yahoo Finance CLI or other market-specific data sources before writing `006_pricing.md`.
