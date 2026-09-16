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

## Windows & macOS Manual Setup

Since pre-compiled standalone installers are not yet available, Windows and Mac users can run the application directly using the Python source code.

### 1. Install Prerequisites

Make sure **Python 3** and **FFmpeg** are installed and configured on your system:

* **Windows:** Download Python from the Microsoft Store or Python.org. Install FFmpeg and ensure it is added to your system's Environment Variables (PATH).
* **macOS:** Install Homebrew, then install Python and FFmpeg by running:

```bash
brew install python ffmpeg
```

### 2. Download and Run

1. Download the `converter.py` file from this repository.
2. Open your terminal (macOS) or Command Prompt/PowerShell (Windows) in the directory containing the file.
3. Run the application:

  ```bash
  python converter.py
  ```

On Windows and Mac, the file browser dialogs will automatically open with your native system folder structures and bookmarks intact!
