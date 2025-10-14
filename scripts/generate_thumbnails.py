#!/usr/bin/env python3
"""
Generate thumbnails for all wallpapers in the repository.
Usage: python scripts/generate_thumbnails.py
"""

from PIL import Image
import os
from pathlib import Path

WALLPAPER_DIR = Path("wallpapers")
THUMBNAIL_SIZE = (200, 356)
THUMBNAIL_QUALITY = 75

def generate_thumbnail(image_path):
    """Generate thumbnail for a single image."""
    if "_thumb" in image_path.name:
        return  # Skip existing thumbnails
    
    thumb_path = image_path.parent / f"{image_path.stem}_thumb{image_path.suffix}"
    
    if thumb_path.exists():
        print(f"✓ Thumbnail already exists: {thumb_path.name}")
        return
    
    try:
        with Image.open(image_path) as img:
            # Convert to RGB if necessary
            if img.mode != "RGB":
                img = img.convert("RGB")
            
            img.thumbnail(THUMBNAIL_SIZE, Image.Resampling.LANCZOS)
            img.save(thumb_path, "JPEG", quality=THUMBNAIL_QUALITY, optimize=True)
            print(f"✓ Generated thumbnail: {thumb_path.name}")
    except Exception as e:
        print(f"✗ Error generating thumbnail for {image_path.name}: {e}")

def main():
    """Generate thumbnails for all wallpapers."""
    print("Generating thumbnails for all wallpapers...\n")
    
    for category_dir in WALLPAPER_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        
        print(f"Processing category: {category_dir.name}")
        image_count = 0
        for image_path in category_dir.glob("*.jpg"):
            generate_thumbnail(image_path)
            image_count += 1
        
        if image_count == 0:
            print(f"  No images found in {category_dir.name}")
        print()
    
    print("✓ Thumbnail generation complete!")

if __name__ == "__main__":
    main()
