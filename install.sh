#!/bin/bash

# Get the absolute path of the directory where this script is located
APP_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
DESKTOP_FILE="$HOME/.local/share/applications/video-transcoder.desktop"

# Check if the user passed the uninstall flag
if [ "$1" == "--uninstall" ]; then
    echo "==========================================="
    echo " Removing Video Audio Transcoder...        "
    echo "==========================================="
    
    if [ -f "$DESKTOP_FILE" ]; then
        rm "$DESKTOP_FILE"
        echo "🗑️  Removed desktop launcher shortcut."
        echo "✨ Uninstallation complete! (Source files remain in your download folder)."
    else
        echo "ℹ️  Launcher shortcut not found. Nothing to remove."
    fi
    echo "==========================================="
    exit 0
fi

# Standard Installation Logic
echo "==========================================="
echo " Installing Video Audio Transcoder...      "
echo "==========================================="

# Check if python3-tk, zenity, and ffmpeg are installed
if ! dpkg -s python3-tk zenity ffmpeg &> /dev/null; then
    echo "📦 Installing system dependencies (requires sudo)..."
    sudo apt update && sudo apt install -y python3-tk zenity ffmpeg
fi

echo "📝 Creating desktop launcher shortcut..."

# Generate the desktop shortcut file dynamically with correct local paths
cat << EOF > "$DESKTOP_FILE"
[Desktop Entry]
StartupWMClass=converter.py
Version=1.0
Type=Application
Name=Video Audio Transcoder
Comment=Fix smartphone video audio tracks for DaVinci Resolve
Exec=python3 $APP_DIR/converter.py
Icon=$APP_DIR/icon.png
Terminal=false
Categories=Utility;AudioVideo;Video;
EOF

# Make the desktop shortcut executable
chmod +x "$DESKTOP_FILE"

echo "✨ Installation complete!"
echo "🚀 You can now find 'Video Audio Transcoder' in your system application menu!"
echo "💡 To remove the shortcut later, run: ./install.sh --uninstall"
echo "==========================================="
