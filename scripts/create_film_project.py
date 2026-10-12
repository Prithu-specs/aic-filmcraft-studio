#!/usr/bin/env python3
"""Create a provider-neutral Filmcraft project with a stable scene folder tree."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("Project name must contain at least one ASCII letter or digit.")
    return slug


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def create_project(name: str, root: Path, scene_count: int, provider: str) -> Path:
    if not 1 <= scene_count <= 100:
        raise ValueError("Scene count must be between 1 and 100.")
    project_slug = slugify(name)
    provider_slug = slugify(provider)
    root = root.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    project = root / project_slug
    if project.exists():
        raise FileExistsError(f"Refusing to overwrite existing project: {project}")

    project.mkdir()
    try:
        scenes = [f"scene-{i:02d}-unassigned" for i in range(1, scene_count + 1)]
        dirs = [
            "00-admin", "01-story", "02-canon/characters", "02-canon/props",
            "02-canon/locations", "02-canon/color-lighting", "02-canon/sound",
            "03-storyboards", "04-platform", "05-production", "06-edit",
            "06-edit/assembly", "07-delivery", "08-archive",
        ]
        for relative in dirs:
            (project / relative).mkdir(parents=True, exist_ok=True)

        for scene_id in scenes:
            scene_dirs = [
                f"03-storyboards/{scene_id}/frames",
                f"03-storyboards/{scene_id}/review",
                f"05-production/{scene_id}/01-authority",
                f"05-production/{scene_id}/02-assets",
                f"05-production/{scene_id}/03-prompt",
                f"05-production/{scene_id}/04-upload-proof",
                f"05-production/{scene_id}/05-renders",
                f"05-production/{scene_id}/06-audio",
                f"05-production/{scene_id}/07-ledger",
            ]
            for relative in scene_dirs:
                (project / relative).mkdir(parents=True, exist_ok=True)
            scene_root = project / "05-production" / scene_id
            (scene_root / "01-authority" / "scene-card.md").write_text(
                f"# {scene_id}\n\nStatus: planned\n\nProducer approval: pending\n\nApproved scene beat: pending\n\nExact approved references: pending\n\nAcceptance checks: pending\n",
                encoding="utf-8",
            )
            write_json(scene_root / "02-assets" / "asset-manifest.json", {
                "scene_id": scene_id,
                "status": "planned",
                "assets": [],
                "note": "Only Codex-created, Producer-approved images may be imported into a video provider.",
            })
            with (scene_root / "07-ledger" / "attempt-ledger.csv").open("w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([
                    "attempt_id", "provider", "model", "resolution", "aspect_ratio",
                    "duration_seconds", "asset_ids", "exact_cost_credits", "quote_timestamp_utc",
                    "producer_go", "job_id", "status", "output_path", "review_0_25_50_75_100",
                    "decision", "next_action",
                ])

        write_json(project / "00-admin" / "project-manifest.json", {
            "project_id": project_slug,
            "display_name": name,
            "provider_adapter": provider_slug,
            "scene_count": scene_count,
            "scene_ids": scenes,
            "approval_owner": "Producer",
            "image_source_policy": "Codex only; no video-provider image generation",
            "status": "planning",
        })
        with (project / "00-admin" / "approvals.csv").open("w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["record_id", "scope", "version", "decision", "producer", "timestamp_utc", "evidence_path", "notes"])
        with (project / "00-admin" / "credit-ledger.csv").open("w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["attempt_id", "scope", "provider", "model", "quote_credits", "actual_credits", "producer_go", "timestamp_utc", "output_path", "status"])
        write_json(project / "04-platform" / "platform-map.json", {
            "canonical_project_id": project_slug,
            "provider": provider_slug,
            "provider_project_id": None,
            "scenes": {scene_id: {"provider_folder_id": None, "assets": []} for scene_id in scenes},
        })
        (project / "01-story" / "script.md").write_text(
            "# Approved script\n\nStatus: pending Producer approval.\n\n", encoding="utf-8"
        )
        (project / "06-edit" / "assembly" / "assembly-order.txt").write_text(
            "# Add approved scene IDs in final script order after all scene clips pass review.\n",
            encoding="utf-8",
        )
        (project / "README.md").write_text(
            f"# {name}\n\nCreated with the AIC Filmcraft provider-neutral scaffold.\n"
            f"Provider adapter: `{provider_slug}`. Scenes: {scene_count}.\n\n"
            "All stills are created in Codex, shown to the Producer, and approved before import. "
            "The video platform stores/copies approved assets and generates scene videos only after "
            "per-attempt cost approval. See `00-admin/project-manifest.json`.\n",
            encoding="utf-8",
        )
    except Exception:
        # Do not leave a half-created tree that could look like a valid project.
        import shutil
        shutil.rmtree(project, ignore_errors=True)
        raise
    return project


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Human-readable project name")
    parser.add_argument("--scene-count", type=int, required=True, help="Approved scene count from the locked story")
    parser.add_argument("--provider", default="higgsfield", help="Provider adapter ID (default: higgsfield)")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Parent directory for the new project")
    args = parser.parse_args(argv)
    try:
        path = create_project(args.name, args.root, args.scene_count, args.provider)
    except (ValueError, FileExistsError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
