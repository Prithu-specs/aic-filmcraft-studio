# New provider adapter template

Copy this file to `adapters/<provider>.md`; keep the canonical workflow and folders unchanged. Do not add unsupported features as if they exist.

## Provider identity

- Provider/service:
- Account/workspace:
- Adapter version:
- Verified at (UTC):
- Verified by:

## Capability verification

| Operation | Supported? | Tool/API/UI evidence | Notes/limits |
|---|---|---|---|
| Create project | unknown | | |
| Create a folder per scene | unknown | | |
| Import approved Codex images | unknown | | |
| Copy/register imported images for reuse | unknown | | |
| Attach exact approved image reference to video | unknown | | |
| Quote exact cost without generation | unknown | | |
| Generate one video scene | unknown | | |
| Export clip to local storage | unknown | | |
| Read job status/output after interruption | unknown | | |

## Mapping rules

- Canonical project folder:
- Canonical scene ID format: `scene-NN-slug`
- Provider project ID stored at:
- Provider scene folder IDs stored at: `04-platform/platform-map.json`
- Media/copy IDs stored at: matching scene's `04-upload-proof/`
- Provider-specific settings stored at: matching scene's `03-prompt/` and `07-ledger/`

## Operational procedure

1. Create the platform project and record its ID/URL.
2. Create one provider folder per canonical scene ID; verify the folder list.
3. Import only Producer-approved Codex assets. Do not call the provider image generator.
4. Ask the provider to copy/register each imported asset into the reusable project library. Verify by returned media ID and reference selection.
5. Preflight the exact video request; show the quote and wait for this attempt's Producer GO.
6. Generate one scene at a time, export, probe, and review before advancing.
7. Assemble only after all required clips pass their review gates.

## Unsupported capability protocol

If any mandatory feature is unsupported, record the evidence and stop at that gate. Do not switch to provider image generation, omit a scene folder, drop reference conditioning, guess costs, or batch unrelated scenes. Ask the Producer before using a clearly mapped equivalent; retain canonical IDs and folder layout regardless.
