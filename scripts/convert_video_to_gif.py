#!/usr/bin/env python3
"""
Convert videos to optimized GIFs for app demonstrations.
Usage: python scripts/convert_video_to_gif.py

This script converts all .mp4 files in the app_gifs directory to optimized GIFs.
Requires: ffmpeg (install via: brew install ffmpeg on macOS)
"""

import subprocess
import os
from pathlib import Path

APP_GIFS_DIR = Path("app_gifs")
OUTPUT_DIR = Path("app_gifs")

# GIF optimization settings
FPS = 15  # Frames per second (lower = smaller file size)
WIDTH = 320  # Width in pixels (height auto-calculated to maintain aspect ratio)
QUALITY = 80  # Quality 1-100 (higher = better quality but larger file)

def check_ffmpeg():
    """Check if ffmpeg is installed."""
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Error: ffmpeg is not installed.")
        print("  Install it with: brew install ffmpeg (macOS) or apt-get install ffmpeg (Linux)")
        return False

def convert_video_to_gif(video_path):
    """Convert a single video file to an optimized GIF."""
    gif_path = video_path.parent / f"{video_path.stem}.gif"
    
    if gif_path.exists():
        print(f"✓ GIF already exists: {gif_path.name}")
        return
    
    print(f"Converting {video_path.name} to GIF...")
    
    try:
        # Two-pass conversion for better quality and smaller file size
        # Pass 1: Generate color palette
        palette_path = video_path.parent / "palette.png"
        palette_cmd = [
            "ffmpeg",
            "-i", str(video_path),
            "-vf", f"fps={FPS},scale={WIDTH}:-1:flags=lanczos,palettegen=stats_mode=diff",
            "-y",
            str(palette_path)
        ]
        
        subprocess.run(palette_cmd, capture_output=True, check=True)
        
        # Pass 2: Create GIF using the palette
        gif_cmd = [
            "ffmpeg",
            "-i", str(video_path),
            "-i", str(palette_path),
            "-lavfi", f"fps={FPS},scale={WIDTH}:-1:flags=lanczos [x]; [x][1:v] paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle",
            "-y",
            str(gif_path)
        ]
        
        subprocess.run(gif_cmd, capture_output=True, check=True)
        
        # Clean up palette file
        palette_path.unlink()
        
        # Get file sizes
        video_size = video_path.stat().st_size / (1024 * 1024)  # MB
        gif_size = gif_path.stat().st_size / (1024 * 1024)  # MB
        
        print(f"✓ Created: {gif_path.name}")
        print(f"  Video size: {video_size:.2f} MB")
        print(f"  GIF size: {gif_size:.2f} MB")
        print(f"  Compression: {(1 - gif_size/video_size) * 100:.1f}%")
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Error converting {video_path.name}: {e}")
        # Clean up partial files
        if gif_path.exists():
            gif_path.unlink()
        if palette_path.exists():
            palette_path.unlink()
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    """Convert all videos in app_gifs directory to GIFs."""
    print("Video to GIF Converter\n")
    print(f"Settings: {FPS} fps, {WIDTH}px width, quality {QUALITY}\n")
    
    if not check_ffmpeg():
        return
    
    if not APP_GIFS_DIR.exists():
        print(f"✗ Error: Directory '{APP_GIFS_DIR}' not found")
        return
    
    # Find all video files
    video_files = list(APP_GIFS_DIR.glob("*.mp4")) + list(APP_GIFS_DIR.glob("*.mov"))
    
    if not video_files:
        print(f"No video files found in {APP_GIFS_DIR}")
        return
    
    print(f"Found {len(video_files)} video file(s)\n")
    
    for video_path in video_files:
        convert_video_to_gif(video_path)
        print()
    
    print("✓ Conversion complete!")

if __name__ == "__main__":
    main()
