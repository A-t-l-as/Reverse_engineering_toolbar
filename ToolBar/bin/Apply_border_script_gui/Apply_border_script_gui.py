from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def apply_border(bitmap_path, border_path, output_path):
    """
    Applies a border to a bitmap while preserving the parameters of the input image.
    """
    try:
        # Open the bitmap and read its parameters
        bitmap = Image.open(bitmap_path)
        original_format = bitmap.format
        original_mode = bitmap.mode
        original_size = bitmap.size

        # Convert bitmap to RGBA for operations (restore at the end)
        bitmap = bitmap.convert("RGBA")

        # Open the frame and adjust the size
        border = Image.open(border_path).convert("RGBA")
        border = border.resize(original_size)

        # Applying a border to a bitmap
        result = Image.alpha_composite(bitmap, border)

        # Convert the result to the original mode (if possible)
        if original_mode != "RGBA":
            result = result.convert(original_mode)

        # Save the resulting image in its original format.
        result.save(output_path, format=original_format)
        messagebox.showinfo("Sukces", f"Obraz zapisano w:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error has occurred: {e}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Select a bitmap file
    bitmap_path = filedialog.askopenfilename(
        title="Select a bitmap file",
        filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All files", "*.*")]
    )
    if not bitmap_path:
        return

    # Select the border file
    border_path = filedialog.askopenfilename(
        title="Select a file with a border",
        filetypes=[("Images PNG", "*.png"), ("All files", "*.*")]
    )
    if not border_path:
        return

    # Select the save location
    output_path = filedialog.asksaveasfilename(
        title="Save the resulting image as",
        defaultextension=".png",
        filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All files", "*.*")]
    )
    if not output_path:
        return

    apply_border(bitmap_path, border_path, output_path)


if __name__ == "__main__":
    main()
