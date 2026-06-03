#!/usr/bin/env python3
"""Generate an agent capability report for this research harness.

The script only records whether credentials/capabilities are present. It never
prints or writes secret values.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def run_cmd(args: list[str], timeout: int = 20) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            args,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
        return {
            "ok": completed.returncode == 0,
            "returncode": completed.returncode,
            "stdout": completed.stdout.strip()[:500],
            "stderr": completed.stderr.strip()[:500],
        }
    except Exception as exc:  # pragma: no cover - defensive CLI guard
        return {"ok": False, "returncode": None, "stdout": "", "stderr": str(exc)[:500]}


def status_from_bool(value: bool) -> str:
    return "available" if value else "missing"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Create a capability report for a research run.")
    parser.add_argument("--run-dir", help="Research run directory. Writes state/capability_report.json when set.")
    parser.add_argument("--output", help="Explicit output path. Overrides --run-dir default.")
    parser.add_argument("--agent-name", default="unknown")
    parser.add_argument("--web-search", choices=["yes", "no", "unknown"], default="unknown")
    parser.add_argument("--browser", choices=["yes", "no", "unknown"], default="unknown")
    parser.add_argument(
        "--skip-yahoo-smoke",
        action="store_true",
        help="Only check that uv and tools/yf exist; do not run tools/yf --help.",
    )
    args = parser.parse_args(argv)

    project_root = Path.cwd()
    run_dir = Path(args.run_dir) if args.run_dir else None
    if run_dir and not run_dir.exists():
        print(f"ERROR: run directory not found: {run_dir}")
        return 2

    output_path = Path(args.output) if args.output else None
    if output_path is None:
        output_path = (run_dir / "state" / "capability_report.json") if run_dir else Path("capability_report.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    python_info = {
        "available": True,
        "executable": sys.executable,
        "version": sys.version.split()[0],
    }

    tushare_available = importlib.util.find_spec("tushare") is not None
    token_present = bool(os.environ.get("TUSHARE_TOKEN"))
    tushare_status = "available" if tushare_available and token_present else "missing-with-fallback"
    if not tushare_available:
        tushare_status = "missing"

    uv_path = shutil.which("uv")
    uv_available = uv_path is not None
    uv_version = run_cmd([uv_path, "--version"]) if uv_available else {"ok": False, "stdout": "", "stderr": "uv not found"}
    yf_path = project_root / "tools" / "yf"
    yf_exists = yf_path.exists()
    yf_smoke = {"ok": False, "stdout": "", "stderr": "skipped"}
    if uv_available and yf_exists and not args.skip_yahoo_smoke:
        yf_smoke = run_cmd([uv_path, "run", "--script", str(yf_path), "--help"], timeout=60)
    yahoo_status = "available" if uv_available and yf_exists and (args.skip_yahoo_smoke or yf_smoke["ok"]) else "missing-with-fallback"

    git_path = shutil.which("git")
    git_result = run_cmd([git_path, "--version"]) if git_path else {"ok": False, "stdout": "", "stderr": "git not found"}

    limitations: list[str] = []
    if args.web_search != "yes":
        limitations.append("web_search_not_confirmed: do not independently run 002-005 without a source pack")
    if args.browser != "yes":
        limitations.append("browser_not_confirmed: source/PDF verification may be limited")
    if not token_present:
        limitations.append("tushare_token_missing: A-share structured data may be unavailable")
    if yahoo_status != "available":
        limitations.append("yahoo_cli_unavailable: overseas market data requires fallback")

    report = {
        "agent_name": args.agent_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "project_root": str(project_root),
        "python": python_info,
        "tushare": {
            "package_available": tushare_available,
            "token_present": token_present,
            "status": tushare_status,
        },
        "yahoo_cli": {
            "uv_available": uv_available,
            "uv_path": uv_path or "",
            "uv_version": uv_version.get("stdout", ""),
            "tools_yf_exists": yf_exists,
            "help_smoke_ok": bool(yf_smoke["ok"]) if not args.skip_yahoo_smoke else None,
            "status": yahoo_status,
            "error": "" if yf_smoke["ok"] or args.skip_yahoo_smoke else yf_smoke.get("stderr", ""),
        },
        "web_search": {
            "declared": args.web_search,
            "notes": "Manual declaration; local script cannot detect agent-native search.",
        },
        "browser": {
            "declared": args.browser,
            "notes": "Manual declaration; local script cannot detect agent-native browser tools.",
        },
        "git": {
            "available": bool(git_result["ok"]),
            "version": git_result.get("stdout", ""),
        },
        "file_write": {
            "available": True,
            "notes": "This report was written successfully.",
        },
        "limitations": limitations,
    }

    output_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"capability_report={output_path}")
    print(f"python=available {python_info['version']}")
    print(f"tushare={tushare_status} token_present={token_present}")
    print(f"yahoo_cli={yahoo_status}")
    print(f"web_search={args.web_search}")
    print(f"browser={args.browser}")
    print(f"git={status_from_bool(bool(git_result['ok']))}")
    if limitations:
        print("limitations=" + "; ".join(limitations))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
