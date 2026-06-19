import os
from PIL import Image

def create_square_favicon(input_path, output_path, padding=20):
    try:
        with Image.open(input_path) as img:
            img = img.convert("RGBA")
            # Get bounding box of non-transparent pixels
            bbox = img.getbbox()
            if not bbox:
                print(f"Image {input_path} is completely transparent.")
                return False
                
            # Crop to bounding box
            cropped = img.crop(bbox)
            
            # Make it a square
            width, height = cropped.size
            max_dim = max(width, height)
            
            # Create a new transparent square image
            square_size = max_dim + padding * 2
            square_img = Image.new('RGBA', (square_size, square_size), (0, 0, 0, 0))
            
            # Paste the cropped image in the center
            offset_x = (square_size - width) // 2
            offset_y = (square_size - height) // 2
            square_img.paste(cropped, (offset_x, offset_y), cropped)
            
            # Resize to 512x512 for favicon
            final_img = square_img.resize((512, 512), Image.Resampling.LANCZOS)
            
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            final_img.save(output_path, "PNG")
            print(f"Success: Created {output_path} from {input_path}")
            return True
    except Exception as e:
        print(f"Error processing {input_path}: {e}")
        return False

# Try multiple possible source images
sources = [
    r"Recursos\logo-ibm.png",
    r"Recursos\IBM Logo Fondo Claro.png",
    r"Recursos\logo-fb.png"
]

output_path = r"Recursos\opt\favicon_real_logo.png"

for src in sources:
    if os.path.exists(src):
        if create_square_favicon(src, output_path):
            break
else:
    print("Could not find any suitable source image.")
