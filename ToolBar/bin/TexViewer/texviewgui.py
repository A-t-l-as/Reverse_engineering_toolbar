import sys
import shutil
import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def main():

    root = tk.Tk()
    root.withdraw()  # Ukrywa główne okno
    zrodlo = filedialog.askopenfilename(title="Select file")
    if zrodlo:
        print("Selected path:", zrodlo)
    else:
        print("No file selected.")
        return
    
    katalog_docelowy = r"PATH\TO\DIRECTORY\TexViewer"
    plik_docelowy = os.path.join(katalog_docelowy, "bufor.bin")

    # Kopiowanie pliku
    try:
        shutil.copy2(zrodlo, plik_docelowy)
        print(f"File copied to {plik_docelowy}")
    except Exception as e:
        print(f"Error copying file: {e}")
        return

    # Odczyt i ewentualna modyfikacja 12. bajtu
    try:
        with open(plik_docelowy, "rb+") as f:
            f.seek(11)  # 12. bajt = offset 11 (liczenie od 0)
            bajt = f.read(1)
            if bajt == b'\x10':
                f.seek(11)
                f.write(b'\x80')
                print("The 12th byte has been changed from 0x10 to 0x80.")
            else:
                print(f"The 12th byte is not equal to 0x10 (it is: {bajt.hex()})")
    except Exception as e:
        print(f"Error when modifying the file: {e}")
        return

    # Uruchomienie programu Texviewer_inside.exe z argumentem bufor.bin
    try:
        subprocess.run(
            [os.path.join(katalog_docelowy, "Texviewer_inside.exe"), "bufor.bin"],
            cwd=katalog_docelowy
        )
        print("The Texviewer_inside.exe program has been launched.")
    except Exception as e:
        print(f"Error when starting the program: {e}")

if __name__ == "__main__":
    main()
