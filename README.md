# Forge

AI-operated faceless short-form **content venture**. North-star metric: time to
**first revenue**, then repeatable revenue. $0 paid spend until first revenue.

Separate, clean project. **Reuses** the battle-tested `titan` faceless-video
pipeline (sibling repo) — does not rebuild it.

## Status
- **Phase 0 — environment:** ✅ done (this scaffold).
- **Phase 1 — niche research + business plan:** in progress. Niche is **OPEN**;
  decided by evidence, owner sign-off required before any build.

## Layout
```
src/forge/        venture code (bootstrap bridge to titan, future pipelines)
content/scripts/  video scripts by pillar
assets/           broll / music / thumbnails (gitignored, regenerable)
docs/             business plan, decisions, metrics
data/             metrics db (gitignored)
.venv/            dedicated WSL-native venv (gitignored)
```

## Reuse model
`src/forge/bootstrap.py` adds `titan/src` to the path, loads titan's `.env`
(secrets stay there — never duplicated), and re-exports `render_reel`,
`PexelsClient`, `YouTubeClient`, `ffmpeg_available`.

```bash
.venv/bin/python -c "from forge import bootstrap; print(bootstrap.status())"
```

## Constraints
- $0 spend until first revenue. Free tiers only.
- Never commit secrets (`.env`, tokens) — gitignored.
- Owner approves: spending, account creation, legal/tax, and the final plan.
