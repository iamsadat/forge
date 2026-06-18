# Backlog — routed to first (and repeatable) revenue

Tags: `[CC]` Claude Code · `[CW]` Cowork · `[OWNER]` you · `[CW→OWNER]` Cowork preps,
you approve. Pull from your lane, top-down. Check items off in your commits.
Milestones (M0–M4) are defined in `docs/OPERATIONS.md`.

## 🎯 M0 — Funnel live  (unblocks every existing video)
- [ ] `[CW→OWNER]` Build the Kit landing page (bio hub) — `docs/funnel-setup.md` §B
- [ ] `[OWNER]` Connect Gumroad → Kit (API key, tags `free-magnet`/`customer`) — §C
- [ ] `[CW]` Paste real URLs into `content/links.md` once live (BIO_HUB, AFF_N8N)
- [ ] `[OWNER]` Set Instagram bio link = the Kit landing page
- [ ] `[CW]` Refresh dashboard snapshot once links are live
- [ ] `[CW]` **DEPLOY the redesigned `tracker/index.html` to the live Lovable app** — owner can't see the redesign live; repo file ≠ Lovable project, no deploy pipeline (urgent)
- [ ] `[CW]` Re-upload rebuilt `content/product/templates.zip` to the $49 Gumroad product (now has all 5 workflows)

## 💵 M1 — First $1  (prove it takes money)
- [ ] `[CW→OWNER]` Start outreach 10–20/day — `docs/outreach.md` + `tracker/outreach-tracker.xlsx`
- [ ] `[CW→OWNER]` Publish first reels (3–4/wk) — `content/publishing.md` schedule
- [ ] `[CW]` Log first opt-ins / views / sales in `docs/METRICS.md`
- [ ] `[OWNER]` Confirm n8n affiliate acceptance → `[CW]` drop link into nurture Email 3

## 🔧 M2 — First service build  ($300–1,500)
- [ ] `[CW→OWNER]` Book a free audit from an outreach reply
- [x] `[CC]` Finalize the flagship missed-call n8n workflow for client deploy — done 2026-06-18 (Config node + missed-call filter + parameterized; validated)
- [x] `[CC]` Export the other 4 workflows (speed-to-lead, reviews, reminders, nurture) — done 2026-06-18 (02–05 JSON validated; templates.zip rebuilt → `[CW]` re-upload to Gumroad)
- [ ] `[OWNER]` Deliver first build (client's own Twilio — we stay $0)

## 📈 M3–M4 — Repeatable
- [x] `[CC]` Wire YouTube OAuth auto-upload — done 2026-06-18 (`src/forge/publish.py` reuses titan's client; dry-run validated all 12; owner-gated: `--confirm` stages as private) → `[OWNER]` run `--confirm` when ready
- [ ] `[CC]` Render batch03 — **deferred** (distributing the existing 12 > rendering more; do after first traffic/data)
- [ ] `[CW]` Weekly metrics review → double-down vs cut (scheduled task does the pull)
- [ ] `[CW]` Promote `tracker/index.html` to a live Cowork artifact pulling real funnel data
- [ ] `[OWNER]` Set kill/scale criteria in `docs/METRICS.md` after 2–3 weeks of data

## 🧊 Icebox (later)
- [ ] `[CC]` Long-form for YouTube monetization (YPP)
- [ ] `[CW]` Second product / upsell once the $49 pack converts
- [ ] `[CW]` Connect analytics (YouTube/Gumroad/Kit) so dashboards + reviews auto-fill
