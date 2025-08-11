# Relative Frame Display

A Blender addon that displays the current frame number relative to the start of the timeline playback range directly in the 3D viewport.

**Author:** Eaxum  
**Version:** 1.2  
**Compatible with:** Blender 4.0+

## Features

- **Real-time display** of relative frame numbers in the 3D viewport
- **Clean, professional styling** with subtle transparency
- **Easy toggle** via Animation panel or View menu
- **Bottom-left positioning** that doesn't interfere with your work
- **Shows both relative and absolute frame information**

## Installation

### Method 1: Install from Zip Package (Recommended)
1. Download the addon as a zip file (containing `__init__.py` and other files)
2. Open Blender
3. Go to **Edit > Preferences > Add-ons**
4. Click **Install...** button
5. Navigate to and select the zip file
6. Click **Install Add-on**
7. Enable the addon by checking the box next to "Animation: Relative Frame Display"

### Method 2: Install Single Python File
1. Download the `relative_frame_display.py` file
2. Open Blender
3. Go to **Edit > Preferences > Add-ons**
4. Click **Install...** button
5. Navigate to and select the `relative_frame_display.py` file
6. Click **Install Add-on**
7. Enable the addon by checking the box next to "Animation: Relative Frame Display"

### Method 3: Manual Installation
1. Download the addon files
2. Copy them to your Blender addons folder:
   - **Windows:** `%APPDATA%\Blender Foundation\Blender\4.x\scripts\addons\relative_frame_display\`
   - **macOS:** `~/Library/Application Support/Blender/4.x/scripts/addons/relative_frame_display/`
   - **Linux:** `~/.config/blender/4.x/scripts/addons/relative_frame_display/`
3. Restart Blender
4. Go to **Edit > Preferences > Add-ons**
5. Search for "Relative Frame Display"
6. Enable the addon by checking the box

## Usage

### Enabling the Display
- **Via Panel:** Open the Animation panel in the 3D viewport sidebar (N key) and click "Show Viewport Display"
- **Via Menu:** Go to **View > Toggle Relative Frame Display** in the 3D viewport

### What You'll See
The addon displays two lines of text in the bottom-left corner of your 3D viewport:
- **Main text:** "Relative Frame: X" (white, larger font)
- **Secondary text:** "Current: Y / Start: Z" (gray, smaller font)

### Example
If your timeline starts at frame 100 and you're currently on frame 105:
```
Relative Frame: 6
Current: 105 / Start: 100
```

## Use Cases

Perfect for animators who want to know their position relative to animation sequences:
- **Character animation cycles**
- **Keyframe timing relative to action start**
- **Scene planning and storyboarding**
- **Animation reviews and timing adjustments**

## Uninstalling

1. Go to **Edit > Preferences > Add-ons**
2. Search for "Relative Frame Display"
3. Click the arrow to expand the addon details
4. Click **Remove** button
5. Restart Blender

## Support

This addon is provided as-is for the Blender community. If you encounter issues, please check that you're using Blender 4.0 or newer.

## License

This addon is released under the GPL v3 license, same as Blender itself.
