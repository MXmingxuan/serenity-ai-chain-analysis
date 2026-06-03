# 003_component_decomposition 上游零部件拆解

## 1. 为什么必须拆到零部件层

上一版研究证明了 AI 数据中心缺电正在推动部分项目采用 onsite / behind-the-meter gas power，但如果研究停在 GE Vernova、Mitsubishi、Wartsila、Cummins、Siemens Energy、上海电气、东方电气、杰瑞股份这些主机或系统公司，就会漏掉真正供给弹性更差的层级。

燃气轮机和燃气发动机的瓶颈不只在整机装配，而在：

- 高温热端部件；
- 高温合金材料；
- 单晶 / 定向凝固 / 精密铸造；
- 热障涂层和表面防护；
- 维修备件和长期服务协议；
- OEM 认证和批量交付记录。

因此本轮把“数据中心燃气发电机”拆成“主机/OEM -> 一级模块 -> 二级零部件 -> 材料/工艺 -> 后市场服务”的链条。

## 2. Layered Map

| layer | node | function | bottleneck reason | evidence level | source |
|---|---|---|---|---|---|
| system/OEM | GE Vernova, Mitsubishi Power, Siemens Energy, Wartsila, Cummins | 交付燃机、燃气发动机或数据中心电力方案 | 订单、交期、服务能力、项目许可 | A/S | GE/Wartsila/Mitsubishi/Cummins official |
| first-level module | turbine island, gas engine block, generator set, switchgear, balance of plant | 决定系统效率、可靠性和交付 | 模块集成、冗余和数据中心认证 | A/B | OEM product and project sources |
| second-level part | turbine blades, vanes, combustor liners, shrouds, transition pieces, seals | 承受最高温、高压、腐蚀和疲劳 | 制造难度高、良率和认证周期长 | B | Howmet, Oerlikon, Yingliu, MHI sources |
| critical material | superalloy, single crystal alloy, powder alloy, ceramic core, thermal barrier coating | 决定温度承受能力和寿命 | 材料体系、纯净度、组织稳定性、涂层工艺 | B | Gangyan Gaona, Wanze, Tunan, Oerlikon |
| process/equipment | precision casting, directional solidification, coating, heat treatment, NDT, machining | 决定批产良率和一致性 | 资本密集、 know-how 密集、首件鉴定和客户认证 | B | Yingliu Group, MHI Dongfang JV |
| aftermarket/service | hot gas path inspection, spare parts, long-term service agreement, repair coating | 形成持续收入 | 运行小时驱动换件和维修 | A/B | Siemens Energy and Oerlikon service/coating sources |
| certification/customer qualification | OEM qualification, data-center reliability requirement, environmental permits | 决定替代速度 | 供应商导入慢，客户不愿轻易换核心热端件 | B | company and industry sources |

## 3. Hard-To-Replace Components

| component | why hard | likely suppliers | listed-company mapping | evidence gap |
|---|---|---|---|---|
| 透平叶片 / 动叶 | 高温、蠕变、疲劳、冷却结构复杂，是燃机热端核心 | Howmet, 应流股份, 万泽股份, 钢研高纳, 图南股份 | HWM, 603308.SH, 000534.SZ, 300034.SZ, 300855.SZ | 数据中心燃机订单传导到具体供应商的比例不透明 |
| 导向叶片 / 静叶 | 控制高温燃气流场，对材料和尺寸精度要求高 | Howmet, 应流股份, 钢研高纳, MHI 东方燃机 JV | HWM, 603308.SH, 300034.SZ | OEM 认证和型号覆盖需逐项验证 |
| 燃烧室 / 火焰筒 / 过渡段 | 受热冲击、腐蚀和排放控制影响 | Siemens/MHI/GE 体系供应商、部分高温合金加工企业 | 603308.SH, 000534.SZ, 300034.SZ 等观察 | 中国上市公司直接披露有限 |
| 热障涂层 / MCrAlY / 陶瓷涂层 | 延长热端寿命，提高服役温度 | Oerlikon, OEM 内部涂层线, 应流延伸涂层能力 | OERL.SW, 603308.SH | 涂层收入和客户绑定难量化 |
| 高温合金母合金 / 单晶合金 | 决定叶片承温、寿命和良率 | 钢研高纳、万泽股份、图南股份、抚顺特钢、西部超导 | 300034.SZ, 000534.SZ, 300855.SZ, 600399.SH, 688122.SH | 航发/燃机/数据中心燃机需求拆分不足 |
| 后市场热端维修和备件 | 燃机全生命周期需要多次中修/大修 | OEM, Howmet, Oerlikon, MHI Dongfang JV | HWM, OERL.SW, 7011.T | 备件与服务收入披露粒度不足 |

## 4. Profit Conversion Path

| layer | revenue elasticity | margin elasticity | recurrence | main risk |
|---|---|---|---|---|
| system/OEM | 高 | 中高 | 高，服务合同驱动 | 估值已高、项目延期、客户压价 |
| hot gas path parts | 中高 | 高 | 中高，运行小时驱动换件 | 认证周期长、订单传导不透明 |
| superalloy/material | 中 | 中高 | 中 | 航发需求和燃机需求混合，收入拆分难 |
| coating/process | 中 | 中高 | 高，维修和翻新驱动 | 多数能力在 OEM 或私人公司内 |
| aftermarket/service | 高 | 高 | 高 | 数据披露少，可能被 OEM 吃掉大部分利润 |

## 5. Impact On 004 Targets

拆解后，候选池需要明显调整：

- 海外不只看 GE Vernova / Siemens / Mitsubishi / Wartsila，还要加入 Howmet Aerospace 和 Oerlikon 作为热端部件与涂层对标。
- A 股不只看杰瑞、上海电气、东方电气、潍柴，还要加入应流股份、万泽股份、钢研高纳、图南股份、抚顺特钢、西部超导。
- 对中国公司不能直接写“受益数据中心燃气发电机”，应写为“若全球燃机需求上行，热端部件/高温合金国产供应链可能受益；但需要订单、型号、客户和收入占比验证”。
- 真正更像瓶颈的不是普通发电机组，而是热端叶片、导向叶片、燃烧室、单晶/定向凝固高温合金、涂层与维修服务。

## 6. Gaps

- 具体 OEM 对应供应商名单多为非公开认证关系，难以完全验证。
- 海外热端件供应链中 Precision Castparts、Chromalloy、Doncasters 等大量为非上市或集团内部资产，可投映射有限。
- 中国上市公司多披露“两机”或“燃气轮机”能力，较少拆到数据中心燃机订单。
- 后市场服务和热端维修利润率强，但披露粒度不足。

## 7. 本轮小结

上游拆解后，本主题的真实瓶颈从“燃气发电机主机”进一步收敛到“燃机热端部件 + 高温合金材料 + 精密铸造/涂层 + 后市场服务”。这使得应流股份、万泽股份、钢研高纳、图南股份、Howmet、Oerlikon 等进入候选池，但它们的证据等级必须与主机订单证据区分开。
