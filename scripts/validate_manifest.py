#!/usr/bin/env python3
"""
Validate manifest.json structure and check if all referenced files exist.
Usage: python scripts/validate_manifest.py
"""

import json
from pathlib import Path
import sys

MANIFEST_PATH = Path("manifest.json")
WALLPAPER_DIR = Path("wallpapers")

def validate_manifest():
    """Validate manifest structure and file existence."""
    print("Validating manifest.json...\n")
    
    if not MANIFEST_PATH.exists():
        print("✗ manifest.json not found!")
        return False
    
    try:
        with open(MANIFEST_PATH) as f:
            manifest = json.load(f)
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON in manifest.json: {e}")
        return False
    
    # Check required fields
    required_fields = ["version", "lastUpdated", "baseUrl", "wallpapers"]
    for field in required_fields:
        if field not in manifest:
            print(f"✗ Missing required field: {field}")
            return False
    
    print(f"✓ Manifest version: {manifest['version']}")
    print(f"✓ Last updated: {manifest['lastUpdated']}")
    print(f"✓ Base URL: {manifest['baseUrl']}")
    print(f"✓ Total wallpapers: {len(manifest['wallpapers'])}\n")
    
    if len(manifest['wallpapers']) == 0:
        print("⚠ No wallpapers in manifest (this is OK for initial setup)")
        return True
    
    # Validate each wallpaper entry
    all_valid = True
    for idx, wallpaper in enumerate(manifest["wallpapers"], 1):
        print(f"Validating wallpaper {idx}: {wallpaper.get('id', 'UNKNOWN')}")
        
        # Check required wallpaper fields
        required_wallpaper_fields = [
            "id", "filename", "category", "displayName", 
            "url", "thumbnailUrl", "width", "height", "fileSize"
        ]
        
        missing_fields = [field for field in required_wallpaper_fields if field not in wallpaper]
        if missing_fields:
            print(f"  ✗ Missing fields: {', '.join(missing_fields)}")
            all_valid = False
            continue
        
        # Check if files exist
        category = wallpaper["category"]
        filename = wallpaper["filename"]
        thumb_filename = filename.replace(".jpg", "_thumb.jpg")
        
        full_path = WALLPAPER_DIR / category / filename
        thumb_path = WALLPAPER_DIR / category / thumb_filename
        
        if not full_path.exists():
            print(f"  ✗ File not found: {full_path}")
            all_valid = False
        else:
            file_size = full_path.stat().st_size
            print(f"  ✓ Full size exists: {filename} ({file_size / 1024:.1f}KB)")
        
        if not thumb_path.exists():
            print(f"  ✗ Thumbnail not found: {thumb_path}")
            all_valid = False
        else:
            thumb_size = thumb_path.stat().st_size
            print(f"  ✓ Thumbnail exists: {thumb_filename} ({thumb_size / 1024:.1f}KB)")
        
        print()
    
    if all_valid:
        print("✓ Manifest validation successful!")
        return True
    else:
        print("✗ Manifest validation failed!")
        return False

if __name__ == "__main__":
    success = validate_manifest()
    sys.exit(0 if success else 1)
