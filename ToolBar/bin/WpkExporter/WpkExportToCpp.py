import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def main():
    # Tworzymy ukryte okno tkinter (nie chcemy pustego okna)
    root = tk.Tk()
    root.withdraw()

    # Okno wyboru pliku
    file_path = filedialog.askopenfilename(title="Wybierz plik")

    if not file_path:
        print("Nie wybrano pliku. Zamykanie programu.")
        return

    # Tworzymy komendę
    command = [r".\bin\WpkExporter\WpkExporter.exe", file_path, "cpp"]

    try:
        # Uruchamiamy program z wybraną ścieżką
        result = subprocess.run(command, capture_output=True, text=True)

        # Wyświetlamy wynik
        print("=== WYJŚCIE PROGRAMU ===")
        print(result.stdout)
        print("=== BŁĘDY (jeśli były) ===")
        print(result.stderr)

    except FileNotFoundError:
        print("Nie znaleziono pliku WpkExporter.exe w bieżącym katalogu!")

if __name__ == "__main__":
    main()
