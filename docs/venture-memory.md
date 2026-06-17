# Forge — Venture Memory (living state)

_Single source of truth for decisions. Update as we go._

## Identity
- **Project:** Forge — AI-operated faceless short-form content venture.
- **Owner:** technical founder (data engineer; Python/APIs/OAuth). Operates on
  Windows + WSL. Sets direction & approves; AI executes.
- **North star:** time to first revenue → repeatable revenue.

## Hard constraints
- $0 paid spend until first revenue (free tiers only).
- Never commit secrets; titan `.env` is the single secret source.
- Owner personally approves: spending, account creation, legal/tax, FINAL PLAN.

## Assets reused (not rebuilt)
- titan faceless-video pipeline (`titan/src/titan/content/`): `video.py`
  (script→edge-tts VO→vertical MP4), `captions.py` (karaoke ASS), `effects.py`
  (ffmpeg drawtext/zoompan/xfade), `assets/pexels.py` (b-roll), `daily.py`
  (rotating render+publish), `publish/youtube.py` (OAuth upload).
- Reused via `forge/src/forge/bootstrap.py` (path + titan `.env`).
- Verified keys: Pexels ✅, YouTube refresh/client_id/client_secret ✅.
  Pixabay/ElevenLabs empty (not needed — edge-tts is free).

## Open decisions (Phase 1 — research first, NO defaults)
- **NICHE / ANGLE / FORMAT / PLATFORM MIX: OPEN.** To be scored on:
  monetization depth, buyer-intent, competition, production fit, credibility
  fit, speed to first revenue. NOT assumed (not AI, not finance, nothing).
- Monetization: design for 4 streams (affiliate · $29–99 product · lead-gen
  service · ads). Streams 1–3 must score well, not just ads.

## Phase log
- 2026-06-16 — Phase 0 done: venture scaffolded, dedicated WSL venv, titan
  reuse bridge wired, keys verified, metrics tracker live. $0 spend.
- 2026-06-16 — Phase 1 started: niche research.
- 2026-06-17 — Phase 1 done: niche locked (SMB automation, horizontal service
  offer), studio brand "The Ops Engine"; plan approved by owner.
- 2026-06-17 — Phase 2 build: 6 scripts (batch01) written + all 6 rendered &
  verified on WSL (806KB–2MB MP4s). Render driver `produce.py` fixes faceless
  b-roll VO coverage. Monetization (4 streams) + publishing/SEO drafted.
  $49 product pack started (flagship n8n workflow + setup recipes).
  Interactive progress tracker built (in-repo `tracker/index.html` + hosted
  Lovable app: https://forge-ops-engine-tracker.lovable.app).
- 2026-06-17 — GitHub push BLOCKED: no creds/gh in env; repo committed locally
  & push-ready (`scripts/push_to_github.sh`). Owner must auth to push.
