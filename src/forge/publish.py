"""Stage + upload Forge's rendered Shorts to YouTube.

Reuses titan's working ``YouTubeClient`` (OAuth refresh-token flow, resumable
upload) via the titan bridge — no new auth code, no duplicated secrets.

**Owner-gated by design.** Defaults to a fully offline **dry-run** (builds and
prints the exact YouTube metadata for every render but touches no network). A
real upload requires ``--confirm`` *and* defaults to ``privacy=private`` so
nothing ever goes public without the owner reviewing it in YouTube Studio first.

Per-video metadata is derived from the same scripts that produced the renders
(so titles/slugs line up), following the rules in ``content/publishing.md``
(``#Shorts`` title, hook + value + CTA, bio link, niche tags).

Run (safe, offline preview of all 12):
    PYTHONPATH=src .venv/bin/python -m forge.publish

Stage to YouTube as PRIVATE drafts (only after the owner says go):
    PYTHONPATH=src .venv/bin/python -m forge.publish --confirm
    PYTHONPATH=src .venv/bin/python -m forge.publish --confirm --only the-50-000-leak-in-your-missed-calls
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from forge import bootstrap  # noqa: F401 — loads titan env + sys.path first
from forge.produce import RENDERS, _slug

from titan.content.video import parse_reel_script
from titan.content.publish.youtube import YouTubeClient

ROOT = Path(__file__).resolve().parents[2]  # forge/
BATCHES = ["content/scripts/batch01.md", "content/scripts/batch02.md"]

TAGS = [
    "small business", "local business", "automation", "ai automation",
    "small business tips", "entrepreneur", "home services", "ai tools",
]
BIO_CTA = "\U0001F517 Free automation templates: link in bio."

# significant-word threshold for fuzzy matching a script title to a render file
_STOP = {"the", "a", "an", "in", "your", "you", "to", "of", "for", "and", "on", "every", "this", "that"}


def build_metadata(script: dict) -> tuple[str, str, list[str]]:
    """YouTube (title, description, tags) for one parsed script."""
    base = script["title"].strip().strip('"')
    title = base if base.lower().rstrip().endswith("#shorts") else f"{base} #Shorts"
    title = title[:100]

    value = " ".join(s["text"] for s in script.get("scenes", [])[:2]).strip()
    hashtags = " ".join("#" + t.replace(" ", "") for t in TAGS[:5])
    parts = [script.get("hook", "").strip(), value, script.get("cta", "").strip(), BIO_CTA, hashtags]
    description = "\n\n".join(p for p in parts if p)[:4900]
    return title, description, TAGS


def _available_stems() -> list[str]:
    return sorted(p.stem for p in RENDERS.glob("*.mp4")) if RENDERS.exists() else []


def _match_render(slug: str, stems: list[str]) -> Path | None:
    """Exact slug match, else best fuzzy match by shared significant words."""
    if slug in stems:
        return RENDERS / f"{slug}.mp4"
    want = {w for w in slug.split("-") if w and w not in _STOP}
    best, best_score = None, 0
    for stem in stems:
        have = {w for w in stem.split("-") if w and w not in _STOP}
        score = len(want & have)
        if score > best_score:
            best, best_score = stem, score
    if best and best_score >= 2:
        return RENDERS / f"{best}.mp4"
    return None


def iter_videos():
    """Yield (batch, index, script, render_path|None) for every script."""
    stems = _available_stems()
    used: set[str] = set()
    for batch in BATCHES:
        path = ROOT / batch
        if not path.exists():
            continue
        i = 1
        while True:
            try:
                script = parse_reel_script(str(path), i)
            except ValueError:
                break
            slug = _slug(script["title"], f"script{i}")
            render = _match_render(slug, [s for s in stems if s not in used])
            if render:
                used.add(render.stem)
            yield batch, i, script, render
            i += 1


def main() -> None:
    ap = argparse.ArgumentParser(description="Stage/upload Forge Shorts to YouTube (owner-gated).")
    ap.add_argument("--confirm", action="store_true", help="actually upload (default: dry-run, no network)")
    ap.add_argument("--privacy", default="private", choices=["private", "unlisted", "public"],
                    help="upload privacy (default: private — review before going public)")
    ap.add_argument("--only", help="only the render with this slug/stem")
    ap.add_argument("--limit", type=int, default=0, help="cap number processed")
    args = ap.parse_args()

    yt = YouTubeClient()
    configured = yt.is_configured()
    mode = "LIVE UPLOAD" if args.confirm else "DRY-RUN (offline, no upload)"
    print(f"== forge.publish · {mode} · privacy={args.privacy} · YouTube creds={'OK' if configured else 'MISSING'} ==\n")
    if args.confirm and not configured:
        sys.exit("YouTube creds missing — cannot upload. Check titan .env (TITAN_YOUTUBE_*).")

    total = ready = missing = 0
    for _batch, _idx, script, render in iter_videos():
        title, description, tags = build_metadata(script)
        slug = render.stem if render else _slug(script["title"], "?")
        if args.only and args.only != slug:
            continue
        total += 1
        if render is None or not render.exists():
            missing += 1
            print(f"[{total:>2}] ✗ MISSING RENDER  ({_slug(script['title'], '?')})\n      title: {title}\n")
            continue
        result = yt.upload_short(
            str(render), title, description, tags,
            dry_run=not args.confirm, confirm=args.confirm, privacy_status=args.privacy,
        )
        ready += 1
        print(f"[{total:>2}] ✓ {slug}")
        print(f"      title: {title}")
        print(f"      tags : {', '.join(tags)}")
        if args.confirm:
            vid = result.get("id")
            link = f"https://youtu.be/{vid}" if vid else "(no id returned)"
            print(f"      uploaded → {link}  (privacy={args.privacy})")
        print()
        if args.limit and total >= args.limit:
            break

    print(f"== {ready} ready/uploaded · {missing} missing render · {total} total ==")
    if not args.confirm:
        print("Dry-run only — nothing was uploaded. Re-run with --confirm (owner approval) to stage as private.")


if __name__ == "__main__":
    main()
