from PIL import Image, ImageChops

def extract_shield(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Crop white/transparent borders first
    bg = Image.new('RGBA', img.size, (255, 255, 255, 255))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    width, height = img.size
    
    # The shield is usually at the top, and the text is below.
    # The shield is roughly square. Let's crop the top part based on the width.
    # We will look for the first empty row to separate shield from text.
    
    # Let's just crop a square from the top-center!
    # Because the shield is centered at the top.
    # Wait, the width of the shield is probably less than the width of the text.
    # Let's find the bounding box of the top connected component.
    
    pixels = img.load()
    
    # Find the bottom of the shield by looking for a horizontal gap
    # A gap is a row with all white or transparent pixels.
    shield_bottom = height
    in_shield = True
    for y in range(height):
        row_is_empty = True
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a > 10 and (r < 240 or g < 240 or b < 240):
                row_is_empty = False
                break
        
        if y > 10 and not row_is_empty:
            in_shield = True
        if y > 10 and row_is_empty and in_shield:
            shield_bottom = y
            break
            
    # Crop the top part (shield)
    shield_img = img.crop((0, 0, width, shield_bottom))
    
    # Now crop horizontal empty space of the shield
    bg_shield = Image.new('RGBA', shield_img.size, (255, 255, 255, 255))
    diff_shield = ImageChops.difference(shield_img, bg_shield)
    bbox_shield = diff_shield.getbbox()
    if bbox_shield:
        shield_img = shield_img.crop(bbox_shield)
        
    # Make it a perfect square
    w, h = shield_img.size
    size = max(w, h)
    # Add some padding (e.g. 10%)
    pad = int(size * 0.1)
    size += pad * 2
    
    square = Image.new("RGBA", (size, size), (255, 255, 255, 0)) # transparent
    square.paste(shield_img, (pad + (size - w - pad*2) // 2, pad + (size - h - pad*2) // 2))
    
    square.save(output_path)
    print("Shield extracted successfully!")

extract_shield("Recursos/Logos/bordo_300.png", "Recursos/favicon_shield.png")
