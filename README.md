# Digital Wellbeing Wallpapers

Curated wallpaper collection for the Digital Wellbeing Focus Modes launcher.

## Categories
- **Work**: Professional, minimal designs for focused work
- **Personal**: Colorful, vibrant wallpapers for personal time
- **Gaming**: Energetic, neon designs for gaming sessions
- **Minimal**: Clean, distraction-free wallpapers
- **Default**: General-purpose wallpapers

## Usage
This repository is consumed by the Digital Wellbeing launcher app. Wallpapers are served via GitHub Raw URLs.

### Manifest URL
```
https://raw.githubusercontent.com/amjb_apps/digital-wellbeing-wallpapers/main/manifest.json
```

## Contributing
1. Add wallpapers to appropriate category folder
2. Generate thumbnails using `scripts/generate_thumbnails.py`
3. Update `manifest.json` with new wallpaper metadata
4. Validate manifest using `scripts/validate_manifest.py`
5. Submit pull request

## Image Specifications
- **Full size**: 1080x1920 (max 1MB)
- **Thumbnails**: 200x356 (max 50KB)
- **Format**: JPEG (progressive)
- **Quality**: 85-90% (full), 75-80% (thumbnails)

## Workflow for Adding Wallpapers

### 1. Add Wallpaper to Category Folder
```bash
# Copy your wallpaper to the appropriate category
cp ~/Downloads/my_wallpaper.jpg wallpapers/work/work_new_design.jpg
```

### 2. Generate Thumbnail
```bash
python scripts/generate_thumbnails.py
```

### 3. Optimize Images
```bash
python scripts/optimize_images.py
```

### 4. Update Manifest
Edit `manifest.json` and add your wallpaper entry:
```json
{
  "id": "work_new_design",
  "filename": "work_new_design.jpg",
  "category": "work",
  "displayName": "New Design",
  "description": "Description of the wallpaper",
  "url": "https://raw.githubusercontent.com/amjb_apps/digital-wellbeing-wallpapers/main/wallpapers/work/work_new_design.jpg",
  "thumbnailUrl": "https://raw.githubusercontent.com/amjb_apps/digital-wellbeing-wallpapers/main/wallpapers/work/work_new_design_thumb.jpg",
  "width": 1080,
  "height": 1920,
  "fileSize": 524288,
  "tags": ["tag1", "tag2"],
  "author": "Digital Wellbeing Team",
  "license": "CC0"
}
```

### 5. Validate
```bash
python scripts/validate_manifest.py
```

### 6. Commit
```bash
git add .
git commit -m "Add new work wallpaper: work_new_design"
git push origin main
```

## License
All wallpapers are licensed under CC0 (Public Domain) unless otherwise specified.
