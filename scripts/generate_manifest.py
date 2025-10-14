#!/usr/bin/env python3
"""
Generate manifest.json from wallpaper folder structure.
Usage: python scripts/generate_manifest.py
"""

import json
from pathlib import Path
from datetime import datetime
import os

WALLPAPER_DIR = Path("wallpapers")
MANIFEST_PATH = Path("manifest.json")
BASE_URL = "https://raw.githubusercontent.com/aliumujib/digital-wellbeing-wallpapers/main"
SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png", ".webp"}

def generate_display_name(filename):
    """Generate a human-readable display name from filename."""
    # Remove extension and replace underscores with spaces
    name = Path(filename).stem
    # Capitalize each word
    return " ".join(word.capitalize() for word in name.split("_"))

def generate_description(filename, category):
    """Generate a description based on filename and category."""
    name = Path(filename).stem.lower()
    
    # Category-specific descriptions
    if category == "work":
        return f"Professional wallpaper for focused work sessions"
    elif category == "personal":
        return f"Vibrant wallpaper for personal time"
    elif category == "gaming":
        return f"Energetic wallpaper for gaming sessions"
    elif category == "minimal":
        return f"Clean, distraction-free wallpaper"
    elif category == "default":
        # Try to generate description from filename
        if "desert" in name or "dune" in name:
            return "Serene desert landscape"
        elif "ocean" in name or "tide" in name or "wave" in name:
            return "Calming ocean scene"
        elif "tree" in name or "forest" in name:
            return "Natural landscape with trees"
        elif "mountain" in name or "hill" in name:
            return "Peaceful mountain vista"
        elif "river" in name or "boat" in name:
            return "Tranquil water scene"
        elif "zen" in name or "garden" in name:
            return "Zen-inspired peaceful scene"
        elif "drift" in name or "flow" in name:
            return "Abstract flowing design"
        elif "stellar" in name or "star" in name:
            return "Cosmic starry scene"
        elif "sunrise" in name or "sunset" in name or "sunlit" in name:
            return "Beautiful sunrise/sunset scene"
        elif "crane" in name or "bird" in name:
            return "Elegant wildlife scene"
        elif "mist" in name or "fog" in name:
            return "Misty atmospheric scene"
        else:
            return "Beautiful natural wallpaper"
    
    return f"Beautiful {category} wallpaper"

def extract_tags(filename, category):
    """Extract relevant tags from filename."""
    name = Path(filename).stem.lower()
    tags = [category]
    
    # Common tag keywords
    tag_keywords = {
        "dark": "dark",
        "light": "light",
        "minimal": "minimal",
        "abstract": "abstract",
        "nature": "nature",
        "ocean": "ocean",
        "desert": "desert",
        "mountain": "mountain",
        "tree": "tree",
        "forest": "forest",
        "water": "water",
        "sky": "sky",
        "sunset": "sunset",
        "sunrise": "sunrise",
        "zen": "zen",
        "calm": "calm",
        "peaceful": "peaceful",
        "gradient": "gradient",
        "colorful": "colorful",
        "blue": "blue",
        "green": "green",
        "orange": "orange",
        "purple": "purple",
        "neon": "neon",
    }
    
    for keyword, tag in tag_keywords.items():
        if keyword in name:
            tags.append(tag)
    
    return tags

def get_image_dimensions(image_path):
    """Get image dimensions. Returns (width, height) or (1080, 1920) as default."""
    try:
        from PIL import Image
        with Image.open(image_path) as img:
            return img.size
    except ImportError:
        print("⚠ PIL not installed, using default dimensions (1080x1920)")
        return (1080, 1920)
    except Exception as e:
        print(f"⚠ Could not read dimensions for {image_path.name}: {e}")
        return (1080, 1920)

def generate_manifest():
    """Generate manifest.json from folder structure."""
    print("Generating manifest.json from wallpaper folder structure...\n")
    
    wallpapers = []
    
    for category_dir in sorted(WALLPAPER_DIR.iterdir()):
        if not category_dir.is_dir():
            continue
        
        category = category_dir.name
        print(f"Processing category: {category}")
        
        # Get all image files (excluding thumbnails)
        images = [
            f for f in sorted(category_dir.iterdir())
            if f.is_file() and f.suffix.lower() in SUPPORTED_FORMATS and "_thumb" not in f.name
        ]
        
        for image in images:
            # Check if thumbnail exists
            thumb_name = f"{image.stem}_thumb{image.suffix}"
            thumb_path = image.parent / thumb_name
            
            if not thumb_path.exists():
                print(f"  ⚠ Missing thumbnail for {image.name}")
            
            # Get file info
            file_size = image.stat().st_size
            width, height = get_image_dimensions(image)
            
            # Generate wallpaper entry
            wallpaper_id = f"{category}_{image.stem}"
            wallpaper_entry = {
                "id": wallpaper_id,
                "filename": image.name,
                "category": category,
                "displayName": generate_display_name(image.name),
                "description": generate_description(image.name, category),
                "url": f"{BASE_URL}/wallpapers/{category}/{image.name}",
                "thumbnailUrl": f"{BASE_URL}/wallpapers/{category}/{thumb_name}",
                "width": width,
                "height": height,
                "fileSize": file_size,
                "tags": extract_tags(image.name, category),
                "author": "Abdulmujeeb Aliu",
                "license": "CC0"
            }
            
            wallpapers.append(wallpaper_entry)
            print(f"  ✓ Added: {image.name}")
        
        print()
    
    # Create manifest
    manifest = {
        "version": 1,
        "lastUpdated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "baseUrl": BASE_URL,
        "wallpapers": wallpapers
    }
    
    # Write manifest
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✓ Manifest generated successfully!")
    print(f"  Total wallpapers: {len(wallpapers)}")
    print(f"  Output: {MANIFEST_PATH}\n")

if __name__ == "__main__":
    generate_manifest()
