# Component Decomposition Protocol

This protocol prevents equipment-heavy themes from stopping at the system integrator or headline OEM layer.

## When It Applies

Apply this protocol when the research object involves:

- equipment, machinery, power systems, turbines, generators, engines, cooling systems, optical modules, servers, packaging equipment, manufacturing tools, or industrial systems;
- phrases such as "不要只看龙头", "二级零部件", "上游零部件", "热端部件", "材料", "耗材", "维修服务";
- any theme where the most interesting bottleneck may sit upstream of the listed system company.

## Required Output

For applicable runs, create:

```text
reports/003_component_decomposition.md
```

This report can be written after `003_supply.md` and before `004_targets.md`. It does not replace `003_supply.md`; it deepens it.

## Required Decomposition Layers

Use the following layers unless the industry clearly needs a different split:

| layer | question | examples |
|---|---|---|
| system / OEM | Who sells the complete system? | gas turbine OEM, CDU maker, power equipment integrator |
| first-level modules | What modules determine performance or delivery? | turbine island, gas engine block, cold plate, manifold, switchgear |
| second-level parts | Which parts are hard to make or qualify? | turbine blades, vanes, combustor liners, seals, pump valves |
| critical materials | Which materials constrain quality or cost? | superalloy, thermal barrier coating, fluorinated materials, copper |
| process / equipment | Which process creates the bottleneck? | precision casting, coating, heat treatment, NDT, machining |
| aftermarket / consumables | Which recurring parts or services have pricing power? | hot gas path repair, spare parts, long-term service agreements |
| certification / customer qualification | What slows supplier substitution? | data-center qualification, OEM certification, safety/environmental permits |

## Search Requirements

Search packet queries should include component terms, not only theme or OEM terms.

For a gas turbine or gas generator run, include queries such as:

- `gas turbine hot gas path components data center demand`
- `gas turbine blades vanes combustor liners superalloy suppliers`
- `燃气轮机 叶片 热端部件 高温合金 上市公司`
- `燃机 热障涂层 精密铸造 无损检测`
- `gas turbine long term service agreement spare parts`

## Candidate Mapping Rules

`004_targets.md` must distinguish:

- system/OEM candidates;
- module suppliers;
- second-level part suppliers;
- material/process suppliers;
- aftermarket and service companies;
- theme-only names with no exposure proof.

Do not promote a component supplier to high priority unless there is evidence for at least one of:

- direct revenue exposure;
- OEM qualification or customer certification;
- capacity constraint, long lead time, or delivery bottleneck;
- margin/pricing evidence;
- recurring aftermarket or consumables demand.

## Evidence Discipline

- Component adjacency is not enough.
- If only a company product catalog mentions the part, grade it no higher than B unless revenue/order/customer evidence exists.
- If only market discussion links the company to the component, grade it C/D.
- Record missing component coverage as a gap, not as "no opportunity".

## Final Report Requirement

`008_final_report.md` should include a short section named one of:

- `上游零部件拆解`
- `Component Decomposition`
- `二级/三级零部件`
- `核心部件与材料`

This section should say whether the real bottleneck is at the system/OEM layer or further upstream.
