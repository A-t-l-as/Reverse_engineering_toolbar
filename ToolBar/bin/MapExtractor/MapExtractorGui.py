import os
import shutil
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

# Set the path to MapConverter here
MAPCONVERTER_DIR = Path(r"PATH\TO\DIRECTORY\MapExtractor")

def process_file(file_path):
    file_path = Path(file_path).resolve()
    
    if not file_path.exists():
        messagebox.showerror("Error", f"Plik {file_path} nie istnieje.")
        return
    
    if not (MAPCONVERTER_DIR / "MapExtractor.exe").exists():
        messagebox.showerror("Error", f"MapExtractor.exe was not found in the {MAPCONVERTER_DIR} directory.")
        return
    
    try:
        # Step 1: Copy the file
        copied_file = MAPCONVERTER_DIR / file_path.name
        shutil.copy(file_path, copied_file)
        
        # Step 2: Run MapExtractor.exe
        subprocess.run(
            [str(MAPCONVERTER_DIR / "MapExtractor.exe"), copied_file.name],
            cwd=MAPCONVERTER_DIR,
            check=True
        )
        
        # Step 3: Moving the output directory
        output_dir_name = file_path.stem + "_" + file_path.suffix.lstrip(".")
        output_dir = MAPCONVERTER_DIR / output_dir_name
        target_dir = file_path.parent / output_dir_name
        
        if not output_dir.exists():
            messagebox.showerror("Error", f"The directory {output_dir} was not found.")
            return
        
        if target_dir.exists():
            shutil.rmtree(target_dir)
        
        shutil.move(str(output_dir), str(target_dir))
        messagebox.showinfo("Success", f"The directory has been moved to:\n{target_dir}")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select the file to process",
        filetypes=[("All files", "*.*")]
    )
    if file_path:
        process_file(file_path)

# GUI
root = tk.Tk()
root.title("MapExtractor GUI")
root.geometry("300x150")

label = tk.Label(root, text="Click to select a file:")
label.pack(pady=10)

button = tk.Button(root, text="Select file", command=select_file)
button.pack(pady=10)

root.mainloop()
