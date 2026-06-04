import os
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog

def main():
    # Hide the main Tkinter window
    root = tk.Tk()
    root.withdraw()

    # Wybór pliku .aod
    file_path = filedialog.askopenfilename(
        title="Select the .aod file",
        filetypes=[("AOD files", "*.aod")]
    )
    
    if not file_path:
        print("No file has been selected.")
        return

    # Paths
    file_name = os.path.basename(file_path)
    source_dir = os.path.dirname(file_path)
    work_dir = r"PATH/TO/Aod2Msh_2003_KnightShift"
    exe_path = os.path.join(work_dir, "Aod2msh.exe")

    if not os.path.exists(work_dir):
        print(f"No catalog: {work_dir}")
        return

    if not os.path.exists(exe_path):
        print(f"No program: {exe_path}")
        return

    # Move the .aod file to the working directory
    dest_aod = os.path.join(work_dir, file_name)
    shutil.move(file_path, dest_aod)
    print(f"Przeniesiono {file_name} do {work_dir}")

    # Run the Aod2msh.exe program and wait for it to finish.
    print("Starting Aod2msh.exe...")
    subprocess.run([exe_path, file_name], cwd=work_dir, check=True)

    # Path to the generated .msh
    msh_file = os.path.splitext(file_name)[0] + ".msh"
    msh_path = os.path.join(work_dir, msh_file)

    if not os.path.exists(msh_path):
        print("The .msh file was not generated.")
        return

    # Transferring files back
    shutil.move(dest_aod, os.path.join(source_dir, file_name))
    shutil.move(msh_path, os.path.join(source_dir, msh_file))

    print(f"Done! The files {file_name} and {msh_file} have been moved to {source_dir}.")

if __name__ == "__main__":
    main()
