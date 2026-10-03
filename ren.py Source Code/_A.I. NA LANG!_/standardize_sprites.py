from PIL import Image
import os

TARGET_W, TARGET_H = 1500, 3000
SPRITE_DIR = "game/images/sprites"

for fname in os.listdir(SPRITE_DIR):
    if not fname.endswith(".webp"):
        continue

    path = os.path.join(SPRITE_DIR, fname)
    img = Image.open(path).convert("RGBA")
    w, h = img.size

    if (w, h) == (TARGET_W, TARGET_H):
        print(f"OK, already correct: {fname}")
        continue
    scale = min(TARGET_W / w, TARGET_H / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    resized = img.resize((new_w, new_h), Image.LANCZOS)

    canvas = Image.new("RGBA", (TARGET_W, TARGET_H), (0, 0, 0, 0))
    paste_x = (TARGET_W - new_w) // 2
    paste_y = TARGET_H - new_h
    canvas.paste(resized, (paste_x, paste_y), resized)

    canvas.save(path, "webp")
    print(f"Standardized: {fname}  ({w}x{h} -> {TARGET_W}x{TARGET_H})")

print("\nDone. All sprites now share one canvas size.")