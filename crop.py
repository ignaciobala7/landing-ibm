from PIL import Image, ImageChops

def process_image(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Crop transparent borders
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    # Crop white borders
    bg = Image.new('RGBA', img.size, (255, 255, 255, 255))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    # Make square by adding minimal transparent padding
    width, height = img.size
    size = max(width, height)
    square = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    square.paste(img, ((size - width) // 2, (size - height) // 2))
    
    square.save(output_path)
    print("Done!")

process_image("Recursos/logo-fb.png", "Recursos/favicon_optimized.png")
