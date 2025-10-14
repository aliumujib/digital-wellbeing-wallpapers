.PHONY: all list thumbnails manifest validate optimize clean help

# Default target
all: list thumbnails manifest validate

# List all wallpapers in tree format
list:
	@echo "📋 Listing wallpapers..."
	@python3 scripts/list_wallpapers.py

# Generate thumbnails for all wallpapers
thumbnails:
	@echo "🖼️  Generating thumbnails..."
	@python3 scripts/generate_thumbnails.py

# Generate manifest.json from folder structure
manifest:
	@echo "📝 Generating manifest..."
	@python3 scripts/generate_manifest.py

# Validate manifest and check files
validate:
	@echo "✅ Validating manifest..."
	@python3 scripts/validate_manifest.py

# Optimize all images
optimize:
	@echo "⚡ Optimizing images..."
	@python3 scripts/optimize_images.py

# Clean all generated thumbnails
clean:
	@echo "🧹 Cleaning thumbnails..."
	@find wallpapers -name "*_thumb.*" -type f -delete
	@echo "✓ All thumbnails removed"

# Full workflow: list, generate, validate
workflow: list thumbnails manifest validate
	@echo ""
	@echo "✨ Workflow complete!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Review the generated manifest.json"
	@echo "  2. Run 'make optimize' if needed"
	@echo "  3. Commit and push to GitHub"
	@echo ""

# Quick workflow without listing
quick: thumbnails manifest validate
	@echo "✨ Quick workflow complete!"

# Help
help:
	@echo "Digital Wellbeing Wallpapers - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  make all        - Run full workflow (list + thumbnails + manifest + validate)"
	@echo "  make workflow   - Same as 'all' with summary"
	@echo "  make quick      - Quick workflow (skip listing)"
	@echo "  make list       - List all wallpapers in tree format"
	@echo "  make thumbnails - Generate thumbnails for all wallpapers"
	@echo "  make manifest   - Generate manifest.json from folder structure"
	@echo "  make validate   - Validate manifest and check files"
	@echo "  make optimize   - Optimize all images (compress)"
	@echo "  make clean      - Remove all generated thumbnails"
	@echo "  make help       - Show this help message"
	@echo ""
	@echo "Typical workflow:"
	@echo "  1. Add wallpapers to category folders"
	@echo "  2. Run 'make workflow'"
	@echo "  3. Review manifest.json"
	@echo "  4. Commit and push"
	@echo ""
