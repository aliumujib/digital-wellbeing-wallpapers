# GitHub Actions Workflows

## Workflows

### 1. `validate-and-regenerate.yml` (Main Branch)

**Triggers**: 
- Push to `main` branch
- Changes to `wallpapers/`, `scripts/`, or `manifest.json`
- Manual trigger via workflow_dispatch

**What it does**:
1. ✅ Lists all wallpapers
2. 🖼️  Generates missing thumbnails
3. 📝 Regenerates manifest.json
4. ✅ Validates manifest
5. 🤖 Auto-commits changes if needed

**Use case**: Automatically keeps manifest up-to-date when you push wallpapers directly to main.

---

### 2. `validate-pr.yml` (Pull Requests)

**Triggers**: 
- Pull requests to `main` branch

**What it does**:
1. ✅ Validates manifest structure
2. 🔍 Checks for missing thumbnails
3. 🔍 Verifies manifest is up-to-date
4. ❌ Fails if validation errors found

**Use case**: Ensures PRs have proper thumbnails and updated manifest before merging.

---

## Workflow Behavior

### On Push to Main
```
Push wallpapers → Workflow runs → Auto-generates thumbnails & manifest → Commits changes
```

### On Pull Request
```
Create PR → Workflow validates → Shows errors if any → Merge when green ✅
```

---

## Manual Trigger

You can manually trigger the regeneration workflow:

1. Go to **Actions** tab in GitHub
2. Select **"Validate and Regenerate Manifest"**
3. Click **"Run workflow"**
4. Select branch and click **"Run workflow"**

---

## What Gets Auto-Generated

- ✅ Thumbnails (`*_thumb.webp`)
- ✅ manifest.json (complete regeneration)
- ✅ Automatic commit with message: "🤖 Auto-regenerate manifest and thumbnails"

---

## Local Development

You should still run locally before pushing:

```bash
make workflow    # Generate everything locally
git add .
git commit -m "Add new wallpapers"
git push
```

The GitHub Action is a **safety net** that ensures everything stays in sync even if you forget to run the scripts locally.

---

## Troubleshooting

### Workflow fails with "Missing thumbnails"
**Solution**: Run `make thumbnails` locally and commit

### Workflow fails with "Manifest out of date"
**Solution**: Run `make manifest` locally and commit

### Workflow doesn't trigger
**Check**: 
- Changes are in `wallpapers/` folder
- Pushing to `main` branch
- Workflow file is in `.github/workflows/`

---

## Benefits

✅ **Never forget to generate thumbnails** - Auto-generated on push  
✅ **Always up-to-date manifest** - Auto-regenerated on push  
✅ **PR validation** - Catches errors before merge  
✅ **Automatic commits** - No manual intervention needed  
✅ **Workflow summary** - See results in GitHub Actions UI  

---

## Example Workflow Run

```
📋 Current wallpapers:
   Total wallpapers: 16
   Total size: 1.72MB

🖼️  Generating thumbnails...
   ✓ Generated 16 thumbnails

📝 Regenerating manifest...
   ✓ Manifest generated successfully!

✅ Validating manifest...
   ✓ Manifest validation successful!

🤖 Auto-committing changes...
   ✓ Changes committed and pushed
```
