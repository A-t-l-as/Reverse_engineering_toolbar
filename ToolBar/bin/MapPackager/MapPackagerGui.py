import os
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog

# Path to the MapConverter directory (hardcoded)
MAPCONVERTER_PATH = r"PATH\TO\DIRECTORY\MapPackager"

def main():
    root = tk.Tk()
    root.withdraw()
    source_dir = filedialog.askdirectory(title="Select the directory to pack")
    if not source_dir:
        print("No directory selected.")
        return

    # Name of the directory and output file
    dir_name = os.path.basename(source_dir)
    if "_" in dir_name:
        parts = dir_name.rsplit("_", 1)  # only the last “_”
        output_file_name = f"{parts[0]}.{parts[1]}"
    else:
        output_file_name = dir_name  # fallback

    # Target path in the MapConverter directory
    dest_dir = os.path.join(MAPCONVERTER_PATH, dir_name)

    # Copying a directory
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(source_dir, dest_dir)
    print(f"The directory has been copied to {dest_dir}.")

    # Calling MapPackager.exe
    map_packager_exe = os.path.join(MAPCONVERTER_PATH, "MapPackager.exe")
    subprocess.run([map_packager_exe, dir_name], cwd=MAPCONVERTER_PATH)
    print("MapPackager has been launched.")

    # Moving the output file next to the source directory
    generated_file = os.path.join(MAPCONVERTER_PATH, output_file_name)
    if os.path.exists(generated_file):
        shutil.move(generated_file, os.path.join(os.path.dirname(source_dir), output_file_name))
        print(f"The output file has been moved to {os.path.dirname(source_dir)}")
    else:
        print(f"The generated file was not found: {generated_file}")

if __name__ == "__main__":
    main()
