#!/usr/bin/env python3
"""Report workspace registration and filesystem drift without rewriting files."""

from __future__ import annotations

import argparse
import json
import tomllib
from pathlib import Path


IGNORED = {".git", ".idea", ".vscode", "__pycache__", "node_modules"}


def load(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def inspect_root(path: Path, manifest_path: Path) -> dict:
    result = {"path": str(path), "manifest": str(manifest_path), "status": "pass", "findings": []}
    if not path.is_dir():
        result["status"] = "fail"; result["findings"].append("root missing"); return result
    if not manifest_path.is_file():
        result["status"] = "fail"; result["findings"].append("manifest missing"); return result
    try:
        manifest = load(manifest_path)
    except Exception as exc:
        result["status"] = "fail"; result["findings"].append(f"manifest parse failed: {exc}"); return result
    registered = set(manifest.get("structure", {}).get("children", []))
    physical = {item.name for item in path.iterdir() if item.is_dir() and item.name not in IGNORED}
    missing = sorted(registered - physical, key=str.lower)
    extra = sorted(physical - registered, key=str.lower)
    if missing:
        result["findings"].append("registered but missing: " + ", ".join(missing))
    if extra:
        result["findings"].append("physical but unregistered: " + ", ".join(extra))
    authorities = []
    for candidate in path.glob("*.manifest.toml"):
        try:
            data = load(candidate)
            if data.get("manifest", {}).get("manifest_type") in {"directory", "project"}:
                authorities.append(candidate.name)
        except Exception:
            pass
    if len(authorities) != 1:
        result["findings"].append("local entity authorities: " + (", ".join(authorities) or "none"))
    if result["findings"]:
        result["status"] = "drift"
    result["registered_children"] = len(registered)
    result["physical_children"] = len(physical)
    return result


def markdown(results: list[dict]) -> str:
    lines = ["# Workspace Inventory Report", "", "| Root | Status | Registered | Physical | Findings |", "| --- | --- | ---: | ---: | --- |"]
    for item in results:
        lines.append(
            f"| `{item['path']}` | {item['status']} | {item.get('registered_children', 0)} | "
            f"{item.get('physical_children', 0)} | {'; '.join(item['findings']) or 'None'} |"
        )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, default=Path("D:/"))
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()
    workspace = args.workspace_root.resolve()
    development = load(workspace / "Development.manifest.toml")
    results = [
        inspect_root(Path(root["path"]), Path(root["manifest"]))
        for root in development.get("roots", [])
        if root.get("kind") != "standards-registry"
    ]
    print(json.dumps(results, indent=2) if args.format == "json" else markdown(results))
    return 1 if any(item["status"] != "pass" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
