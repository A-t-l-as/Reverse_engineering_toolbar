import os
from tkinter import Tk, filedialog
from pydub import AudioSegment

def main():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select an audio file",
        filetypes=[("Audio files", "*.mp3 *.wav *.flac *.ogg *.aac *.m4a *.wma *.aiff *.au"), ("All files", "*.*")]
    )

    if not file_path:
        print("No file has been selected.")
        return

    mp2_path = os.path.splitext(file_path)[0] + ".mp2"

    audio = AudioSegment.from_file(file_path)
    audio.export(mp2_path, format="mp2")
    print(f"The file has been converted to: {mp2_path}")

    tws_path = mp2_path.replace(".mp2", ".tws")
    os.rename(mp2_path, tws_path)
    print(f"The file was saved as: {tws_path}")


if __name__ == "__main__":
    main()
