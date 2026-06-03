# Search Packet: 液冷二级零部件

## Run

- Run directory: `research_runs/2026-06-03-液冷二级零部件`
- Steps covered: `002_demand`, `003_supply`, `004_targets`
- Purpose: Validate why AI servers make liquid cooling a hard requirement, then identify which secondary components have slow delivery, strict customer qualification, or upstream bottleneck characteristics.

## Search Intent

1. Confirm the technical demand shift from air cooling to liquid cooling for Blackwell-era AI infrastructure.
2. Separate market-known "liquid cooling leaders" from harder-to-deliver second-tier and upstream components.
3. Build an evidence-backed candidate map for pipes, connectors, cold plates, pumps, manifolds, CDU subassemblies, fluorinated materials, and precision manufacturing links.

## Query List

- `NVIDIA Blackwell liquid cooling AI infrastructure efficiency`
- `GB200 NVL72 liquid cooling OCP direct liquid cooling`
- `direct liquid cooling cold plate GPU hotspot design academic paper`
- `AI data center liquid cooling cold plate manifold connector pump supply chain`
- `川环科技 液冷服务器 管路 年报 UL`
- `中航光电 液冷连接器 液冷源 数据中心 年报`
- `大元泵业 液冷泵 数据中心 年报`
- `华丰科技 电光液 微型液冷 服务器`

## Source Priority

1. Official sources, company announcements, regulatory filings, and exchange disclosures.
2. Annual reports, investor-relations material, earnings calls, and customer certification evidence.
3. Standards bodies, OCP material, and academic thermal-design papers.
4. Reputable industry media and supply-chain reporting.
5. Sell-side notes, social media, and market discussion only as sentiment context.

## Accepted Sources

- NVIDIA official material on Blackwell and liquid-cooled AI infrastructure.
- OCP and direct-liquid-cooling technical material where it clarifies rack, manifold, cold-plate, or coolant-loop constraints.
- Academic papers on GPU/CPU hotspot control and cold-plate design sensitivity.
- Company filings and announcements for 川环科技, 中航光电, 华丰科技, 大元泵业, and related A-share candidates.
- Existing `sources/source_index.md` entries used as the run-level source ledger.

## Rejected Or Downgraded Sources

- Pure concept-stock lists with no link to company filings or product revenue.
- Order rumors without customer, shipment, or filing support.
- Social-media popularity claims unless used only for "hot consensus" context.
- Reposted sell-side tables that did not expose primary-source assumptions.

## Coverage Gaps

- Overseas liquid-cooling comparables were not normalized into the same structured market-data table as A-share candidates.
- Revenue share by liquid-cooling product line remains uneven across candidates.
- Customer qualification status is often indirect; some conclusions rely on product certification, product catalog, or management commentary rather than named customer orders.
- Upstream material and machining bottlenecks need a second pass before being treated as confirmed investment clues.

## Impact On Next Steps

- Treat 川环科技 and 中航光电 as higher-evidence A-share candidates only where the report cites primary or semi-primary evidence.
- Keep 华丰科技, 大元泵业, and upstream material/process names in the radar layer unless revenue visibility improves.
- Require `006_pricing` to distinguish structured A-share market data from overseas or unstructured market context.
- Carry overseas structured coverage as an explicit gap rather than pretending the historical run has full cross-market parity.
