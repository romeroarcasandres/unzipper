# Unzipper

This script unzips all .zip files in a selected directory, recursively handling any newly extracted .zip files within the directory.

## Overview

The `Unzipper.py` script processes a given directory to find and extract all .zip files within it. It handles nested zip files by recursively searching and extracting until no zip files remain. The extracted contents are placed in the same directory as their respective zip files, and the original zip files are removed after extraction.

## Requirements

- Python 3
- `os` library (for file and directory operations)
- `zipfile` library (for handling zip files)
- `shutil` library (for file operations)
- `tempfile` library (for creating temporary directories)
- `tkinter` library (for file dialog and message boxes)

## Files

- `Unzip_Utility.py`

## Usage

1. Run the script.
2. A file dialog will prompt you to select a directory containing zip files.
3. After selecting the directory, the script will recursively find and extract all zip files within the selected directory.
4. A message box will notify you when all zip files have been successfully unzipped.

## Important Note

Ensure that the selected directory contains valid .zip files.
The script removes the original .zip files after extraction.
The extracted files will be placed in the same directory as the original .zip files.

## License
This project is governed by the CC BY-NC 4.0 license. For comprehensive details, kindly refer to the LICENSE file included with this project.
