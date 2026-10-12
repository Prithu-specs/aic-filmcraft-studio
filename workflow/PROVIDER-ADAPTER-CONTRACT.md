# Provider adapter contract

Adapters make the provider interchangeable without changing the canonical project/scene layout, approvals, IDs, or evidence records. This is a contract for implementation and operation; it does not claim that every provider exposes every capability.

## Required adapter operations

An adapter must expose or document these operations using the target provider's actual supported controls:

1. `create_project(project_name, format)` → provider project ID and URL.
2. `create_scene_folder(project_id, scene_id, scene_title)` → provider folder ID/URL.
3. `import_asset(project_id, scene_folder_id, local_path, asset_id)` → provider media ID.
4. `copy_or_register_asset(project_id, scene_folder_id, media_id, asset_id)` → reusable reference ID or an explicit unsupported result.
5. `verify_asset(project_id, scene_folder_id, asset_id, media_id)` → evidence that the expected image is selectable as a reference.
6. `preflight_video(scene_id, shot_card, model_settings)` → exact quote, quote timestamp, and accepted settings; no job submission.
7. `generate_video(scene_id, approved_asset_ids, approved_prompt, approved_settings)` → job ID/status/output; only after the Producer's exact-attempt GO.
8. `export_scene(scene_id, provider_output_id, local_destination)` → local file plus validation metadata.
9. `verify_scene(scene_id, local_file)` → duration, dimensions, codec, audio presence, playback/review evidence.
10. `list_jobs` / `read_job` → recoverable status and output references.

If a provider does not offer a required operation (e.g. native folders, copy/register, or exact image-reference input), the adapter must return `unsupported` with evidence. Do not silently approximate it. Ask the Producer before using a logical folder/tag fallback; preserve the canonical scene folder and IDs regardless.

## Common records

- `project_id`: canonical project slug, unchanged across providers.
- `scene_id`: `scene-NN-slug`, stable across local and provider storage.
- `asset_id`: `<family>-<slug>-vNN`, e.g. `prop-briefcase-v01`.
- `provider_project_id`, `provider_folder_id`, `provider_media_id`, `provider_job_id`: provider-specific identifiers, stored as fields in mapping files only.
- `approval_state`: `candidate | approved | rejected | repair | stale`.
- `attempt_state`: `planned | quoted | awaiting_go | submitted | complete | review | approved | repair | retired | failed`.

## Spend and authority contract

- Asset images are created only in Codex. Provider adapters may upload, duplicate/register, organize, or reference those images; they must never invoke provider image generation for film assets.
- A quote is valid only for the exact provider, model, resolution, aspect ratio, duration, options, references, output count, and current price returned by the provider preflight.
- No generation call may occur from a `planned`, `quoted`, or `awaiting_go` state. It requires a recorded explicit Producer GO matching the attempt ID and quote.
- Every repair/retry is a new attempt with its own fresh quote and approval.
- A provider can return a candidate; it cannot set Producer approval state.

## Storage and naming

Local files remain the source of truth. Each provider folder mirrors the matching local `scene-NN-slug`. Keep a `04-platform/platform-map.json` with the mapping; never rename canonical IDs to match provider folder IDs. Store import/copy proof and provider job IDs under that same scene's `04-upload-proof/` and `07-ledger/`.

## Compatibility matrix

Each adapter maintains a checked-at date and fills this matrix from live provider evidence before use:

| Capability | Required evidence |
|---|---|
| Project creation | project ID, URL, account/workspace |
| Folder creation | folder IDs matching canonical scene IDs |
| Upload/import | media IDs + successful completion |
| Copy/register | reusable reference ID or explicit unsupported result |
| Reference attach | accepted media role and visible attachment confirmation |
| Quote-only cost | exact cost with no generation submitted |
| Video generation | model, durations, resolution, audio, output count |
| Export | accessible local file and media probe |
| Job recovery | status/output lookup for interrupted session |

Last checked is operational metadata, not a promise of perpetual provider support. Verify again on every production.
