import os

path = r"PATH\TO\DIRECTORY\sample_work_space\Scripts"

try:
    os.startfile(path)
except FileNotFoundError:
    print(f"The path does not exist {path}")
except OSError as e:
    print(f"Another system error: {e}")
