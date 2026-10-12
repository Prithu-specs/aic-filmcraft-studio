# Provider-neutral film production workflow

This is the canonical process for a scene-based film. The project layout and gate semantics do not change by platform. A provider adapter only maps the standard operations to a site's actual UI/API and must report unsupported capabilities rather than silently skipping them.

## Human authority and department agents

- **Producer:** Prithu; owns script, image, prompt, spend, repair, and release approvals.
- **Film Director agent:** narrative intent, blocking, performance, shot-to-beat fit.
- **Art Director agent:** characters, props, environments, palette, visual continuity.
- **Music Director agent:** dialogue/music/sound plan and emotional progression.
- **Lighting Director agent:** motivated lighting, exposure, source direction, scene continuity.

Agents propose and review; none can authorize paid attempts or approve assets on the Producer's behalf.

## Mandatory sequence

1. **Create the project and scene map.** Approve the story, scene count, dialogue, format, palette, deliverable, budget envelope, and rights plan. Create one local scene folder per approved scene using the scaffold.
2. **Lock the visual canon.** Define character anatomy/turnarounds, prop anatomy and exact dimensions, location geometry, wardrobe, color bible, lighting rules, sound palette, and prohibited drift. Give every asset a stable ID and version.
3. **Create all stills in Codex only.** This includes character sheets, prop sheets, backgrounds, storyboards, and production/start frames. Never generate or edit stills with a video-platform image-credit balance. Codex subscription/quota use must be disclosed honestly. Save the originals and provenance in the local project.
4. **Review and approve the image batches.** Show every generated image. Mark each asset `candidate`, `approved`, `rejected`, or `repair`. A rejected still cannot become a video reference. Fix from the approved source, show the replacement, and obtain approval again.
5. **Prepare platform project and folders.** Create the project in the chosen video service and one scene folder per approved scene. Keep the exact canonical IDs (`scene-01-...`) and map local folders to platform folders in `04-platform/platform-map.json`.
6. **Import and copy approved assets.** Upload only approved Codex files into their corresponding platform scene folders. Ask the platform to copy/register each file into project assets as reusable references. Verify every file by ID/name/preview and log proof. Do not regenerate the still in the video platform. If folder creation, copying, or reference attachment is unsupported, pause and report the limitation; get Producer approval for a documented equivalent before continuing.
7. **Write and approve one video card per scene/shot.** It names exact references, scene action, dialogue, movement, camera, lighting, sound, model, resolution, ratio, duration, current attempt cost, acceptance checks, and continuity risk. Preflight cost through the selected provider immediately before the attempt. Display the card and exact price; wait for Producer `GO` for that specific attempt. A broad project GO is not batch spend authorization.
8. **Generate video scene by scene.** Submit one scene/shot at a time from its platform folder, referencing only the approved imported assets. Record job ID, inputs, price, output, and status in that scene's ledger. Rejected generations and repairs are retained as evidence; every paid retry needs a new quote and GO.
9. **Review each full moving clip before advancing.** Review at 0%, 25%, 50%, 75%, and 100%, plus audio. Check identity, prop dimensions and ownership, action mechanics, geography, screen direction, dialogue intelligibility, music/sound, and end state. Only approved clips enter the edit.
10. **Assemble after every required scene is complete.** Join approved scene clips in script order with approved transitions, dialogue, sound effects, and score. Review the whole movie from start to finish with sound. Verify duration, codecs, resolution, audio sync, color, captions, rights, and final scene order. Producer picture-locks the master before delivery.
11. **Archive and deliver.** Keep the brief, script, approvals, Codex originals, provider import map, scene folders, prompts, cost ledger, candidates, selected clips, edit recipe, audio, QA, and final master together. Deliver only a verified, Producer-approved master.

## Stable project layout

```text
<project>/
  00-admin/                   # brief, roles, approvals, spend ledger, project manifest
  01-story/                   # approved script, dialogue, beat map
  02-canon/
    characters/               # Codex-made anatomy/turnaround sheets + canon
    props/                    # Codex-made prop anatomy sheets + exact dimensions
    locations/                # Codex-made location/background references
    color-lighting/           # approved color bible and lighting continuity
    sound/                    # dialogue/music/sound plan and rights
  03-storyboards/
    scene-NN-slug/            # Codex-made storyboard frames + review decision
  04-platform/                # adapter name, platform project ID, folder/media mapping
  05-production/
    scene-NN-slug/
      01-authority/           # approved scene card and beat
      02-assets/              # approved Codex source stills and manifest
      03-prompt/              # fixed canon + variable shot prompt
      04-upload-proof/        # imported/copied platform assets and verification
      05-renders/             # candidates, review, approved scene clip
      06-audio/               # dialogue, Foley, ambience, music for this scene
      07-ledger/              # per-attempt cost, approval, job, QC
  06-edit/                    # assembly order, edit instructions, joins, picture-lock
  07-delivery/                # verified master, captions, delivery receipt
  08-archive/                 # recovery notes, provenance, postmortem
```

Every provider adapter must preserve this tree and the `scene-NN-slug` identifiers. Platform-side folders mirror the scene IDs; provider-specific IDs are stored only in the mapping ledger, never substituted for canonical IDs.
