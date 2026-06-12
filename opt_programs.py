import os
from PIL import Image, ImageOps

def optimize_image(input_path, output_name, max_size=(1200, 1200), quality=85):
    try:
        with Image.open(input_path) as img:
            img = ImageOps.exif_transpose(img)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            output_dir = os.path.join("Recursos", "opt")
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, output_name)
            img.save(output_path, "JPEG", quality=quality)
            print(f"Success: {output_path}")
    except Exception as e:
        print(f"Error {input_path}: {e}")

images = [
    (r"fotos IBM\_7412427.jpg", "program_resi_3.jpg"),
    (r"fotos IBM\DSC08092.jpg", "program_resi_4.jpg")
]

for in_path, out_name in images:
    if os.path.exists(in_path):
        optimize_image(in_path, out_name)
    else:
        print(f"Missing: {in_path}")
