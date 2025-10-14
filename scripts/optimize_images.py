#!/usr/bin/env python3
"""
Optimize all wallpaper images for web delivery.
Usage: python scripts/optimize_images.py
"""

from PIL import Image
import os
from pathlib import Path

WALLPAPER_DIR = Path("wallpapers")
MAX_FULL_SIZE = 1024 * 1024  # 1MB
MAX_THUMB_SIZE = 50 * 1024   # 50KB
FULL_QUALITY = 85
THUMB_QUALITY = 75

def optimize_image(image_path, max_size, quality):
    """Optimize a single image."""
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode != "RGB":
                img = img.convert("RGB")
            
            # Save with optimization
            img.save(image_path, "JPEG", quality=quality, optimize=True, progressive=True)
            
            file_size = os.path.getsize(image_path)
            if file_size > max_size:
                print(f"⚠ {image_path.name} is {file_size / 1024:.1f}KB (exceeds {max_size / 1024:.0f}KB)")
            else:
                print(f"✓ Optimized: {image_path.name} ({file_size / 1024:.1f}KB)")
    except Exception as e:
        print(f"✗ Error optimizing {image_path.name}: {e}")

def main():
    """Optimize all wallpapers."""
    print("Optimizing all wallpaper images...\n")
    
    for category_dir in WALLPAPER_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        
        print(f"Optimizing category: {category_dir.name}")
        image_count = 0
        for image_path in category_dir.glob("*.jpg"):
            if "_thumb" in image_path.name:
                optimize_image(image_path, MAX_THUMB_SIZE, THUMB_QUALITY)
            else:
                optimize_image(image_path, MAX_FULL_SIZE, FULL_QUALITY)
            image_count += 1
        
        if image_count == 0:
            print(f"  No images found in {category_dir.name}")
        print()
    
    print("✓ Image optimization complete!")

if __name__ == "__main__":
    main()
