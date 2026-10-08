#!/usr/bin/env python3
"""Read-only feasibility gate for local MiniMax H3 jobs.

It intentionally does not start, stop, reinstall, download, or modify MiniMax.
Use it before every local render; a non-zero status means do not dispatch.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


SAFE_BF16_MAX_SECONDS = 5
MIN_FREE_DISK_GIB = 100


def run(*args: str) -> str:
    try:
        return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT).strip()
    except (OSError, subprocess.CalledProcessError):
        return ""


def gib(bytes_value: int) -> float:
    return round(bytes_value / 1024**3, 1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--duration", type=float, required=True)
    parser.add_argument("--resolution", required=True, help="model canvas, WIDTHxHEIGHT")
    parser.add_argument("--memory-limit-gb", type=float, default=24)
    parser.add_argument("--model-root", type=Path, required=True)
    parser.add_argument("--turbo-lora", type=Path, required=True)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--start-frame", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--ffmpeg", type=Path, default=Path(shutil.which("ffmpeg") or ""))
    args = parser.parse_args()

    checks: list[dict[str, object]] = []

    def check(name: str, ok: bool, detail: str, severity: str = "block") -> None:
        checks.append({"name": name, "ok": ok, "severity": severity, "detail": detail})

    try:
        width, height = (int(value) for value in args.resolution.lower().split("x", 1))
        valid_canvas = width > 0 and height > 0 and width % 32 == 0 and height % 32 == 0
        check("model_canvas", valid_canvas, "Canvas must be positive and both dimensions must be divisible by 32.")
    except ValueError:
        check("model_canvas", False, "Resolution must be formatted WIDTHxHEIGHT.")

    check("duration", args.duration > 0, "Duration must be positive.")
    check(
        "bf16_chunk_limit",
        args.duration <= SAFE_BF16_MAX_SECONDS,
        f"This local BF16 MiniMax route is limited to {SAFE_BF16_MAX_SECONDS:g}-second source clips. Split longer scenes into locked segments and carry an approved end frame into the next segment.",
    )
    check("model_root", (args.model_root / "transformer").is_dir(), "Expected MiniMax FL2VA transformer directory is missing." if not (args.model_root / "transformer").is_dir() else "Transformer directory found.")
    check("turbo_lora", args.turbo_lora.is_file(), "Turbo LoRA file is missing." if not args.turbo_lora.is_file() else "Turbo LoRA file found.")
    check("runtime", args.runtime.is_file(), "Reference-enabled runtime wrapper is missing." if not args.runtime.is_file() else "Runtime wrapper found.")
    check("start_frame", args.start_frame.is_file(), "Approved start-frame lock is missing." if not args.start_frame.is_file() else "Start-frame lock found.")
    check(
        "ffmpeg",
        args.ffmpeg.is_file() and os.access(args.ffmpeg, os.X_OK),
        f"ffmpeg must be an executable absolute path for the sanitized launch environment: {args.ffmpeg}",
    )

    output_parent = args.output_dir.parent if args.output_dir.suffix else args.output_dir
    free_gib = gib(shutil.disk_usage(output_parent).free) if output_parent.exists() else 0
    check("free_disk", free_gib >= MIN_FREE_DISK_GIB, f"{free_gib:g} GiB free; require at least {MIN_FREE_DISK_GIB} GiB.")

    memory_bytes = run("sysctl", "-n", "hw.memsize")
    total_gib = gib(int(memory_bytes)) if memory_bytes.isdigit() else 0
    check("memory_limit", 0 < args.memory_limit_gb <= max(total_gib - 8, 0), f"Requested {args.memory_limit_gb:g} GiB; machine total is {total_gib:g} GiB and an 8 GiB system reserve is required.")

    active = run("ps", "-axo", "pid=,command=")
    excluded_pids = {os.getpid(), os.getppid()}
    active_minimax = []
    for line in active.splitlines():
        parts = line.strip().split(maxsplit=1)
        if len(parts) != 2 or not parts[0].isdigit() or int(parts[0]) in excluded_pids:
            continue
        command = parts[1]
        if "run_evo.py" in command or "minimax-h3-generate" in command:
            active_minimax.append(command)
    check("no_competing_render", not active_minimax, "No competing MiniMax process found." if not active_minimax else "A MiniMax process is already active; do not run concurrent local renders.")

    failures = [item for item in checks if not item["ok"] and item["severity"] == "block"]
    result = {
        "status": "PASS" if not failures else "BLOCKED",
        "safe_bf16_max_seconds": SAFE_BF16_MAX_SECONDS,
        "checks": checks,
        "required_launch_policy": "one-shot job only; automatic relaunch is forbidden",
        "required_runtime_media_policy": "pass the preflight-verified absolute --ffmpeg path; never rely on launchd PATH",
        "required_review_policy": "decode output, inspect 0/25/50/75/100 percent, then approve carry-over frame",
    }
    print(json.dumps(result, indent=2))
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
