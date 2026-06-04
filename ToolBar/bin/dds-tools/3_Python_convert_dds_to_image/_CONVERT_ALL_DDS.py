import os
from PIL import Image

input_dir = "input"

output_dir = "output"

os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith(".dds"):
        file_path = os.path.join(input_dir, filename)

        try:
            # open the .dds file
            img = Image.open(file_path)
            
            new_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_dir, new_filename)

            # save in PNG format
            img.save(output_path, "PNG")
            print(f"Converted: {filename} → {new_filename}")

        except Exception as e:
            print(f"Error during {filename}: {e}")
