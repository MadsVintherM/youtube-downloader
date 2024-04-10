# YouTube Downloader Script

## Overview
This project includes a Python script that utilizes the `pytube` library to download videos from YouTube through the command line, displaying the download progress. For Windows users, a Batch file is provided to simplify usage by allowing video links to be inputted directly after a double-click on the file.

## Prerequisites
- Python 3.x
- `pytube` library, installable via pip:
      pip install pytube


## Files
- **ytdl.py**: The Python script for downloading YouTube videos.
- **download_youtube_video.bat**: For Windows users, a Batch file to run the script with a simple UI for link input.

## Setup
1. Clone or download the repository to your machine.
2. Install Python and the `pytube` library if you haven't already.
3. Place `ytdl.py` and `download_youtube_video.bat` in your preferred download directory.

## Usage

### Windows Users
1. Edit `download_youtube_video.bat` by right-clicking and selecting "Edit". Replace `C:\path\to\ytdl.py` with the full path to where `ytdl.py` is saved.
2. Save and close the editor.
3. Double-click `download_youtube_video.bat`, input the YouTube video link when prompted, and press Enter.
4. The video will be downloaded to the directory specified in `ytdl.py`, with progress shown in the command window.

### Command Line Users
1. Open a terminal or command prompt.
2. Navigate to the directory containing `ytdl.py`.
3. Execute the script with the YouTube video URL as an argument:
 ```bash
 python ytdl.py "https://www.youtube.com/watch?v=VIDEO_ID"

Replace VIDEO_ID with the actual YouTube video ID.

Customizing Download Location
To change where videos are downloaded, edit the ytdl.py script and modify the path in the yd.download('/path/to/directory') function to your desired location.

Notes
Downloads the highest available resolution of the video.
Shows download progress in the command line.
Troubleshooting
If there are issues with pytube, ensure you have the latest version installed. PyTube is frequently updated to fix bugs and issues.

Contributing
Contributions to improve the script or fix issues are welcome. Please fork the repository and submit a pull request with your changes.
