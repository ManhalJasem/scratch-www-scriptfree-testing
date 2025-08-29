#!/usr/bin/env python3
import sys
import os
from pathlib import Path
from datetime import datetime

# Defaults (override with CLI args)
RUNNER_PATH = Path("test_script/scratch_exp/navbar_runner.py")
PKG_DIR = Path("test_script/scratch_exp")
FUNC_NAME = "search_bar_test"  # change if your entry function differs

def newest_module(pkg_dir: Path) -> str:
    if not pkg_dir.is_dir():
        raise FileNotFoundError(f"Package directory not found: {pkg_dir}")

    candidates = [p for p in pkg_dir.glob("test_script_*.py") if p.name != "__init__.py"]
    if not candidates:
        raise FileNotFoundError(f"No generated modules like test_script_*.py found in {pkg_dir}")

    # Prefer by mtime; if a timestamp is embedded in the filename, this still works well.
    newest = max(candidates, key=lambda p: p.stat().st_mtime)
    return newest.stem  # module name without .py


def main():
    # Optional CLI: point_runner_to_latest.py [runner.py] [test_script/scratch_exp] [FuncName]
    global RUNNER_PATH, PKG_DIR, FUNC_NAME
    if len(sys.argv) >= 2:
        RUNNER_PATH = Path(sys.argv[1])
    if len(sys.argv) >= 3:
        PKG_DIR = Path(sys.argv[2])
    if len(sys.argv) >= 4:
        FUNC_NAME = sys.argv[3]

    if not RUNNER_PATH.is_file():
        print(f"ERROR: runner.py not found at {RUNNER_PATH}", file=sys.stderr)
        sys.exit(2)

    module_name = newest_module(PKG_DIR)

    new_import = f"from test_script.scratch_exp.{module_name} import {FUNC_NAME}\n"

    # Read runner, replace only the first line.
    with RUNNER_PATH.open("r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        print("ERROR: runner.py is empty.", file=sys.stderr)
        sys.exit(2)


    # Replace line 1 (index 0)
    lines[0] = new_import

    with RUNNER_PATH.open("w", encoding="utf-8", newline="") as f:
        f.writelines(lines)

    print(f"Updated first line in {RUNNER_PATH} to:\n{new_import.strip()}")

if __name__ == "__main__":
    main()
