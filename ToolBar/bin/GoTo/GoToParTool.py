import os

path = r"PATH\TO\DIRECTORY\Turbo-ParTool-ByAtlas_v5_0"

try:
    os.startfile(path)
except FileNotFoundError:
    print(f"The path does not exist {path}")
except OSError as e:
    print(f"Another system error: {e}")
