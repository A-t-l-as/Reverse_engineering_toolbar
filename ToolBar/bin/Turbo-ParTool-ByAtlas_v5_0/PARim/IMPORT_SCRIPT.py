import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def main():

    # Tworzymy komendę
    command = [r"./bin/Turbo-ParTool-ByAtlas_v5_0/PARim/PARim.exe", "./bin/Turbo-ParTool-ByAtlas_v5_0/PARim/TestPar"]

    try:
        # Uruchamiamy program z wybraną ścieżką
        result = subprocess.run(command, capture_output=True, text=True)

        # Wyświetlamy wynik
        print("=== WYJŚCIE PROGRAMU ===")
        print(result.stdout)
        print("=== BŁĘDY (jeśli były) ===")
        print(result.stderr)

    except FileNotFoundError:
        print("Nie znaleziono pliku PARim.exe w bieżącym katalogu!")

if __name__ == "__main__":
    main()
