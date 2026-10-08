# Local MiniMax H3 reliability

Use this reference only for local MiniMax H3 work.

## Proven local constraint

The installed route uses a streamed BF16 MiniMax H3 model and BF16 Turbo LoRA. Its documented production example is a 1344×768, 5-second source clip. On this machine, attempting a 10-second source clip caused a Metal command-buffer out-of-memory failure. Therefore, the active production ceiling is **5 seconds per source clip** until a later, documented feasibility test proves otherwise.

Delivery resolution is separate from source resolution. A completed source clip may be cropped and upscaled to 1920×1080 at 24 fps only after it decodes and passes continuity review.

## Required preflight

Run this read-only command from the skill folder or project copy, substituting the project paths:

```bash
python3 scripts/minimax_local_preflight.py \
  --duration 5 --resolution 1344x768 --memory-limit-gb 24 \
  --model-root "/path/to/models/MiniMax-H3/FL2VA" \
  --turbo-lora "/path/to/minimax_h3_fl2v_turbo_4step_v1.0_768p_bf16.safetensors" \
  --runtime "/path/to/run_evo.py" \
  --start-frame "/path/to/approved-start-frame.png" \
  --output-dir "/path/to/unit/05-renders"
```

Proceed only on `"status": "PASS"`. The preflight checks duration, canvas alignment, model and reference paths, ffmpeg, disk, memory reserve, and competing MiniMax processes.

## Dispatch and failure rules

1. Use a one-shot job that captures stdout and stderr to the unit ledger. Do not use automatic process relaunch.
2. Record the model canvas separately from the delivery canvas.
3. If the first 5-second clip passes the moving review, extract and review its last frame before using it as the only carry-over reference for the next 5-second clip.
4. On `Insufficient Memory`, stop. Do not repeat the same duration and canvas. Reduce source duration or canvas, reduce streamed block residency, or select another tool route. Change only one variable per recovery attempt.
5. On a missing MP4 or muxing error, preserve the generated intermediate media and verify ffmpeg before retrying. Do not blame continuity assets for a runtime failure.
6. Decode the complete final MP4 and inspect 0%, 25%, 50%, 75%, and 100% before delivery.

## Repository intake gate

Before a reinstall, update, or newly imported repository:

1. Confirm the expected upstream remote and pin the exact commit or signed release.
2. Run `git fsck --full --no-reflogs`; stop if it reports corruption.
3. Inspect `pyproject.toml`, requirements, lock files, installer scripts, and commands that download, execute, or elevate privileges.
4. Scan for dynamic execution, shell interpolation, unpinned downloads, and unexpected write locations.
5. Run the project’s documented tests or doctor check in an isolated environment where practical.
6. Do not run a downloaded installer, `curl | sh`, or repository setup command until the intake record is approved.

This gate reduces risk but cannot prove a third-party repository is safe. Preserve the intake evidence with the project.
