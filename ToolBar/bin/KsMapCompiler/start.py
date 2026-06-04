import subprocess
import os

def main():
    
    os.chdir(r"PATH\TO\DIRECTORY\KsMapCompiler")
    command = r".\KsMapCompiler.exe"

    try:
        # Uruchamiamy program z wybraną ścieżką
        result = subprocess.run(command, capture_output=True, text=True)

        # Wyświetlamy wynik
        print("=== WYJŚCIE PROGRAMU ===")
        print(result.stdout)
        print("=== BŁĘDY (jeśli były) ===")
        print(result.stderr)

    except FileNotFoundError:
        print("Nie znaleziono pliku KsMapCompiler.exe w bieżącym katalogu!")

if __name__ == "__main__":
    main()
