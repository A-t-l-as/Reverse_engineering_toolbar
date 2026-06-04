import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def main():
    # Ukrycie głównego okna Tkinter
    root = tk.Tk()
    root.withdraw()

    # Otwórz okno wyboru katalogu
    katalog = filedialog.askdirectory(title="Wybierz katalog")
    if not katalog:
        print("Nie wybrano katalogu.")
        return

    # Ścieżka do programu (możesz zmienić na pełną, jeśli nie jest w PATH)
    exe_path = "./bin/ParticleTool/MyAod2Particle.exe"

    # Uruchomienie programu z katalogiem jako argumentem
    try:
        subprocess.run([exe_path, katalog], check=True)
        print(f"Uruchomiono: {exe_path} {katalog}")
    except FileNotFoundError:
        print(f"Nie znaleziono programu: {exe_path}")
    except subprocess.CalledProcessError as e:
        print(f"Błąd podczas uruchamiania programu: {e}")

if __name__ == "__main__":
    main()
