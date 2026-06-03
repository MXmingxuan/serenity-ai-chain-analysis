#!/usr/bin/env python3
"""Validate a prompt-chain research run.

This script checks mechanical quality gates only. It does not judge the
investment conclusion.
"""

from __future__ import annotations

import csv
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
            warnings.append("004_targets.md appears to have weak cross-market coverage")

    final_path = reports_dir / "008_final_report.md"
    if final_path.exists():
        final_text = read_text(final_path)
        if "全球" not in final_text and "海外" not in final_text and "对标" not in final_text:
            warnings.append("008_final_report.md may be missing global comparison constraints")

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
