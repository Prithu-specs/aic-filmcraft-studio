# AIC Filmcraft Studio

A reusable AI filmmaking skill for Filmcraft-style productions: short social videos, proof reels, 3–15 minute shorts, and longer films.

## Includes

- character-led story development and beat planning;
- visual canon, asset registry, scene packet, and shot-card workflow;
- controlled generation, review, repair, continuity, and seam checks;
- editorial, sound, finishing, rights, delivery, and archive controls; and
- complete operating playbook with 20 actions and selectable specialist department routes;
- a provider-neutral, Codex-first asset workflow with a stable per-scene project tree;
- Higgsfield import/copy verification, scene-by-scene video dispatch, review, and final assembly gates; and
- a project scaffold script and provider-adapter contract so another compatible site can use the same structure.

## Use

Install the `AIC-Film-Craft-Studio` folder in a Codex-compatible skills directory. The main workflow is self-contained in `SKILL.md`; the `references/` directory supplies editable working templates and expanded guides.

For a new film, create a provider-neutral local scene tree after the story/scene count is approved:

```bash
python3 scripts/create_film_project.py "My Film" --scene-count 8 --provider higgsfield --root ~/Documents/Films
```

Use `workflow/PROVIDER-NEUTRAL-PRODUCTION.md` for the mandatory human+agent sequence and approval gates, `workflow/PROVIDER-ADAPTER-CONTRACT.md` for the stable interface, and `adapters/higgsfield.md` as the Higgsfield-specific mapping. Add another site's adapter by copying `adapters/provider-template.md`; keep the project tree, scene IDs, ledgers, and approval states unchanged.

## Source boundary

This package is original operating guidance informed by the public AI Filmmaking Studio Community Edition and Filmcraft workflow practice. It does not reproduce the source site’s examples, prompt catalogue, case studies, or current vendor claims. Verify tool capabilities, pricing, permissions, and rights for every production.
