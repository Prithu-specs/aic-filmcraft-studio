# Film project template

Create this tree with `python3 scripts/create_film_project.py "Project Name" --scene-count <approved-count> --provider <adapter> --root <parent>`.

```text
<slug>/
  00-admin/
    project-manifest.json
    approvals.csv
    credit-ledger.csv
  01-story/
    script.md
  02-canon/
    characters/ props/ locations/ color-lighting/ sound/
  03-storyboards/
    scene-NN-unassigned/frames/
    scene-NN-unassigned/review/
  04-platform/
    platform-map.json
  05-production/
    scene-NN-unassigned/
      01-authority/scene-card.md
      02-assets/asset-manifest.json
      03-prompt/
      04-upload-proof/
      05-renders/
      06-audio/
      07-ledger/attempt-ledger.csv
  06-edit/assembly/assembly-order.txt
  07-delivery/
  08-archive/
```

Rename each `scene-NN-unassigned` only when the approved beat map is locked. Use the exact same final canonical scene ID for the local folder, storyboard folder, provider-side folder, attempt ledger, and edit order. Provider IDs belong only in `04-platform/platform-map.json` and per-scene upload evidence.

Do not store generated media in the skill repository. The scaffolded film project is the source of truth. Create every still in Codex, obtain Producer approval, then import/copy the approved stills into the selected video provider. The provider generates video only after per-scene quote and approval.
