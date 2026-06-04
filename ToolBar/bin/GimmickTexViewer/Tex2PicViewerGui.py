import sys
import shutil
import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import math

class Constants:
    BUFFER_DIR = "buffer~"
    BUFFER_FILE_1 = "buffer.bmp"
    BUFFER_FILE_2 = "buffer2.png"
    BUFFER_FILE_TEX = "buffer.tex"
    TEX2PIC_PATH = r"PATH\TO\DIRECTORY\GimmickTexViewer"
    
    BUFFER_DIR_PATH = os.path.join(TEX2PIC_PATH, BUFFER_DIR)
    BUFFER_FILE_2_PATH = os.path.join(TEX2PIC_PATH, BUFFER_FILE_2)
    BUFFER_FILE_1_PATH = os.path.join(TEX2PIC_PATH, BUFFER_FILE_1)

class ImageApp:
    def __init__(self, root, path):
        self.root = root
        self.root.title("GimmickTexViewer")

        # Główny frame
        main_frame = tk.Frame(root)
        main_frame.pack(fill="both", expand=True)

        # Lewa część – obrazek
        self.canvas = tk.Canvas(main_frame, bg="gray")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Prawa część – przyciski
        btn_frame = tk.Frame(main_frame)
        btn_frame.pack(side="right", fill="y", padx=10, pady=10)

        tk.Button(btn_frame, text="➕ Zoom in", command=self.zoom_in, width=10).pack(pady=5)
        tk.Button(btn_frame, text="➖ Zoom out", command=self.zoom_out, width=10).pack(pady=5)

        # Wczytanie obrazu
        self.original = Image.open(path)
        self.scale = 1.0
        self.display_image()

    def display_image(self):
        w, h = self.original.size
        new_size = (int(w * self.scale), int(h * self.scale))
        resized = self.original.resize(new_size, Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resized)

        self.canvas.delete("all")  # usuwa poprzedni obraz
        # wyśrodkowanie obrazu w canvas
        canvas_w = self.canvas.winfo_width() or self.canvas.winfo_reqwidth()
        canvas_h = self.canvas.winfo_height() or self.canvas.winfo_reqheight()
        self.canvas.create_image(canvas_w//2, canvas_h//2, image=self.img, anchor="center")

    def zoom_in(self):
        self.scale *= 1.2
        self.display_image()

    def zoom_out(self):
        self.scale *= 0.8
        self.display_image()


def join_images_with_montage():

    # sprawdzenie katalogu
    if not os.path.isdir(Constants.BUFFER_DIR_PATH):
        print(f"No {Constants.BUFFER_DIR_PATH} directory")
        return
    
    # znajdź wszystkie pliki graficzne
    files = sorted([
        f for f in os.listdir(Constants.BUFFER_DIR_PATH) 
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))
    ])
    
    if not files:
        print(f"No images in the {Constants.BUFFER_DIR_PATH} directory")
        return
    
    images = [Image.open(os.path.join(Constants.BUFFER_DIR_PATH, f)) for f in files]
    widths, heights = zip(*(im.size for im in images))
    
    # oblicz kafelkowanie (np. kwadratowe)
    cols = math.ceil(math.sqrt(len(images)))
    rows = math.ceil(len(images) / cols)
    
    max_w = max(widths)
    max_h = max(heights)
    
    out = Image.new("RGB", (cols * max_w, rows * max_h), (255, 255, 255))
    
    for idx, im in enumerate(images):
        x = (idx % cols) * max_w
        y = (idx // cols) * max_h
        out.paste(im, (x, y))
    
    out.save(Constants.BUFFER_FILE_2_PATH)
    print(f"{Constants.BUFFER_FILE_2_PATH} was created using Pillow")

def main():

    root = tk.Tk()
    root.withdraw()  # Ukrywa główne okno
    zrodlo = filedialog.askopenfilename(title="Select file")
    if zrodlo:
        print("Selected path:", zrodlo)
    else:
        print("No file selected.")
        return
    
    katalog_docelowy = Constants.TEX2PIC_PATH
    plik_docelowy = os.path.join(katalog_docelowy, Constants.BUFFER_FILE_TEX)

    # Kopiowanie pliku
    try:
        shutil.copy2(zrodlo, plik_docelowy)
        print(f"File copied to {plik_docelowy}")
    except Exception as e:
        print(f"Error copying file: {e}")
        return


    # Uruchomienie programu Texviewer_inside.exe z argumentem bufor.bin
    try:
        subprocess.run(
            [os.path.join(katalog_docelowy, "Tex2Pic.exe"),"/f", Constants.BUFFER_FILE_TEX],
            cwd=katalog_docelowy
        )
        print("The Tex2Pic.exe program has been launched.")
    except Exception as e:
        print(f"Error when starting the program: {e}")
    
    join_images_with_montage()
    
   
    root.deiconify()
    root.geometry("1000x600")

    if os.path.exists(Constants.BUFFER_FILE_2_PATH):
        app = ImageApp(root, Constants.BUFFER_FILE_2_PATH)
    else:
        print(f"File {Constants.BUFFER_FILE_2_PATH} does not exist")
    
    if os.path.exists(Constants.BUFFER_FILE_1_PATH):
        app = ImageApp(root, Constants.BUFFER_FILE_1_PATH)
    else:
        print(f"File {Constants.BUFFER_FILE_1_PATH} does not exist")
    
    root.mainloop()
    
if __name__ == "__main__":
    main()
