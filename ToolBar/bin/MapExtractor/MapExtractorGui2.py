import os
import shutil
import subprocess
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Path to MapConverter (hardcoded)
MAPCONVERTER_PATH = r"PATH\TO\DIRECTORY\MapExtractor"  # <- change to your own

def main():
    #1. Selecting a file via the GUI
    Tk().withdraw()  # Hides the main Tkinter window
    file_path = askopenfilename(title="Select the file to convert")
    if not file_path:
        print("No file has been selected.")
        return

    # 2. Copying the file to the MapConverter directory
    file_name = os.path.basename(file_path)
    dest_path = os.path.join(MAPCONVERTER_PATH, file_name)
    shutil.copy(file_path, dest_path)
    print(f"{file_name} has been copied to {MAPCONVERTER_PATH}")

    # 3. Run MapExtractor in the MapConverter directory
    extractor_path = os.path.join(MAPCONVERTER_PATH, "MapExtractor.exe")
    subprocess.run([extractor_path, file_name], cwd=MAPCONVERTER_PATH, check=True)
    print(f"MapExtractor has been launched on {file_name}")

    # 4. Move the generated directory next to the original file
    base_name, ext = os.path.splitext(file_name)
    generated_dir = f"{base_name}_{ext.lstrip('.')}"
    generated_dir_path = os.path.join(MAPCONVERTER_PATH, generated_dir)
    target_dir_path = os.path.join(os.path.dirname(file_path), generated_dir)

    if os.path.exists(generated_dir_path):
        shutil.move(generated_dir_path, target_dir_path)
        print(f"{generated_dir} has been moved to {target_dir_path}")
    else:
        print(f"The generated directory could not be found: {generated_dir_path}")

if __name__ == "__main__":
    main()
