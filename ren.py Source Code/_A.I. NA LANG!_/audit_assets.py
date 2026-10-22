# Run from inside the game folder (or its parent):  python audit_assets.py
# Read-only. Changes nothing. Shows which assets cost the most memory and download size.
import os
from PIL import Image

root = "." if os.path.exists("definitions.rpy") else "game"
rows, audio, other = [], [], []
for d, _, files in os.walk(root):
    if any(x in d for x in ("cache", "saves", "tl")):
        continue
    for f in files:
        p = os.path.join(d, f)
        mb = os.path.getsize(p) / 1048576
        low = f.lower()
        if low.endswith((".webp", ".png", ".jpg", ".jpeg")):
            try:
                w, h = Image.open(p).size
            except Exception:
                continue
            rows.append((w * h * 4 / 1048576, w, h, mb, p))
        elif low.endswith((".ogg", ".mp3", ".opus", ".wav")):
            audio.append((mb, p))
        elif mb > 1:
            other.append((mb, p))

print("== IMAGES: biggest in MEMORY once decoded (RGBA) ==")
for mem, w, h, mb, p in sorted(rows, reverse=True)[:15]:
    flag = "  <-- bigger than 1920x1080" if w > 1920 or h > 1080 else ""
    print(f"{mem:6.1f} MB in RAM | {w}x{h} | {mb:5.2f} MB on disk | {p}{flag}")
print("\n== AUDIO: biggest downloads ==")
for mb, p in sorted(audio, reverse=True)[:10]:
    print(f"{mb:6.2f} MB | {p}")
if other:
    print("\n== OTHER files over 1 MB ==")
    for mb, p in sorted(other, reverse=True)[:10]:
        print(f"{mb:6.2f} MB | {p}")
tot_i = sum(r[3] for r in rows); tot_a = sum(a[0] for a in audio)
print(f"\nTOTAL images {tot_i:.1f} MB | audio {tot_a:.1f} MB | (GitHub rejects any single file over 100 MB)")
