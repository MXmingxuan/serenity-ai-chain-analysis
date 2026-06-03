#!/usr/bin/env python3
"""Validate a prompt-chain research run.

This script checks mechanical quality gates only. It does not judge the
investment conclusion.
"""

from __future__ import annotations

import csv
import json
import os
import sys
from pathlib import Path


EXPECTED_REPORTS = [
    "000_scope.md",
    "001_value_chain.md",
    "002_demand.md",
    "003_supply.md",
    "004_targets.md",
    "005_evidence_audit.md",
    "006_pricing.md",
    "007_disconfirmation.md",
    "008_final_report.md",
]

URL_MARKERS = ("http://", "https://", "file:", ".md", ".pdf", ".csv")

COMPONENT_THEME_TRIGGERS = (
    "equipment",
    "machine",
    "machinery",
    "generator",
    "gas turbine",
    "turbine",
    "engine",
    "power system",
    "liquid cooling",
    "cooling",
    "optical module",
    "packaging",
    "server",
    "material",
    "process",
    "设备",
    "主机",
    "系统",
    "发电机",
    "燃气",
    "燃机",
    "轮机",
    "发动机",
    "液冷",
    "光模块",
    "封装",
    "材料",
    "工艺",
    "零部件",
    "部件",
)

COMPONENT_SECTION_MARKERS = (
    "component decomposition",
    "upstream component",
    "second-level",
    "third-level",
    "hot gas path",
    "上游零部件",
    "二级零部件",
    "三级零部件",
    "核心部件",
    "关键材料",
    "热端部件",
    "制造工艺",
)

MARKET_ALIASES = {
    "US": {"US", "USA", "美股", "NYSE", "NASDAQ"},
    "HK": {"HK", "HKG", "港股"},
    "CN_A": {"CN_A", "A股", "A 股", "SH", "SZ", "SSE", "SZSE"},
    "OTHER": {"OTHER", "其他", "TW", "JP", "EU", "LSE", "TSE"},
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def parse_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def normalize_market(raw: str) -> str:
    value = (raw or "").strip()
    upper = value.upper()
    for canonical, aliases in MARKET_ALIASES.items():
        if value in aliases or upper in aliases:
            return canonical
    if upper.endswith(".HK"):
        return "HK"
    if upper.endswith(".SH") or upper.endswith(".SZ"):
        return "CN_A"
    if upper:
        return upper
    return ""


def is_component_heavy_theme(run_dir: Path, reports_dir: Path) -> bool:
    texts: list[str] = [run_dir.name]
    for path in [
        run_dir / "state" / "research_state.yaml",
        reports_dir / "000_scope.md",
        reports_dir / "001_value_chain.md",
        reports_dir / "003_supply.md",
    ]:
        if path.exists():
            texts.append(read_text(path))
    combined = "\n".join(texts).lower()
    return any(trigger.lower() in combined for trigger in COMPONENT_THEME_TRIGGERS)


def has_component_decomposition(run_dir: Path, reports_dir: Path) -> bool:
    component_report = reports_dir / "003_component_decomposition.md"
    if component_report.exists():
        return True
    candidate_paths = [
        reports_dir / "003_supply.md",
        reports_dir / "004_targets.md",
        reports_dir / "008_final_report.md",
        run_dir / "sources" / "search_packet.md",
    ]
    text = "\n".join(read_text(path) for path in candidate_paths if path.exists()).lower()
    return any(marker.lower() in text for marker in COMPONENT_SECTION_MARKERS)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/validate_run.py <research_run_dir>")
        return 2

    run_dir = Path(argv[1])
    errors: list[str] = []
    warnings: list[str] = []

    if not run_dir.exists():
        print(f"ERROR: run directory not found: {run_dir}")
        return 2

    reports_dir = run_dir / "reports"
    for name in EXPECTED_REPORTS:
        if not (reports_dir / name).exists():
            errors.append(f"missing report: reports/{name}")

    card = run_dir / "cards" / "009_research_card.md"
    if not card.exists():
        errors.append("missing card: cards/009_research_card.md")

    source_index = run_dir / "sources" / "source_index.md"
    if not source_index.exists():
        warnings.append("missing source index: sources/source_index.md")
    else:
        source_text = read_text(source_index)
        if not any(marker in source_text for marker in URL_MARKERS):
            warnings.append("source_index.md may not contain traceable URLs or file paths")

    trace_path = run_dir / "state" / "run_trace.jsonl"
    if not trace_path.exists():
        warnings.append("missing execution trace: state/run_trace.jsonl")
    else:
        for line_no, line in enumerate(read_text(trace_path).splitlines(), 1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
            except Exception as exc:
                errors.append(f"run_trace.jsonl parse failed at line {line_no}: {exc}")
                continue
            required_trace_fields = {
                "timestamp",
                "step",
                "agent",
                "action_type",
                "tool_or_source",
                "input_summary",
                "output_summary",
                "status",
                "error",
                "artifacts_changed",
            }
            missing = sorted(required_trace_fields - set(event))
            if missing:
                errors.append(f"run_trace.jsonl line {line_no} missing fields: {', '.join(missing)}")

    csv_paths = [
        run_dir / "state" / "evidence_ledger.csv",
        run_dir / "market_data" / "symbol_universe.csv",
        run_dir / "market_data" / "price_snapshot.csv",
        run_dir / "market_data" / "valuation_snapshot.csv",
        run_dir / "market_data" / "liquidity_snapshot.csv",
    ]
    csv_rows: dict[Path, list[dict[str, str]]] = {}
    for path in csv_paths:
        if not path.exists():
            warnings.append(f"missing csv: {path.relative_to(run_dir)}")
            continue
        try:
            rows = parse_csv(path)
            csv_rows[path] = rows
        except Exception as exc:  # pragma: no cover - defensive CLI guard
            errors.append(f"csv parse failed: {path.relative_to(run_dir)}: {exc}")

    universe_path = run_dir / "market_data" / "symbol_universe.csv"
    universe_rows = csv_rows.get(universe_path, [])
    if universe_rows:
        fields = set(universe_rows[0].keys())
        required_fields = {
            "symbol",
            "market",
            "name",
            "coverage_required",
            "coverage_status",
            "gap_reason",
        }
        missing_fields = sorted(required_fields - fields)
        if missing_fields:
            warnings.append(
                "symbol_universe.csv uses legacy schema; missing fields: "
                + ", ".join(missing_fields)
            )

        markets = {
            normalize_market(row.get("market", "") or row.get("symbol", ""))
            for row in universe_rows
        }
        markets.discard("")
        if len(markets) < 2:
            notes_path = run_dir / "market_data" / "market_data_notes.md"
            notes = read_text(notes_path).lower() if notes_path.exists() else ""
            has_gap_reason = any(
                token in notes
                for token in ["缺失数据", "未覆盖", "gap", "missing", "无直接标的"]
            )
            if has_gap_reason:
                warnings.append(
                    "symbol_universe.csv covers fewer than two markets, but notes contain a gap section"
                )
            else:
                errors.append(
                    "symbol_universe.csv covers fewer than two markets and no market gap reason was found"
                )

        required_symbols = {
            row.get("symbol", "").strip()
            for row in universe_rows
            if (row.get("coverage_required", "").strip().lower() in {"yes", "y", "true", "1"})
        }
        if required_symbols:
            price_rows = csv_rows.get(run_dir / "market_data" / "price_snapshot.csv", [])
            priced_symbols = {row.get("symbol", "").strip() for row in price_rows}
            missing = sorted(required_symbols - priced_symbols)
            if missing:
                notes_path = run_dir / "market_data" / "market_data_notes.md"
                notes = read_text(notes_path) if notes_path.exists() else ""
                not_explained = [symbol for symbol in missing if symbol not in notes]
                if not_explained:
                    errors.append(
                        "coverage_required symbols missing price data without notes: "
                        + ", ".join(not_explained)
                    )

    targets_path = reports_dir / "004_targets.md"
    if targets_path.exists():
        targets = read_text(targets_path)
        market_mentions = sum(
            1
            for token in ["美股", "港股", "A 股", "A股", "其他市场", "US", "HK", "CN_A"]
            if token in targets
        )
        if market_mentions < 2:
            gap_markers = ["未覆盖", "缺口", "gap", "missing", "无直接标的", "暂未发现", "数据不可得"]
            if any(marker in targets.lower() for marker in gap_markers):
                warnings.append("004_targets.md appears cross-market limited, but contains a gap explanation")
            else:
                warnings.append("004_targets.md appears to have weak cross-market coverage")

    if is_component_heavy_theme(run_dir, reports_dir) and not has_component_decomposition(run_dir, reports_dir):
        warnings.append(
            "component-heavy theme may be missing component decomposition: "
            "add reports/003_component_decomposition.md or a component decomposition section"
        )

    pricing_path = reports_dir / "006_pricing.md"
    if pricing_path.exists():
        pricing = read_text(pricing_path)
        market_data_markers = [
            "price_snapshot.csv",
            "valuation_snapshot.csv",
            "liquidity_snapshot.csv",
            "market_data",
            "Tushare",
            "Yahoo",
        ]
        if not any(marker in pricing for marker in market_data_markers):
            warnings.append("006_pricing.md may not reference structured market data")

    final_path = reports_dir / "008_final_report.md"
    if final_path.exists():
        final_text = read_text(final_path)
        if "全球" not in final_text and "海外" not in final_text and "对标" not in final_text:
            warnings.append("008_final_report.md may be missing global comparison constraints")

    html_dir = run_dir / "html"
    if html_dir.exists():
        html_report = html_dir / "008_final_report.html"
        if not html_report.exists():
            errors.append("html directory exists but html/008_final_report.html is missing")
        else:
            html_text = read_text(html_report)
            if "../reports/008_final_report.md" not in html_text:
                warnings.append("html report does not link back to Markdown source")
            if "../sources/source_index.md" not in html_text:
                warnings.append("html report does not link to source index")
            if "<!doctype html>" not in html_text[:80].lower():
                warnings.append("html report is missing a doctype")

    token = os.environ.get("TUSHARE_TOKEN", "")
    token_prefix = token[:8] if token else ""
    secret_hits: list[str] = []
    for path in run_dir.rglob("*"):
        if not path.is_file():
            continue
        text = read_text(path)
        if (token and token in text) or (token_prefix and token_prefix in text):
            secret_hits.append(str(path.relative_to(run_dir)))
    if secret_hits:
        errors.append("possible token leakage: " + ", ".join(secret_hits))

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASSED: 0 error(s), {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
