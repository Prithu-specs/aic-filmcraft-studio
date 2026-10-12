# Higgsfield adapter

This adapter implements the provider-neutral contract in `../workflow/PROVIDER-ADAPTER-CONTRACT.md`. Its job is to transfer and reference approved Codex assets, then generate scene videos—never to create film stills in Higgsfield.

## Required project operation

1. Create one Higgsfield project for the film.
2. Create a Higgsfield folder named exactly for each canonical scene ID, such as `scene-01-handoff`. Keep one local scene directory per scene as well.
3. Upload the approved Codex storyboard/start-frame and only the additional approved character, location, and prop references required for that scene.
4. Ask Higgsfield to copy/register the imported images into the project asset/reference library for reuse. Verify and record each copy's asset/media ID and that it can be selected as a video reference.
5. Generate one approved scene/shot at a time from the exact approved reference images. Never call an image-generation endpoint or invoke an image-generation model for production assets.
6. Export each finished clip into the matching local scene folder. Review it before proceeding. After all required scenes are approved, join them in the approved story order and verify the complete movie.

## Per-scene ledger fields

Record at minimum:

- canonical `scene_id`, title, and local folder;
- Higgsfield project/folder IDs and URLs;
- source Codex asset IDs, filenames, versions, and producer approvals;
- imported media IDs, copy/register IDs, confirmation that each is available as a video reference;
- exact selected video model/settings and quote timestamp/cost;
- Producer GO text/time for that exact attempt;
- generation job ID, status, output ID, export path, and media probe;
- 0/25/50/75/100% review, audio review, defects, decision, and next action.

## Capability and failure rules

Provider features can change. Before each production, check the current Higgsfield interface/MCP for project creation, folders, asset import, copy/register, reference roles, cost preflight, video generation, and export. Do not infer a feature from an old run or this document.

- If native project or scene-folder creation is unavailable, mark it `unsupported`, stop, show the evidence, and ask the Producer before using tags or a logical folder map as a fallback.
- If upload/import/copy fails, retry only the import path within the producer-approved retry budget. Never regenerate the image in Higgsfield as a workaround.
- If the provider cannot attach the exact approved Codex image as a reference, stop and report the blocker; do not silently switch to text-only generation.
- If cost preflight is unavailable, stop before submission; do not estimate from a stale rate card or provider defaults.
- Do not generate multiple independent scenes in a single batch. Every attempt has its own scene card and explicit GO.

## Assembly handoff

After every required scene has a locally exported, technically verified, continuity-approved clip:

1. Create `06-edit/assembly-order.txt` from the approved script order.
2. Confirm consistent frame rate, resolution/aspect, codec, color space, and audio strategy; normalize by re-encoding when needed rather than stream-copying mixed formats blindly.
3. Assemble video and approved dialogue, effects, ambience, and score.
4. Decode and play the complete movie from beginning to end; inspect joins and listen for gaps/clipping/sync problems.
5. Record final runtime, frame dimensions, codecs, audio tracks, checksum, picture-lock decision, and delivery destination.
6. Deliver only after Producer approval of the full movie.
