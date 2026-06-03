# Market Data Notes - 数据中心燃气发电机

Data run timestamp: 2026-06-03.  
Structured sources:

- A-share: Tushare `pro.daily` and `pro.daily_basic`.
- Overseas/HK/EU/JP: Yahoo Finance via `yfinance`.

## Coverage

`symbol_universe.csv` contains 17 rows. Sixteen `coverage_required=yes` symbols were covered in `price_snapshot.csv`, `valuation_snapshot.csv`, and `liquidity_snapshot.csv`.

Covered markets:

- US: GEV, CAT, CMI, GNRC
- Europe: ENR.DE, WRT1V.HE
- Japan: 7011.T, 7012.T
- Hong Kong: 2727.HK, 1072.HK, 2338.HK
- A-share: 601727.SH, 600875.SH, 002353.SZ, 000338.SZ, 300153.SZ

Not required:

- 2688.HK ENN Energy was kept as gas-supply context, not a generator or gas-turbine OEM.

## Interpretation Rules

- Price strength is expectations evidence, not business proof.
- A-share `market_cap` values from Tushare are provider-reported `total_mv`, generally in ten-thousand CNY units.
- Yahoo `market_cap` values are provider-reported raw market capitalization in local currency.
- PE/PB/PS fields are provider fields, not normalized valuation models.
- Turnover-rate fields are available for A-shares through Tushare. Overseas liquidity uses traded value approximated as volume times latest close.
- Return windows use approximate trading-day windows: 1m 21 days, 3m 63 days, 6m 126 days, 12m 252 days.

## Headline Market Read

- Highly priced or expectations-heavy names include GEV, CAT, CMI, GNRC, ENR.DE, WRT1V.HE, 002353.SZ, 000338.SZ, 2338.HK, 600875.SH, and 1072.HK, based on large 6-12 month gains and/or elevated PE/PB.
- The strongest evidence names are not necessarily the cheapest names. Wartsila and Mitsubishi Heavy have stronger direct project evidence than several A-share names, but their market prices also reflect part of the theme.
- China-listed candidates are mixed: Jereh Group has the strongest product mapping among A-share names but also shows extreme 12-month price strength; Shanghai Electric has lower price momentum but weaker direct data-center order evidence.

## Missing Or Weak Data

- Historical valuation percentiles were not calculated in this pass.
- Sell-side coverage and social-media heat were assessed qualitatively, not counted through a structured news/social dataset.
- Yahoo fields can be incomplete or differ by listing venue. Treat overseas valuation fields as screening inputs, not final valuation work.
- This is not investment advice and should not be interpreted as a buy/sell recommendation.
