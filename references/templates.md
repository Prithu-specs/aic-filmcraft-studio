# Working templates

Copy the smallest template that fits. Keep the current approved version in the project root and link every scene, attempt, review, and delivery record to it.

## Brief and delivery card

```markdown
# [Project] brief v001

- Owner / final release authority:
- Audience and destination:
- Runtime, aspect ratio, delivery date:
- Spending ceiling and protected edit/QA reserve:
- Verified current tools and constraints:
- Rights, consent, music, voice, and source constraints:

## Creative contract
- Logline:
- Viewer question and desired final feeling:
- Beginning → change → consequence:
- Turn/payoff:
- Key visual:
- Emotional, camera, color, and sound direction:
- Riskiest creative or technical dependency:

## Approval envelope
- May proceed without another approval:
- Must be approved before proceeding:
- Final release decision:
```

## Canon and asset registry

```markdown
# Canon v001

## Fixed visual and sound rules
- Format / frame / typography:
- Character identity, wardrobe, performance, and voice:
- Props and their state:
- Locations, geography, time, lighting, palette:
- Camera grammar and prohibited drift:
- Sound and music rules:

## Asset registry
| Asset ID | Item | Version | Source / path | Rights status | Scope | State | Owner |
|---|---|---|---|---|---|---|---|

## Change log
| Version | Change | Why | Impacted scenes/assets/prompts/edit | Approval | Date |
|---|---|---|---|---|---|
```

## Scene packet and shot card

```markdown
# Scene [ID] — [title]
- Canon / brief version:
- Scene purpose and what the viewer must understand:
- Incoming state → dominant change → outgoing state:
- Character want, pressure, decision, and visible behavior:
- Dialogue / silence / title timing:
- Location, time, geography, costume and prop state:
- Blocking, frame, lens/perspective, movement, lighting, color:
- Sound role: dialogue / ambience / Foley / SFX / music / silence:
- Exact approved references:
- Continuity risks and required coverage:
- Acceptance criteria:
- Fallback method and estimated test cost:

## Shot [ID]
- Fixed canon block:
- Variable action block:
- Start image / action / end image:
- Duration and edit purpose:
- Inputs and current tool settings:
- Acceptance criteria:
```

## Asset-first 10-second unit manifest

Create one of these records in every `unit-[NN]-[slug]-[duration]` folder before any upload or paid render.

```markdown
# Unit [ID] — [duration] — [title]
- Scene packet / canon version:
- Incoming state → one timed action → outgoing state:
- Visible character count and identity:
- Locked location geometry and non-negotiable features:
- Props, owner/hand/placement, and state:
- Assets created or copied into `02-assets/`:
- Visual inspection evidence and defects corrected:
- Generator destination/account/project:
- Uploaded filenames and completion proof:
- Fixed canon block / variable action block / hard exclusions:
- Settings and exact credits:
- Producer approval for this exact attempt:
- Moving-clip review: 0% / 25% / 50% / 75% / 100%:
- Decision and approved carry-over frame/state:
```

## Generation preflight and attempt record

```markdown
| Attempt ID | Scene/shot | Canon/asset version | Tool/model/settings | Inputs | Cost/credits | Expected test | Output path | Result | Decision | Defect / next action |
|---|---|---|---|---|---:|---|---|---|---|---|
```

Before submitting: confirm the current tool’s duration, reference, export, rights, and pricing conditions; check asset links; protect the reserve; state the single acceptance test.

## Local MiniMax H3 feasibility and recovery record

```markdown
# Local MiniMax H3 job [ID]
- Repository remote / pinned revision / integrity check:
- Runtime, model root, LoRA, Python, and ffmpeg paths verified:
- Machine memory / free disk / power state:
- Source duration and 32-pixel-aligned canvas:
- Preflight JSON path and PASS result:
- One-shot job ID; automatic relaunch disabled:
- Start-frame lock / prompt / seed / output path:
- Result: complete / failed / blocked:
- Full error log path and exact error signature:
- Failure classification: memory / runtime / muxing / asset / continuity / other:
- Approved recovery change (one variable only):
- 0 / 25 / 50 / 75 / 100 percent review and carry-over frame:
```

## Clip and seam review

```markdown
# Review [ID]
- Item / retained interval / intended edit use:
- Reviewer and date:
- Creative evidence:
- Continuity evidence:
- Technical evidence:
- Rights/accessibility evidence:
- Join test with preceding/following item:
- Decision: approve / repair / retire / blocked
- Targeted revision request or next action:
```

## Master, delivery, and archive

```markdown
# Master and delivery record
- Picture-lock cut and audio/stem versions:
- Full decode/watch/listen completed by:
- Frame, audio, captions, credits, metadata, rights, platform checks:
- Master file checksum or path:
- Destination and receipt/proof:
- Archive location and recovery test:
- Lesson for next production:
```
