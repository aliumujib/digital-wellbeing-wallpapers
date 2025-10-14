# Quick Start Guide

**Naming convention**: `{category}_{description}.jpg`
- Example: `work_minimal_dark.jpg`, `gaming_neon_purple.jpg`

### 2. Generate Thumbnails
```bash
cd digital-wellbeing-wallpapers
python scripts/generate_thumbnails.py
```

This will automatically create `*_thumb.jpg` files for each wallpaper.

### 3. Optimize Images
```bash
python scripts/optimize_images.py
```

This ensures images are compressed and optimized for web delivery.

### 4. Update Manifest
Edit `manifest.json` and add entries for your wallpapers:

```json
{
  "version": 1,
  "lastUpdated": "2025-10-14T06:27:00Z",
  "baseUrl": "https://raw.githubusercontent.com/amjb_apps/digital-wellbeing-wallpapers/main",
  "wallpapers": [
    {
      "id": "work_minimal_dark",
      "filename": "work_minimal_dark.jpg",
      "category": "work",
      "displayName": "Minimal Dark",
      "description": "Clean dark wallpaper for focused work",
      "url": "https://raw.githubusercontent.com/aliumujib/digital-wellbeing-wallpapers/main/wallpapers/work/work_minimal_dark.jpg",
      "thumbnailUrl": "https://raw.githubusercontent.com/aliumujib/digital-wellbeing-wallpapers/main/wallpapers/work/work_minimal_dark_thumb.jpg",
      "width": 1080,
      "height": 1920,
      "fileSize": 524288,
      "tags": ["dark", "minimal", "professional"],
      "author": "Digital Wellbeing Team",
      "license": "CC0"
    }
  ]
}
```

### 5. Validate Everything
```bash
python scripts/validate_manifest.py
```

This checks:
- ✅ Manifest JSON is valid
- ✅ All referenced files exist
- ✅ File sizes are reasonable

### 6. Push to GitHub
```bash
git add .
git commit -m "Add initial wallpaper collection"
git remote add origin https://github.com/aliumujib/digital-wellbeing-wallpapers.git
git push -u origin main
```

## Image Requirements

### Full-Size Wallpapers
- **Resolution**: 1080x1920 (9:16 aspect ratio)
- **Format**: JPEG
- **Quality**: 85-90%
- **Max size**: 1MB
- **Naming**: `{category}_{description}.jpg`

### Thumbnails (auto-generated)
- **Resolution**: 200x356 (9:16 aspect ratio)
- **Format**: JPEG
- **Quality**: 75-80%
- **Max size**: 50KB
- **Naming**: `{category}_{description}_thumb.jpg`

## Recommended Starting Collection

### Work (3 wallpapers)
- Minimal dark background
- Calming blue gradient
- Clean geometric pattern

### Personal (2 wallpapers)
- Vibrant abstract colors
- Warm sunset gradient

### Gaming (2 wallpapers)
- Neon purple cyberpunk
- Dark with neon accents

### Minimal (2 wallpapers)
- Pure black (OLED-friendly)
- Neutral grey

### Default (1 wallpaper)
- Neutral gradient

## Testing Locally

Start a local server to test:
```bash
python -m http.server 8000
```

Then access manifest at:
```
http://localhost:8000/manifest.json
```

## GitHub Repository URL

Once pushed, your wallpapers will be accessible at:
```
https://raw.githubusercontent.com/aliumujib/digital-wellbeing-wallpapers/main/manifest.json
```

## Troubleshooting

### Python Scripts Not Working?
Install Pillow:
```bash
pip install Pillow
```

### Git LFS Issues?
Install Git LFS:
```bash
brew install git-lfs  # macOS
git lfs install
```

### Thumbnails Not Generating?
Check that:
1. Images are in correct format (JPEG)
2. Images are in category folders
3. Pillow is installed

## What's Already Set Up

✅ Directory structure created  
✅ Git repository initialized  
✅ Git LFS configured for images  
✅ Python scripts created and executable  
✅ README.md with documentation  
✅ LICENSE file (CC0)  
✅ manifest.json template  
✅ .gitignore for common files  

## Ready to Go! 🚀

Just add your wallpapers and run the scripts!
