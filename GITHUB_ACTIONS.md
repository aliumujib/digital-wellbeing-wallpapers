# GitHub Actions Setup

## ✅ Automated Workflows Created

Two GitHub Actions workflows have been set up to automate manifest validation and regeneration.

---

## Workflows

### 1. **Validate and Regenerate** (Main Branch)
**File**: `.github/workflows/validate-and-regenerate.yml`

**Triggers**:
- Push to `main` branch
- Changes to `wallpapers/`, `scripts/`, or `manifest.json`
- Manual trigger

**Actions**:
1. Lists all wallpapers
2. Generates missing thumbnails
3. Regenerates manifest.json
4. Validates everything
5. **Auto-commits changes** if needed

**Result**: Your manifest and thumbnails stay up-to-date automatically! 🎉

---

### 2. **Validate PR** (Pull Requests)
**File**: `.github/workflows/validate-pr.yml`

**Triggers**:
- Pull requests to `main`

**Actions**:
1. Validates manifest structure
2. Checks for missing thumbnails
3. Verifies manifest is current
4. **Fails PR** if validation errors found

**Result**: Prevents merging PRs with missing thumbnails or outdated manifests! ✅

---

## How It Works

### Scenario 1: You Push Wallpapers Directly
```bash
# Add wallpapers
cp ~/Downloads/*.webp wallpapers/default/

# Commit and push (even without running scripts!)
git add wallpapers/
git commit -m "Add new wallpapers"
git push
```

**What happens**:
1. GitHub Action detects changes
2. Generates thumbnails automatically
3. Regenerates manifest automatically
4. Commits changes with message: "🤖 Auto-regenerate manifest and thumbnails"
5. Your repo is updated! ✨

### Scenario 2: Someone Creates a PR
```bash
# Contributor adds wallpapers but forgets thumbnails
git add wallpapers/new_wallpaper.webp
git commit -m "Add wallpaper"
# Creates PR
```

**What happens**:
1. GitHub Action runs validation
2. Detects missing thumbnail
3. **PR fails** with error message
4. Shows: "❌ Missing thumbnail: new_wallpaper_thumb.webp"
5. Contributor fixes and updates PR

---

## Best Practices

### Recommended Workflow (Local First)
```bash
# 1. Add wallpapers
cp ~/Downloads/*.webp wallpapers/default/

# 2. Run local workflow
make workflow

# 3. Commit everything
git add .
git commit -m "Add new wallpapers"

# 4. Push
git push
```

**Why?**: 
- ✅ Faster (no waiting for GitHub Actions)
- ✅ Catch errors locally
- ✅ Review changes before pushing

### Lazy Workflow (Let GitHub Do It)
```bash
# Just push wallpapers
git add wallpapers/
git commit -m "Add wallpapers"
git push

# GitHub Actions will handle the rest!
```

**Why?**: 
- ✅ Quick and easy
- ✅ No local setup needed
- ✅ Still guaranteed to work

---

## Manual Trigger

You can manually run the workflow:

1. Go to **Actions** tab on GitHub
2. Select **"Validate and Regenerate Manifest"**
3. Click **"Run workflow"**
4. Select `main` branch
5. Click **"Run workflow"** button

---

## What Gets Auto-Committed

When the workflow runs, it commits:
- ✅ All generated thumbnails (`*_thumb.webp`)
- ✅ Updated `manifest.json`

**Commit message**: `🤖 Auto-regenerate manifest and thumbnails`

**Author**: `github-actions[bot]`

---

## Workflow Status

You can see workflow status:
- **GitHub repo**: Badge shows pass/fail
- **Actions tab**: Full logs and history
- **PR checks**: Shows validation results
- **Commit status**: Green checkmark when passed

---

## Troubleshooting

### Workflow doesn't trigger
**Check**:
- Changes are in `wallpapers/` folder
- Pushing to `main` branch
- `.github/workflows/` files are committed

### Workflow fails
**Common issues**:
1. **Missing Pillow**: Workflow installs it automatically
2. **Invalid manifest**: Check validation errors in logs
3. **Permission issues**: Ensure `GITHUB_TOKEN` has write access

### Auto-commit not working
**Check**:
- Workflow has write permissions
- Not running on a fork (forks can't auto-commit)
- Changes were actually made

---

## Benefits

✅ **Never forget thumbnails** - Auto-generated  
✅ **Always current manifest** - Auto-regenerated  
✅ **PR validation** - Catches errors early  
✅ **Zero maintenance** - Runs automatically  
✅ **Safety net** - Works even if you forget local scripts  

---

## Example Workflow Output

```
Run python3 scripts/list_wallpapers.py
📁 Wallpaper Repository Structure
wallpapers/
├── default/ (16 wallpapers)
│   ├── boat_river.webp (0.22MB) [thumb: ✓]
│   └── ...
📊 Summary:
   Total wallpapers: 16
   Total size: 1.72MB

Run python3 scripts/generate_thumbnails.py
✓ Thumbnail already exists: boat_river_thumb.webp
✓ Generated thumbnail: new_wallpaper_thumb.webp
✓ Thumbnail generation complete!

Run python3 scripts/generate_manifest.py
✓ Added: boat_river.webp
✓ Added: new_wallpaper.webp
✓ Manifest generated successfully!

Run python3 scripts/validate_manifest.py
✓ Manifest validation successful!

Run git commit
[main abc1234] 🤖 Auto-regenerate manifest and thumbnails
 2 files changed, 15 insertions(+)
 create mode 100644 wallpapers/default/new_wallpaper_thumb.webp
```

---

## Summary

You now have **fully automated** wallpaper management:

1. **Add wallpapers** → Push to GitHub
2. **GitHub Actions** → Auto-generates everything
3. **Manifest updated** → Ready to use!

No manual steps required! 🚀
