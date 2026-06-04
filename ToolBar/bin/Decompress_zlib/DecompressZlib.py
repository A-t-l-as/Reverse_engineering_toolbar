import zlib
import os
import tkinter as tk
from tkinter import filedialog

def extract_zlib_streams(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    results = []
    i = 0
    while i < len(data):
        try:
            decomp_obj = zlib.decompressobj()
            chunk = decomp_obj.decompress(data[i:])
            if chunk:
                results.append(chunk)
                # jump to where this stream ended
                i += len(data[i:]) - len(decomp_obj.unused_data)
                continue
        except zlib.error:
            pass
        i += 1

    return results


def main():
    # file selection window
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select the file to decompress")

    if not file_path:
        print("No file has been selected.")
        return

    print(f"File selected: {file_path}")

    streams = extract_zlib_streams(file_path)
    if not streams:
        print("No zlib streams found.")
        return

    # creating the destination directory
    base_name = os.path.basename(file_path)
    name_without_ext = base_name.replace(".", "_")
    output_dir = os.path.join(os.path.dirname(file_path), name_without_ext)

    os.makedirs(output_dir, exist_ok=True)

    # stream recording
    for idx, stream in enumerate(streams, start=1):
        out_path = os.path.join(output_dir, f"stream{idx}.bin")
        with open(out_path, "wb") as f:
            f.write(stream)
        print(f"Saved: {out_path}")

    print(f"Done! Streams {len(streams)} saved in {output_dir}")


if __name__ == "__main__":
    main()
