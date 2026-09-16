# Local Video Audio Transcoder for DaVinci Resolve

A lightweight, multi-threaded Python desktop utility to safely fix phone video audio compatibility issues in DaVinci Resolve (Linux/Windows/Mac). It transcodes audio tracks to uncompressed 16-bit PCM (`pcm_s16le`) while preserving pristine video tracks using zero-copy stream replication (`-c:v copy`).

## Prerequisites

This application requires **FFmpeg** to be installed on your host system.

* **Linux Mint / Ubuntu:** `sudo apt install ffmpeg python3-tk zenity`
* **Windows / Mac:** Ensure `ffmpeg` is added to your system environment variables.

## How to Run

1. Clone this repository or download `converter.py`.
2. Execute the script natively using your Python interpreter:

   ```bash
   python3 converter.py
   ```

## Installation & Uninstallation

To install the application and add it directly to your system app menu:

```bash
chmod +x install.sh
./install.sh
```

To cleanly remove the desktop launcher from your system menu:

```bash
./install.sh --uninstall
```
