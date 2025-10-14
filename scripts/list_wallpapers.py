#!/usr/bin/env python3
"""
List all wallpapers in a tree format.
Usage: python scripts/list_wallpapers.py
"""

from pathlib import Path

WALLPAPER_DIR = Path("wallpapers")
SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png", ".webp"}

def list_wallpapers():
    """List all wallpapers in tree format."""
    print("\n📁 Wallpaper Repository Structure\n")
    print("wallpapers/")
    
    total_count = 0
    total_size = 0
    
    for category_dir in sorted(WALLPAPER_DIR.iterdir()):
        if not category_dir.is_dir():
            continue
        
        # Get all image files
        images = [
            f for f in sorted(category_dir.iterdir())
            if f.is_file() and f.suffix.lower() in SUPPORTED_FORMATS and "_thumb" not in f.name
        ]
        
        if not images:
            print(f"├── {category_dir.name}/ (empty)")
            continue
        
        print(f"├── {category_dir.name}/ ({len(images)} wallpapers)")
        
        category_size = 0
        for idx, image in enumerate(images):
            is_last = idx == len(images) - 1
            prefix = "└──" if is_last else "├──"
            
            file_size = image.stat().st_size
            category_size += file_size
            size_mb = file_size / (1024 * 1024)
            
            # Check if thumbnail exists
            thumb_name = f"{image.stem}_thumb{image.suffix}"
            thumb_path = image.parent / thumb_name
            thumb_status = "✓" if thumb_path.exists() else "✗"
            
            print(f"│   {prefix} {image.name} ({size_mb:.2f}MB) [thumb: {thumb_status}]")
        
        total_count += len(images)
        total_size += category_size
        print(f"│       Subtotal: {category_size / (1024 * 1024):.2f}MB")
        print("│")
    
    print(f"\n📊 Summary:")
    print(f"   Total wallpapers: {total_count}")
    print(f"   Total size: {total_size / (1024 * 1024):.2f}MB")
    print(f"   Average size: {(total_size / total_count) / (1024 * 1024):.2f}MB per wallpaper\n")

if __name__ == "__main__":
    list_wallpapers()
