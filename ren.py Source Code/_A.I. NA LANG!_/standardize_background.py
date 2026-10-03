from PIL import Image
import os

TARGET_W, TARGET_H = 1920, 1080
BG_DIR = "game/images/backgrounds"

for fname in os.listdir(BG_DIR):
    if not fname.endswith(".webp"):
        continue

    path = os.path.join(BG_DIR, fname)
    img = Image.open(path).convert("RGB")  
    w, h = img.size

    if (w, h) == (TARGET_W, TARGET_H):
        print(f"OK, already correct: {fname}")
        continue

    scale = max(TARGET_W / w, TARGET_H / h)
    new_w = int(w * scale + 0.5)
    new_h = int(h * scale + 0.5)
    resized = img.resize((new_w, new_h), Image.LANCZOS)

    ## Center-crop down to exactly the target size
    left = (new_w - TARGET_W) // 2
    top = (new_h - TARGET_H) // 2
    cropped = resized.crop((left, top, left + TARGET_W, top + TARGET_H))

    cropped.save(path, "webp")
    print(f"Standardized: {fname}  ({w}x{h} -> {TARGET_W}x{TARGET_H}, cropped)")

print("\nDone. All backgrounds now share one canvas size, filled edge-to-edge.")