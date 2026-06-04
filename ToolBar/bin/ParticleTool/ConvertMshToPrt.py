import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def main():
    # Utwórz ukryte okno tkinter do wyboru pliku
    root = tk.Tk()
    root.withdraw()

    # Wybierz plik wejściowy
    file_path = filedialog.askopenfilename(
        title="Wybierz plik wejściowy",
        filetypes=[("Wszystkie pliki", "*.*")]
    )

    if not file_path:
        messagebox.showinfo("Anulowano", "Nie wybrano pliku.")
        return

    # Uruchom Particle2MyAod.exe <file_path> -force e2160
    try:
        subprocess.run(
            ["./bin/ParticleTool/Particle2MyAod.exe", file_path, "-force", "e2160"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Błąd", f"Błąd podczas uruchamiania Particle2MyAod.exe:\n{e}")
        return

    # Ścieżka do folderu = katalog pliku + nazwa pliku bez rozszerzenia
    base_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    folder_name = os.path.splitext(file_name)[0]
    folder_path = os.path.join(base_dir, folder_name)

    if not os.path.isdir(folder_path):
        messagebox.showerror("Błąd", f"Nie znaleziono katalogu: {folder_path}")
        return

    # Uruchom MyAod2Particle.exe <folder_path>
    try:
        subprocess.run(
            ["./bin/ParticleTool/MyAod2Particle.exe", folder_path],
            check=True
        )
        messagebox.showinfo("Sukces", "Proces zakończony pomyślnie.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Błąd", f"Błąd podczas uruchamiania MyAod2Particle.exe:\n{e}")

if __name__ == "__main__":
    main()
