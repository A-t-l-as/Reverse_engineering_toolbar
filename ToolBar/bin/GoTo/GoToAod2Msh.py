import os

path = r"PATH\TO\DIRECTORY\Aod2Msh_2003_KnightShift"

try:
    os.startfile(path)
except FileNotFoundError:
    print(f"The path does not exist {path}")
except OSError as e:
    print(f"Another system error: {e}")
