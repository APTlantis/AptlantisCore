#!/usr/bin/env python3
"""Create PPS proposal and entity-manifest skeletons from templates."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROPOSAL_TEMPLATE = ROOT / "templates" / "Project-Proposal.md"
MANIFEST_TEMPLATE = ROOT / "templates" / "PROJECT.manifest.toml"


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip()).strip("-").lower()
    return slug or "project"


def render_proposal(project_name: str, project_type: str, delivery_standard: str, readiness: str) -> str:
    text = PROPOSAL_TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("[Project Name]", project_name)
    text = text.replace("[Desktop application, CLI tool, website, dataset, standard, service, library, dashboard]", project_type)
    text = text.replace("[sketch / draft / ready / rework]", readiness)
    text = text.replace("- Proposal:", "- Proposal: PPS")
    text = text.replace("- Workspace:", "- Workspace: WGS")
    text = text.replace("- Delivery:", f"- Delivery: {delivery_standard}")
    return text


def render_manifest(project_name: str, project_type: str, delivery_standard: str) -> str:
    project_id = slugify(project_name)
    text = MANIFEST_TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        'id = "example-project"': f'id = "{project_id}"',
        'title = "Example Project"': f'title = "{project_name}"',
        'class = "unknown"': f'class = "{project_type}"',
        'delivery_standard = ""': f'delivery_standard = "{delivery_standard}"',
        "ProjectName.manifest.toml": f"{project_name}.manifest.toml",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_name", help="Human-readable project name.")
    parser.add_argument("--type", default="unknown", help="Project type or class.")
    parser.add_argument("--delivery-standard", default="", help="Likely delivery standard, such as CTS, DRS, WDS, DDS, SIS, or SFDS.")
    parser.add_argument("--readiness", default="sketch", choices=["sketch", "draft", "ready", "rework"])
    parser.add_argument("--output-dir", type=Path, default=Path.cwd())
    parser.add_argument("--force", action="store_true", help="Overwrite existing skeleton files.")
    args = parser.parse_args()

    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    proposal_path = output / "Project-Proposal.md"
    manifest_path = output / f"{args.project_name}.manifest.toml"
    for path in [proposal_path, manifest_path]:
        if path.exists() and not args.force:
            raise SystemExit(f"Refusing to overwrite existing file: {path}")

    proposal_path.write_text(
        render_proposal(args.project_name, args.type, args.delivery_standard, args.readiness),
        encoding="utf-8",
    )
    manifest_path.write_text(
        render_manifest(args.project_name, args.type, args.delivery_standard),
        encoding="utf-8",
    )
    print(f"Created {proposal_path}")
    print(f"Created {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
