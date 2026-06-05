import os
from PIL import Image, ImageOps

def optimize_image(input_path, max_size, quality=80):
    try:
        with Image.open(input_path) as img:
            # Corregir rotación automática basada en EXIF
            img = ImageOps.exif_transpose(img)
            
            # Redimensionar manteniendo proporciones
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Crear directorio opt si no existe
            output_dir = os.path.join("Recursos", "opt")
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                
            filename = os.path.basename(input_path)
            output_path = os.path.join(output_dir, filename)
            
            # Guardar
            img.save(output_path, "JPEG", quality=quality)
            print(f"Comprimido: {input_path} -> {os.path.getsize(output_path)/1024:.1f} KB")
            return output_path
    except Exception as e:
        print(f"Error {input_path}: {e}")
        return None

images = [
    (r"fotos IBM\A7401000.jpg", (400, 400)),
    (r"fotos IBM\DSC08228.jpg", (400, 400)),
    (r"fotos IBM\_DSC1981.jpg", (400, 400)),
    (r"fotos IBM\DSC08122.jpg", (400, 400)),
    (r"Recursos\Testimonios\alumno1.jpg", (250, 250)),
    (r"Recursos\Testimonios\alumno2.jpg", (250, 250)),
    (r"Recursos\Testimonios\alumno3.jpg", (250, 250)),
    (r"Recursos\Testimonios\alumno4.jpg", (250, 250)),
    (r"fotos IBM\DJI_20241211183234_0096_D_ADAM.jpg", (1920, 1080)),
    (r"fotos IBM\_7412253.jpg", (800, 800)),
    (r"fotos IBM\_7412351.jpg", (800, 800))
]

for img_path, size in images:
    if os.path.exists(img_path):
        optimize_image(img_path, size)
    else:
        print(f"No encontrado: {img_path}")
