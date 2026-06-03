# Market Data Notes

研究对象：
运行目录：
数据日期：

## 数据源覆盖

| 市场 | 数据源/接口 | 覆盖范围 | 限制 | 缺口处理 |
|---|---|---|---|---|
| A 股 | Tushare |  |  |  |
| 港股 | Yahoo Finance CLI / Tushare |  |  |  |
| 美股 | Yahoo Finance CLI / Tushare |  |  |  |
| 其他市场 | Yahoo Finance CLI / web / exchange |  |  |  |

## 已覆盖标的

| symbol | market | name | provider | fields | as_of |
|---|---|---|---|---|---|

## 缺失数据

| symbol | market | name | missing_field | reason | handling |
|---|---|---|---|---|---|

## 数据冲突

| symbol | field | source_a | source_b | handling |
|---|---|---|---|---|

## 第 006 步使用说明

- 股价涨幅、成交额、换手率、估值优先引用结构化数据。
- A 股优先使用 Tushare。
- 美股、港股、ETF、台股和部分海外市场可使用 `uv run --script tools/yf ...`。
- 卖方覆盖、社媒热度、热门共识用搜索补充。
- 如果估值字段缺失，只能写“数据缺失”，不能凭印象判断。
- 如果 004 包含某市场候选，但 006 没有结构化数据，必须在本文件写明缺口。
