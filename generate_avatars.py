from PIL import Image, ImageDraw
import math

def create_couple_boy():
    size = 512
    img = Image.new('RGBA', (size, size), (200, 220, 235, 255))
    d = ImageDraw.Draw(img)
    
    cx, cy = size // 2, size // 2
    
    # T-shirt body
    d.pieslice((cx-120, cy+120, cx+120, cy+340), 180, 360, fill=(107, 139, 168, 255))
    d.rectangle((cx-120, cy+180, cx+120, cy+260), fill=(107, 139, 168, 255))
    
    # Neck
    d.rectangle((cx-30, cy+60, cx+30, cy+130), fill=(245, 208, 184, 255))
    
    # Head - face
    d.ellipse((cx-110, cy-160, cx+110, cy+120), fill=(245, 208, 184, 255))
    
    # Ears
    d.ellipse((cx-125, cy-30, cx-95, cy+70), fill=(245, 208, 184, 255))
    d.ellipse((cx+95, cy-30, cx+125, cy+70), fill=(245, 208, 184, 255))
    
    # Hair - top
    for i in range(0, 180, 8):
        angle = math.radians(180 + i)
        r = 115
        x = cx + r * math.cos(angle)
        y = cy - 80 + r * math.sin(angle) * 0.9
        hair_r = 30 + (i % 30) / 3
        d.ellipse((x-hair_r, y-hair_r, x+hair_r, y+hair_r), fill=(58, 58, 58, 255))
    
    # Main hair cap
    d.ellipse((cx-120, cy-200, cx+120, cy-20), fill=(45, 45, 45, 255))
    
    # Hair bangs
    d.ellipse((cx-80, cy-130, cx-20, cy-60), fill=(42, 42, 42, 255))
    d.ellipse((cx+20, cy-130, cx+80, cy-60), fill=(42, 42, 42, 255))
    d.ellipse((cx-50, cy-100, cx+50, cy-40), fill=(42, 42, 42, 255))
    
    # Eyes - big round
    # Left eye
    d.ellipse((cx-55, cy-20, cx-15, cy+20), fill=(42, 42, 42, 255))
    d.ellipse((cx-48, cy-13, cx-25, cy+10), fill=(255, 255, 255, 255))
    d.ellipse((cx-45, cy-10, cx-35, cy+0), fill=(255, 255, 255, 255))
    
    # Right eye
    d.ellipse((cx+15, cy-20, cx+55, cy+20), fill=(42, 42, 42, 255))
    d.ellipse((cx+25, cy-13, cx+48, cy+10), fill=(255, 255, 255, 255))
    d.ellipse((cx+35, cy-10, cx+45, cy+0), fill=(255, 255, 255, 255))
    
    # Eyebrows
    d.arc((cx-65, cy-55, cx-5, cy-25), 180, 360, fill=(42, 42, 42, 255), width=5)
    d.arc((cx+5, cy-55, cx+65, cy-25), 180, 360, fill=(42, 42, 42, 255), width=5)
    
    # Blush
    d.ellipse((cx-90, cy+40, cx-50, cy+70), fill=(255, 184, 184, 140))
    d.ellipse((cx+50, cy+40, cx+90, cy+70), fill=(255, 184, 184, 140))
    
    # Smile
    d.arc((cx-30, cy+40, cx+30, cy+80), 0, 180, fill=(192, 112, 112, 255), width=6)
    
    # Crop to square
    return img

def create_couple_girl():
    size = 512
    img = Image.new('RGBA', (size, size), (245, 235, 220, 255))
    d = ImageDraw.Draw(img)
    
    cx, cy = size // 2, size // 2
    
    # Long hair behind body - left
    d.ellipse((cx-170, cy-60, cx-50, cy+280), fill=(74, 58, 58, 255))
    # Long hair behind body - right
    d.ellipse((cx+50, cy-60, cx+170, cy+280), fill=(74, 58, 58, 255))
    
    # Body / top
    d.pieslice((cx-130, cy+120, cx+130, cy+340), 180, 360, fill=(232, 220, 200, 255))
    d.rectangle((cx-130, cy+180, cx+130, cy+260), fill=(232, 220, 200, 255))
    
    # Neck
    d.rectangle((cx-30, cy+60, cx+30, cy+130), fill=(245, 216, 192, 255))
    
    # Head - face
    d.ellipse((cx-115, cy-170, cx+115, cy+110), fill=(245, 216, 192, 255))
    
    # Ears
    d.ellipse((cx-130, cy-25, cx-100, cy+75), fill=(245, 216, 192, 255))
    d.ellipse((cx+100, cy-25, cx+130, cy+75), fill=(245, 216, 192, 255))
    
    # Hair top - main cap
    d.ellipse((cx-125, cy-220, cx+125, cy-10), fill=(74, 58, 58, 255))
    
    # Hair bangs - fluffy
    for i, x in enumerate(range(cx-100, cx+100, 35)):
        h = 40 if i % 2 == 0 else 55
        d.ellipse((x-25, cy-120-h, x+25, cy-80), fill=(58, 42, 42, 255))
    
    # Hair sides
    d.ellipse((cx-130, cy-30, cx-80, cy+150), fill=(74, 58, 58, 255))
    d.ellipse((cx+80, cy-30, cx+130, cy+150), fill=(74, 58, 58, 255))
    
    # Hair ends - wavy
    for x in range(cx-160, cx+160, 40):
        d.ellipse((x-20, cy+240, x+20, cy+290), fill=(74, 58, 58, 255))
    
    # Eyes - big round
    # Left eye
    d.ellipse((cx-60, cy-15, cx-15, cy+30), fill=(42, 42, 42, 255))
    d.ellipse((cx-52, cy-5, cx-25, cy+20), fill=(255, 255, 255, 255))
    d.ellipse((cx-50, cy-3, cx-38, cy+12), fill=(255, 255, 255, 255))
    
    # Right eye
    d.ellipse((cx+15, cy-15, cx+60, cy+30), fill=(42, 42, 42, 255))
    d.ellipse((cx+25, cy-5, cx+52, cy+20), fill=(255, 255, 255, 255))
    d.ellipse((cx+38, cy-3, cx+50, cy+12), fill=(255, 255, 255, 255))
    
    # Eyebrows
    d.arc((cx-70, cy-50, cx-5, cy-20), 180, 360, fill=(58, 42, 42, 255), width=5)
    d.arc((cx+5, cy-50, cx+70, cy-20), 180, 360, fill=(58, 42, 42, 255), width=5)
    
    # Blush (more prominent)
    d.ellipse((cx-100, cy+50, cx-50, cy+85), fill=(255, 184, 184, 160))
    d.ellipse((cx+50, cy+50, cx+100, cy+85), fill=(255, 184, 184, 160))
    
    # Smile
    d.arc((cx-30, cy+50, cx+30, cy+90), 0, 180, fill=(192, 112, 112, 255), width=6)
    
    # Heart necklace
    hx, hy = cx, cy+155
    # Draw heart shape
    heart = Image.new('RGBA', (40, 40), (0, 0, 0, 0))
    hd = ImageDraw.Draw(heart)
    hd.ellipse((2, 5, 18, 21), fill=(255, 156, 181, 255))
    hd.ellipse((22, 5, 38, 21), fill=(255, 156, 181, 255))
    hd.polygon([(2, 18), (38, 18), (20, 38)], fill=(255, 156, 181, 255))
    heart = heart.resize((30, 30), Image.LANCZOS)
    img.paste(heart, (hx-15, hy-15), heart)
    
    return img

# Generate and save
boy = create_couple_boy()
boy = boy.resize((600, 600), Image.LANCZOS)
boy.save('/workspace/public/images/couple-boy.png', 'PNG', optimize=True)
print(f"couple-boy.png saved: {boy.size}")

girl = create_couple_girl()
girl = girl.resize((600, 600), Image.LANCZOS)
girl.save('/workspace/public/images/couple-girl.png', 'PNG', optimize=True)
print(f"couple-girl.png saved: {girl.size}")
