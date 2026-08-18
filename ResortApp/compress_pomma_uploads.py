import os
import glob
from PIL import Image

def compress_uploads():
    upload_dir = '/opt/pomma/ResortApp/uploads'
    if not os.path.exists(upload_dir):
        print(f"Directory {upload_dir} not found.")
        return

    compressed = 0
    saved_bytes = 0

    for root, _, files in os.walk(upload_dir):
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in ('.png', '.jpg', '.jpeg', '.webp'):
                filepath = os.path.join(root, f)
                try:
                    orig_size = os.path.getsize(filepath)
                    if orig_size > 300 * 1024:  # Compress if > 300KB
                        with Image.open(filepath) as img:
                            img.thumbnail((1920, 1080), Image.Resampling.LANCZOS)
                            fmt = 'PNG' if ext == '.png' else ('JPEG' if ext in ('.jpg', '.jpeg') else 'WEBP')
                            if fmt == 'JPEG' and img.mode in ('RGBA', 'P'):
                                img = img.convert('RGB')
                            img.save(filepath, fmt, quality=80, optimize=True)
                            new_size = os.path.getsize(filepath)
                            saved_bytes += (orig_size - new_size)
                            compressed += 1
                            print(f"Compressed {f}: {orig_size // 1024}KB -> {new_size // 1024}KB")
                except Exception as e:
                    print(f"Error compressing {f}: {e}")

    print(f"SUCCESS: Compressed {compressed} images, saved {saved_bytes / (1024 * 1024):.2f} MB total bandwidth!")

if __name__ == "__main__":
    compress_uploads()
