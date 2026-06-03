# HTML Report Output Guidelines

Every completed research run should keep the Markdown report and may add a static HTML page under:

```text
research_runs/YYYY-MM-DD-topic/html/008_final_report.html
```

## Required Content

- Link back to `../reports/008_final_report.md`.
- Link to `../sources/source_index.md` when a source index exists.
- Preserve the final research conclusion, evidence boundaries, and disconfirmation list.
- Include a clear note that the output is a research radar, not investment advice.
- If market data is used, include the data date, provider, and coverage gaps.

## Visual Guidance

- Use a theme that matches the research object and audience.
- Avoid generic AI gradients, blue-purple glow palettes, decorative orbs, and marketing-site hero layouts.
- For dense public-equity research, a Bloomberg-terminal-inspired theme is acceptable:
  - near-black background;
  - amber, green, red, and white status colors;
  - dense tables, small caps labels, thin grid lines;
  - compact KPI strips and clear risk flags.

## Technical Guidance

- Prefer a self-contained static HTML file with inline CSS for portability.
- Keep Markdown files as source-of-truth artifacts.
- Do not embed secrets, tokens, private environment paths, or raw API credentials.
- Tables and charts should use source-backed data from `market_data/` where possible.
