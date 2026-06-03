# Market Data Notes - 数据中心燃气发电机上游拆解版

Data run timestamp: 2026-06-03.  
Structured sources:

- A-share: Tushare `pro.daily` and `pro.daily_basic`.
- Overseas/HK/EU/JP: Yahoo Finance via `yfinance`.
- GEV and CAT reused same-day rows from the previous gas-generator run after transient Yahoo download failures in the rerun. The reused rows are from the same project date and provider path, not model-generated data.

## Coverage

`symbol_universe.csv` contains 25 rows. Twenty-four `coverage_required=yes` symbols were covered in `price_snapshot.csv`, `valuation_snapshot.csv`, and `liquidity_snapshot.csv`.

Covered markets:

- US: GEV, CAT, CMI, GNRC, HWM
- Europe: ENR.DE, WRT1V.HE, OERL.SW
- Japan: 7011.T, 7012.T
- Hong Kong: 2727.HK, 1072.HK, 2338.HK
- A-share: 601727.SH, 600875.SH, 002353.SZ, 000338.SZ, 300153.SZ, 603308.SH, 000534.SZ, 300034.SZ, 300855.SZ, 600399.SH, 688122.SH

Not required:

- 2688.HK ENN Energy was kept as gas-supply context, not a generator or hot-section component supplier.

## Interpretation Rules

- Price strength is expectations evidence, not business proof.
- Component-layer companies should be read through two gates: component exposure proof and valuation/crowding.
- A-share `market_cap` values from Tushare are provider-reported `total_mv`, generally in ten-thousand CNY units.
- Yahoo fast-path valuation fields can be sparse; overseas PE/PB/PS should be treated as incomplete screening fields when blank.
- Return windows use approximate trading-day windows: 1m 21 days, 3m 63 days, 6m 126 days, 12m 252 days.

## Headline Market Read

- Upstream component names are not automatically cheap. Yingliu rose about 197% in 12 months, Wanze about 105%, and Jereh about 314%.
- Hot-section overseas comparable Howmet rose about 45% in 12 months, less extreme than many system/OEM or A-share theme names, but valuation detail needs deeper work.
- Oerlikon appears less crowded by 12-month return, but gas-turbine hot-section coating is only one part of its portfolio.
- Fushun Special Steel and Ketopower show weak 12-month returns, but weak price does not solve the evidence problem.

## Missing Or Weak Data

- Historical valuation percentiles were not calculated.
- Yahoo fast-path left some overseas PE/PB/PS fields blank.
- Sell-side coverage and social-media heat were not counted through a structured dataset.
- Component supplier OEM qualification relationships are only partly public.
- This is not investment advice and should not be interpreted as a buy/sell recommendation.
