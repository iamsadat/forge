"""Instagram Reels auto-publisher for Forge / The Ops Engine.

Posts the finished renders to Instagram via the **official Graph API** — the only
ToS-safe way to automate IG (no bot driving the app, so no ban risk). Mirrors the
owner-gated pattern of `publish.py`: dry-run by default, real posting needs --confirm.

How it works (no file upload needed): the repo is public, so each reel is fetchable
at its raw GitHub URL. The Graph API pulls the video from that URL, we poll the
container until it's processed, then publish.

Owner setup (one time, ~20 min — see docs / the chat runbook):
  1. Convert @the_ops_engine to a Professional/Business account + link a Facebook Page.
  2. Create a Meta app at developers.facebook.com → add the Instagram product.
  3. Get your IG Business account id + a long-lived access token with the
     `instagram_content_publish` permission.
  4. Put them in titan/.env:  IG_USER_ID=...   IG_ACCESS_TOKEN=...

Run:
  PYTHONPATH=src .venv/bin/python -m forge.publish_ig            # dry-run (lists what it would post)
  PYTHONPATH=src .venv/bin/python -m forge.publish_ig --confirm  # actually post
  PYTHONPATH=src .venv/bin/python -m forge.publish_ig --only the-50-000-leak-in-your-missed-calls --confirm
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

GRAPH = "https://graph.facebook.com/v21.0"
RAW_BASE = "https://raw.githubusercontent.com/iamsadat/forge/main/renders"
ROOT = Path(__file__).resolve().parents[2]
RENDERS = ROOT / "renders"

# Post the strongest hooks first (ROI order); the rest follow.
ORDER = [
    "the-50-000-leak-in-your-missed-calls",
    "3-automations-every-local-business-should-steal-in-2026",
    "you-lose-the-lead-in-the-first-5-minutes",
    "the-no-show-that-costs-you-300-every-week",
    "stop-letting-leads-die-in-your-dms",
    "the-quiet-reason-your-competitor-outranks-you",
]


def caption_for(slug: str) -> str:
    title = slug.replace("-", " ").replace("2 000", "2,000").replace("50 000", "50,000").title()
    return (
        f"{title}\n\n"
        "🔧 The automations that recover the calls, leads, bookings & reviews local "
        "service businesses quietly lose.\n"
        "👇 Free missed-call automation — link in bio.\n\n"
        "#smallbusiness #localbusiness #automation #aitools #entrepreneur "
        "#homeservices #smallbusinesstips"
    )


def _post(url: str, params: dict) -> dict:
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())


def _get(url: str, params: dict) -> dict:
    q = urllib.parse.urlencode(params)
    with urllib.request.urlopen(f"{url}?{q}", timeout=60) as r:
        return json.loads(r.read().decode())


def publish_reel(slug: str, ig_user_id: str, token: str) -> str:
    video_url = f"{RAW_BASE}/{slug}.mp4"
    # 1) create the media container
    container = _post(
        f"{GRAPH}/{ig_user_id}/media",
        {"media_type": "REELS", "video_url": video_url,
         "caption": caption_for(slug), "access_token": token},
    )
    cid = container["id"]
    # 2) poll until the reel finishes processing (up to ~5 min)
    for _ in range(60):
        st = _get(f"{GRAPH}/{cid}", {"fields": "status_code", "access_token": token})
        code = st.get("status_code")
        if code == "FINISHED":
            break
        if code == "ERROR":
            raise RuntimeError(f"IG processing error for {slug}: {st}")
        time.sleep(5)
    else:
        raise RuntimeError(f"timed out waiting for {slug} to process")
    # 3) publish
    res = _post(f"{GRAPH}/{ig_user_id}/media_publish",
                {"creation_id": cid, "access_token": token})
    return res["id"]


def main() -> None:
    confirm = "--confirm" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]

    slugs = [only] if only else ORDER
    ig_user_id = os.environ.get("IG_USER_ID", "")
    token = os.environ.get("IG_ACCESS_TOKEN", "")

    print(f"Instagram auto-publisher — {len(slugs)} reel(s), confirm={confirm}")
    if not (ig_user_id and token):
        print("⚠️  IG_USER_ID / IG_ACCESS_TOKEN not set — add them to titan/.env after the "
              "Meta setup. Showing dry-run plan only.\n")

    for slug in slugs:
        mp4 = RENDERS / f"{slug}.mp4"
        if not mp4.exists():
            print(f"  ✗ {slug}: render not found, skipping")
            continue
        if not confirm or not (ig_user_id and token):
            print(f"  • would post: {slug}\n      video: {RAW_BASE}/{slug}.mp4")
            continue
        try:
            media_id = publish_reel(slug, ig_user_id, token)
            print(f"  ✅ posted {slug} → media {media_id}")
            time.sleep(30)  # be gentle between posts
        except Exception as e:  # noqa: BLE001
            print(f"  ✗ {slug}: {e}")

    if not confirm:
        print("\nDry run. Re-run with --confirm (and IG_USER_ID/IG_ACCESS_TOKEN set) to post.")


if __name__ == "__main__":
    main()
