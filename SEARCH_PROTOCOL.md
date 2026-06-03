# Search Protocol

Search is a controlled research operation, not an informal browsing habit. Every search-heavy step must leave an audit trail.

## Applies To

Search packets are required for:

- `002_demand`
- `003_supply`
- `003_component_decomposition` when the theme is equipment/system/material/process-heavy
- `004_targets`
- `005_evidence_audit` when new sources are added
- `006_pricing` when sell-side coverage, social heat, or consensus narrative is searched

## Source Priority

Use the strongest available sources first:

1. Official platform or customer sources, company announcements, exchange filings, regulator disclosures.
2. Annual reports, interim reports, earnings call transcripts, investor presentations, IR records.
3. Authoritative industry bodies, standards organizations, academic papers, government or agency data.
4. Reputable industry and financial media.
5. Sell-side research, social media, forum posts, and rumor-like sources.

Do not use lower-priority sources to overwrite higher-priority sources. Lower-priority sources can generate leads, but those leads need verification.

## Search Packet

For each search-heavy step, create or update a `search_packet.md` using `templates/search_packet.md`.

Required fields:

- search intent;
- query list;
- accepted sources;
- rejected sources;
- coverage gaps;
- effect on evidence ledger or next step.

## Component Search Expansion

For equipment-heavy themes, search queries must include component, material, process, and service terms, not only the headline theme and OEM names.

Examples:

- `gas turbine blades vanes combustor liners superalloy suppliers`
- `燃气轮机 叶片 热端部件 高温合金 上市公司`
- `direct liquid cooling manifold quick connector pump valve seal supplier`
- `HBM advanced packaging substrate bonding equipment material supplier`

If component-level search is skipped, record it as a coverage gap in the search packet.

## Evidence Handling

- Every important accepted source must be added to `sources/source_index.md` or `state/evidence_ledger.csv`.
- Rejected sources should be summarized briefly when they explain why a claim was not used.
- Missing evidence is a finding, not a failure. Record it as a coverage gap.
- Avoid copying long passages. Use short quotes only when necessary and prefer paraphrased evidence summaries.
