# Serenity AI Chain Analysis

这是一个用于运行 AI 产业链瓶颈研究的 prompt-chain 项目。项目核心是一组从 `000.md` 到 `009.md` 的提示词，用来把一个研究对象从“对象定义”逐步推进到“产业链位置、需求验证、供给瓶颈、标的映射、证据分级、市场定价、反证条件、最终报告和研究卡片”。

## 项目目标

本项目不是自动交易系统，也不是直接给出买卖建议。它的目标是沉淀一个可复用的研究雷达：

- 寻找 AI 超级周期中可能出现的产业链瓶颈；
- 区分产业事实、合理推理、市场叙事和未验证假设；
- 保留负面证据和反证条件；
- 把每轮研究输出成可追溯的 Markdown 报告、证据台账和结构化市场数据。

## Prompt Chain

| 步骤 | 文件 | 作用 |
|---|---|---|
| 000 | `000.md` | 启动研究与界定对象 |
| 001 | `001.md` | 判断产业链位置与 N 阶传导 |
| 002 | `002.md` | 验证需求源头和需求加速 |
| 003 | `003.md` | 分析供给弹性和瓶颈强度 |
| 004 | `004.md` | 映射候选公司和利润兑现路径 |
| 005 | `005.md` | 做证据分级和叙事拆分 |
| 006 | `006.md` | 分析市场定价、估值和拥挤度 |
| 007 | `007.md` | 建立风险和反证条件 |
| 008 | `008.md` | 输出综合研究报告 |
| 009 | `009.md` | 沉淀研究卡片 |

## 核心框架

- `AGENT_FRAMEWORK.md`：主研究框架。
- `FRAMEWORK_ADDENDUM_CROSS_MARKET.md`：跨市场控制层，防止把“重点研究 A 股/中国上市公司”误执行成“只研究 A 股/中国上市公司”。
- `AGENTS.md`：给后续 agent 的项目入口规则。
- `PROJECT_RETRO_AND_OPTIMIZATION.md`：基于两个案例复盘后的问题清单、根因和优化方向。

## 数据层

项目区分两类数据来源：

- 结构化市场数据：A 股优先使用 Tushare；美股、港股和部分海外市场优先使用本地 Yahoo Finance CLI 工具 `tools/yf`。
- 公开信息搜索：用于公司公告、年报、供应链证据、卖方覆盖、社媒热度和热门共识判断。

密钥安全规则：

- 不把 Tushare token 或其他密钥写入 Markdown、CSV、YAML 或脚本。
- 默认从环境变量 `TUSHARE_TOKEN` 读取。
- 提交前运行校验脚本和敏感信息扫描。

## 目录结构

```text
.
├── 000.md ... 009.md
├── AGENT_FRAMEWORK.md
├── FRAMEWORK_ADDENDUM_CROSS_MARKET.md
├── AGENTS.md
├── PROJECT_RETRO_AND_OPTIMIZATION.md
├── scripts/
│   └── validate_run.py
├── templates/
├── tools/
│   └── yf
├── skills/
├── .agents/
└── research_runs/
```

## 已完成案例

### 数据中心电力设备

目录：`research_runs/2026-06-03-数据中心电力设备中国上市公司`

结论摘要：数据中心电力设备是 AI 基础设施从算力传导到电力容量的二阶/三阶机会，但需要补充海外电力设备龙头和全球定价锚。

### 液冷二级零部件

目录：`research_runs/2026-06-03-液冷二级零部件`

结论摘要：液冷需求真实，但“液冷龙头”已被市场充分关注；更值得拆的是管路、流体连接器、冷板、manifold、泵阀、密封/材料等二级或三级零部件。

## 运行校验

每次完成一个研究目录后，运行：

```powershell
python scripts\validate_run.py "research_runs\YYYY-MM-DD-研究对象"
```

校验内容包括：

- 000-009 报告是否齐全；
- 证据台账和市场数据 CSV 是否可解析；
- `004_targets.md` 是否有跨市场覆盖；
- `symbol_universe.csv` 是否只覆盖单一市场；
- 是否误写入 Tushare token。

## GitHub 同步注意

可以上传研究框架、模板、脚本、提示词、案例报告和不含密钥的数据文件。不要上传本地环境变量、私密 token、临时缓存、`__pycache__` 或虚拟环境目录。
