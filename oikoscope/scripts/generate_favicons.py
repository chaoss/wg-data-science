"""
Generate square favicon assets from oikoscope/assets/oikoscope-logo.png
(icon mark only; crops left of the wordmark using layout heuristics).

Requires: pip install Pillow
Usage: py scripts/generate_favicons.py
Run from the oikoscope/ directory.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image

# Repo layout: this file lives in oikoscope/scripts/
ROOT = Path(__file__).resolve().parents[1]
LOGO = ROOT / "assets" / "oikoscope-logo.png"
OUT = ROOT / "assets"


def main() -> None:
    im = Image.open(LOGO).convert("RGB")
    w, h = im.size
    px = im.load()

    # Columns in the wordmark start around 425+; keep icon strictly left of that.
    x_max = min(435, w)
    xs: list[int] = []
    ys: list[int] = []
    for yy in range(h):
        for xx in range(x_max):
            p = px[xx, yy]
            if 255 - min(p) > 8:
                xs.append(xx)
                ys.append(yy)

    if not xs:
        raise SystemExit("Could not detect icon region; check oikoscope-logo.png")

    left, top, right, bot = min(xs), min(ys), max(xs), max(ys)
    # Small margin so ring anti-aliasing is not clipped
    pad = 14
    left = max(0, left - pad)
    top = max(0, top - pad)
    right = min(w - 1, right + pad)
    bot = min(h - 1, bot + pad)

    crop = im.crop((left, top, right + 1, bot + 1))
    cw, ch = crop.size
    side = max(cw, ch)
    square = Image.new("RGB", (side, side), (255, 255, 255))
    square.paste(crop, ((side - cw) // 2, (side - ch) // 2))

    OUT.mkdir(parents=True, exist_ok=True)

    # Standard sizes
    fav16 = square.resize((16, 16), Image.Resampling.LANCZOS)
    fav32 = square.resize((32, 32), Image.Resampling.LANCZOS)
    fav48 = square.resize((48, 48), Image.Resampling.LANCZOS)
    apple = square.resize((180, 180), Image.Resampling.LANCZOS)

    fav16.save(OUT / "favicon-16x16.png", optimize=True)
    fav32.save(OUT / "favicon-32x32.png", optimize=True)
    fav48.save(OUT / "favicon-48x48.png", optimize=True)
    apple.save(OUT / "apple-touch-icon.png", optimize=True)

    # Multi-size ICO (common browser/tab sizes)
    fav32.save(
        OUT / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
    )

    print("Wrote:", OUT / "favicon-16x16.png")
    print("Wrote:", OUT / "favicon-32x32.png")
    print("Wrote:", OUT / "favicon-48x48.png")
    print("Wrote:", OUT / "apple-touch-icon.png")
    print("Wrote:", OUT / "favicon.ico")


if __name__ == "__main__":
    main()
