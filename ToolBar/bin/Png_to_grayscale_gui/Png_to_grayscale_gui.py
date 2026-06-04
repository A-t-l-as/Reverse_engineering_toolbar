from tkinter import Tk, filedialog
from PIL import Image

def convert_png_to_bmp(input_path, output_path):
    """
    Converts a PNG image to BMP in 8-bit grayscale and sets the resolution to 72 DPI.
    """
    try:
        with Image.open(input_path) as img:
          
            gray_img = img.convert('L')

            gray_img.save(output_path, format='BMP', dpi=(72, 72))

            print(f"The file has been successfully saved as {output_path} in 8-bit grayscale and 72 DPI. ")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

root = Tk()
root.withdraw()

inputfilename = filedialog.askopenfilename(
    title="Select a PNG file",
    filetypes=[("PNG files", "*.png")]
)

if inputfilename:
    
    outputfilename = filedialog.asksaveasfilename(
        title="Save as BMP",
        defaultextension=".bmp",
        filetypes=[("BMP files", "*.bmp")]
    )

    if outputfilename:
        convert_png_to_bmp(inputfilename, outputfilename)
    else:
        print("No output file has been selected.")
else:
    print("No input file has been selected.")