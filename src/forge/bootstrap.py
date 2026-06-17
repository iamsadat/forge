"""Reuse bridge to the titan content pipeline.

Single source of truth for code AND secrets:
  - titan modules are imported from the sibling `titan/src` (no copy, no drift).
  - titan's `.env` (TITAN_*-prefixed keys) is loaded by absolute path, so the
    pipeline's `settings` singleton sees the Pexels + YouTube creds regardless
    of the current working directory.

Import this module BEFORE any `titan.*` import so env vars are populated first.
"""

from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv

# forge/src/forge/bootstrap.py -> parents[3] == Desktop ; titan is a sibling of forge
TITAN_ROOT = Path(__file__).resolve().parents[3] / "titan"
TITAN_SRC = TITAN_ROOT / "src"
TITAN_ENV = TITAN_ROOT / ".env"

if not TITAN_SRC.exists():  # fail loud, not silent
    raise RuntimeError(f"titan source not found at {TITAN_SRC}")

if str(TITAN_SRC) not in sys.path:
    sys.path.insert(0, str(TITAN_SRC))

# Load titan secrets into the process env BEFORE titan.config builds its singleton.
load_dotenv(TITAN_ENV)

# Now safe to pull in the reusable pipeline pieces.
from titan.config import settings  # noqa: E402
from titan.content.assets.pexels import PexelsClient  # noqa: E402
from titan.content.publish.youtube import YouTubeClient  # noqa: E402
from titan.content.video import ffmpeg_available, render_reel  # noqa: E402

__all__ = [
    "settings",
    "PexelsClient",
    "YouTubeClient",
    "render_reel",
    "ffmpeg_available",
    "TITAN_ROOT",
    "TITAN_ENV",
]


def status() -> dict:
    """Lightweight health snapshot — booleans only, never secret values."""
    return {
        "titan_src": str(TITAN_SRC),
        "titan_env_loaded": TITAN_ENV.exists(),
        "ffmpeg": ffmpeg_available(),
        "pexels_key": bool(getattr(settings, "pexels_api_key", "")),
        "youtube_refresh_token": bool(getattr(settings, "youtube_refresh_token", "")),
        "youtube_client_id": bool(getattr(settings, "youtube_client_id", "")),
        "youtube_client_secret": bool(getattr(settings, "youtube_client_secret", "")),
    }
