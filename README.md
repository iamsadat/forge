# Forge

AI-operated faceless short-form **content venture**. North-star metric: time to
**first revenue**, then repeatable revenue. $0 paid spend until first revenue.

Separate, clean project. **Reuses** the battle-tested `titan` faceless-video
pipeline (sibling repo) — does not rebuild it.

## Status
- **Phase 0 — environment:** ✅ done.
- **Phase 1 — research + plan:** ✅ done. Niche locked: AI automation for local
  service businesses; studio brand **The Ops Engine**. Plan approved.
- **Phase 2 — build:** 🔄 ~70%. 12 scripts + 12 rendered & verified videos,
  monetization (4 streams), publishing/SEO, outreach kit, flagship n8n workflow,
  progress tracker.
- **Progress tracker:** `tracker/index.html` (in-repo, open locally) + hosted
  interactive [Lovable app](https://forge-ops-engine-tracker.lovable.app).
- **GitHub:** ✅ pushed — https://github.com/iamsadat/forge (private). The 12
  final MP4 deliverables are included; the 2.3 GB raw Pexels cache and secrets
  stay gitignored.

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
