import os
import zipfile
import shutil
import tempfile
import tkinter as tk
from tkinter import filedialog, messagebox

def unzip_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def handle_zip_files(directory):
    temp_dir = tempfile.mkdtemp()
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.zip'):
                    file_path = os.path.join(root, file)
                    unzip_target_dir = os.path.join(temp_dir, os.path.basename(file_path).replace('.zip', ''))
                    unzip_file(file_path, unzip_target_dir)
                    shutil.move(unzip_target_dir, root)
                    os.remove(file_path)
        # Recursively handle any new zip files that were extracted
        if any(file.endswith('.zip') for _, _, files in os.walk(directory) for file in files):
            handle_zip_files(directory)
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    directory = filedialog.askdirectory(title="Please select a directory to unzip")
    if not directory:
        print("No directory selected. Exiting.")
        return
    if not os.path.isdir(directory):
        print("Invalid directory. Please provide a valid directory path.")
        return

    handle_zip_files(directory)
    messagebox.showinfo("Information", "All zip files have been unzipped.")

if __name__ == "__main__":
    main()
