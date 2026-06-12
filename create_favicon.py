import os
from PIL import Image, ImageDraw, ImageFont

def create_favicon():
    size = (512, 512)
    bg_color = (139, 24, 24) # #8b1818 (Primary red from CSS)
    text_color = (255, 255, 255)
    
    img = Image.new('RGBA', size, bg_color)
    draw = ImageDraw.Draw(img)
    
    # Try to find a bold system font, fallback to default
    try:
        font = ImageFont.truetype("arialbd.ttf", 250)
    except:
        try:
            font = ImageFont.truetype("trebucbd.ttf", 250) # Trebuchet Bold
        except:
            font = ImageFont.load_default()
            
    text = "IBM"
    
    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    x = (size[0] - text_w) / 2
    # Slight visual adjustment for vertical centering depending on font
    y = (size[1] - text_h) / 2 - 20 
    
    draw.text((x, y), text, font=font, fill=text_color)
    
    out_dir = os.path.join("Recursos", "opt")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "favicon_ibm.png")
    
    img.save(out_path, "PNG")
    print(f"Created favicon at: {out_path}")

create_favicon()
