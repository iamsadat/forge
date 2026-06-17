"""Faceless render driver for Forge.

Composes titan's *pure* pipeline pieces (parse_reel_script, make_voiceover,
write_ass, fetch_broll, build_ffmpeg_command) but guarantees the b-roll
visuals cover the full voiceover. titan's own render_reel only pads visuals
with product stills, which faceless (no-product) content doesn't have — so a
b-roll-only render would truncate to clip_count * scene_duration and cut the
audio/captions. We size + cycle b-roll to the VO length instead.

Run:  PYTHONPATH=src .venv/bin/python -m forge.produce content/scripts/batch01.md 1
"""

from __future__ import annotations

import subprocess
import sys
from itertools import cycle, islice
from math import ceil
from pathlib import Path

from forge import bootstrap  # noqa: F401 — loads titan env + sys.path first

from titan.content.assets import fetch_broll, fetch_music
from titan.content.captions import write_ass
from titan.content.video import (
    build_ffmpeg_command,
    ffmpeg_available,
    make_voiceover,
    parse_reel_script,
)

ROOT = Path(__file__).resolve().parents[2]  # forge/
RENDERS = ROOT / "renders"
BROLL_DIR = ROOT / "assets" / "broll"
SCENE_DURATION = 2.5
MAX_CLIPS = 16


def _slug(title: str, fallback: str) -> str:
    s = "".join(c if c.isalnum() else "-" for c in title.lower())
    s = "-".join(p for p in s.split("-") if p)[:60]
    return s or fallback


def render_script(scripts_file: str, index: int, out_path: str | None = None) -> str:
    if not ffmpeg_available():
        raise RuntimeError("ffmpeg not available on PATH")

    script = parse_reel_script(scripts_file, index)
    RENDERS.mkdir(parents=True, exist_ok=True)
    BROLL_DIR.mkdir(parents=True, exist_ok=True)

    out = Path(out_path) if out_path else RENDERS / f"{_slug(script['title'], f'script{index}')}.mp4"
    stem_path = out.parent / out.stem

    # --- Voiceover + word timings ---
    vo_path = str(stem_path) + ".vo.mp3"
    word_timings = make_voiceover(script["narration"], vo_path)
    vo_dur = word_timings[-1]["end"] if word_timings else len(script["scenes"]) * SCENE_DURATION

    # --- Captions ---
    ass_path: str | None = None
    if word_timings:
        ass_path = str(stem_path) + ".captions.ass"
        write_ass(word_timings, ass_path)

    # --- B-roll sized to cover the VO (+1 buffer for xfade overlap) ---
    needed = min(MAX_CLIPS, max(2, ceil(vo_dur / SCENE_DURATION) + 1))
    queries = [s["broll"] for s in script["scenes"] if s.get("broll")]
    if not queries:
        queries = [script.get("product") or "small business office"]
    clips = fetch_broll(queries, count=needed, out_dir=str(BROLL_DIR))
    if not clips:
        raise RuntimeError("no b-roll fetched — check Pexels key / network")
    if len(clips) < needed:
        clips = list(islice(cycle(clips), needed))

    music = fetch_music("upbeat", str(BROLL_DIR))

    cmd = build_ffmpeg_command(
        image_paths=[],
        voiceover_path=vo_path,
        out_path=str(out),
        hook=script["hook"],
        scenes=script["scenes"],
        music_path=music,
        scene_duration=SCENE_DURATION,
        ass_path=ass_path,
        video_paths=clips,
    )
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"ffmpeg failed:\n{res.stderr[-1800:]}")
    return str(out)


if __name__ == "__main__":
    scripts_file = sys.argv[1]
    idx = int(sys.argv[2])
    print(render_script(scripts_file, idx))
