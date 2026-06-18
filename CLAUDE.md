# CLAUDE.md — Forge operating contract (read me first)

Forge is an AI-operated, faceless short-form **content venture** ("The Ops Engine"):
vertical videos teaching local service businesses the automations that recover lost
revenue. **North star: time to first revenue → repeatable revenue.**
Phase 2 (build) is ~70% done. **The current bottleneck is distribution, not code.**

## Two agents, one repo
This venture is run by two Claude surfaces that share state through the files below.
Stay in your lane; both read/write the shared-state files.

**Claude Code (terminal / WSL) — owns the code & render factory**
- `src/forge/produce.py` + titan bridge, batch rendering, ffmpeg, YouTube OAuth upload
- n8n workflow exports for the $49 pack, git hygiene, tests, refactors
- Render: `PYTHONPATH=src .venv/bin/python -m forge.produce content/scripts/<batch>.md <i>`

**Cowork (desktop app) — owns distribution & ops**
- Funnel wiring (Kit, Gumroad, Instagram) via browser / computer-use
- Outreach (Gmail + `tracker/outreach-tracker.xlsx`), publishing, decks/docs
- Dashboard (`tracker/index.html`), scheduled briefings, weekly metrics pulls

## Shared state — single sources of truth (keep current)
- `docs/venture-memory.md` — decisions & phase log. **Append**, don't rewrite history.
- `docs/METRICS.md` — budget / revenue / funnel numbers. **Every result lands here.**
- `content/links.md` — real URLs as accounts go live (empty = funnel not wired yet).
- `tracker/index.html` — the dashboard; reads from the above. Update its snapshot
  numbers when the facts change.

## Hard constraints (both agents)
- **$0 spend** until first revenue. Free tiers only. Flag anything that asks for a card.
- **Never commit secrets.** titan `.env` is the only secret source.
- **Owner approves**: spending, account creation, *sending to real accounts*
  (emails / posts / uploads), legal/tax, and the final plan. Draft and stage freely —
  do not send or publish without an explicit yes.

## Priority right now (in order)
1. **Wire the funnel** so the 12 existing videos are monetizable (Kit page, Gumroad↔Kit,
   IG bio, real URLs in `links.md`).
2. **Run outreach** 10–20/day from `docs/outreach.md` → first **$300–1,500** service build.
3. **Publish daily** (`content/publishing.md` schedule) and **log every number** in METRICS.md.

> Rendering more videos is lower-leverage than distributing the 12 we already have.
> When in doubt, do the thing that moves us toward the first dollar.

## Collaboration protocol (Cowork ⇄ Claude Code)
Full version: **`docs/OPERATIONS.md`**. The essentials:

- **Stay in your lane.** Claude Code owns `src/`, `content/scripts/`, the pipeline.
  Cowork owns `tracker/`, ops `docs/`, funnel + outreach execution. Shared files are
  **append-only**: `docs/venture-memory.md`, `docs/METRICS.md`, `content/links.md`,
  `docs/worklog.md`, `docs/backlog.md`.
- **Every session:** `git pull` → read the top of `docs/worklog.md` + scan
  `docs/backlog.md` → claim tasks tagged for your lane.
- **End of session:** update shared files, append a `docs/worklog.md` entry
  (did / changed / handoff / next), then `git commit && git push`.
- **Routing tags:** `[CC]` Claude Code · `[CW]` Cowork · `[OWNER]` you ·
  `[CW→OWNER]` Cowork preps, you approve.
- **Definition of done:** not "built" — **consistent, repeatable revenue** (M0→M4 in
  `docs/OPERATIONS.md`).
