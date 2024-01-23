from flavourlib import CatppuccinColor
from PIL import Image, ImageDraw, ImageFont
import argparse

# require libraqm to use '--text-direction'
"""
```python
python banner.py --path="./test.png" --text="Hello\nEveryone!!" --text-color=lavender --text-border-color=text --image-b
order-color=mauve --font="./fonts/CascadiaCode/CaskaydiaCoveNerdFontMono-Bold.ttf" --image-border-radius=50 --text-align=c
enter
```
"""

parser = argparse.ArgumentParser(prog="banner.py", 
                                 description="Creates Catppuccin-Flavour Typography. See Github README for further informations.")

parser.add_argument("--path",               type=str, default="Banner.png")
parser.add_argument("--format",             type=str,                       help="Detect filetype if not specified.")
parser.add_argument("--text",               type=str, default="Catppuccin")
parser.add_argument("--text-geometry",      type=str,                       help="Starting position of the text. Use default value if not specified, but this is not recommended.")
parser.add_argument("--text-align",         type=str, default="left",       choices=["left", "center", "right"])
parser.add_argument("--text-direction",     type=str,                       choices=["ltr", "rtl", "ttb"])
parser.add_argument("--flavour",            type=str, default="mocha",      help="4 Catppuccin Flavours are available. See Github README for available choices.")
parser.add_argument("--base-image",         type=str,                       help="Select the background image. Use default image if not specified.")
parser.add_argument("--font",               type=str, required=True,        help="Path to `.ttf` file.")
parser.add_argument("--font-size",          type=int, default=0,            help="Specify the size of your text. Automatically calculated if not specified.")
parser.add_argument("--image-size",         type=str, default="1600x600",   help="Specify Size of the image.")
parser.add_argument("--text-color",         type=str, default="text",       help="Select Color of your text. See Github README for available colors.")
parser.add_argument("--text-border-color",  type=str, default="mauve",      help="Select Color of the text border. See Github README for available choices.")
parser.add_argument("--image-border-color", type=str, default="mauve",      help="Select Color of the image border. See Github README for available choices.")
parser.add_argument("--text-border-size",   type=int, default=-1,           help="Specify Size of the text border. Automatically calculated if not specified, or below 0.")
parser.add_argument("--image-border-size",  type=int, default=-1,           help="Specify Size of the image border. Aubomatically calculated if not specified, or below 0.")
parser.add_argument("--image-border-radius",type=int,                       help="Specify radius of the image border. Draw Rectangle if not specified.")


def parse_geometry(geometry:str, sep:str) -> tuple[int, int]:
    if len(sep) > 1:
        raise RuntimeError("Invalid separator")
    g = geometry.split(sep)
    return (int(g[0]), int(g[1]))

def textpos_calculate(imgsz:tuple[int, int]) -> tuple[int, int]:
    return (imgsz[0]//8, imgsz[1]//8)

def mask_alpha(image_A: Image, image_B: Image) -> Image:
    alpha_A = image_A.split()[3]
    r, g, b, _ = image_B.split()
    result = Image.merge("RGBA", (r, g, b, alpha_A))
    return result


option = parser.parse_args()
# --------------- basic settings ---------------
savepath = option.path # str
colorset = CatppuccinColor(option.flavour)
# -------------------- size --------------------
image_W, image_H = parse_geometry(option.image_size, 'x') # int, int
fontsize = option.font_size if option.font_size > 0 else image_H // 3 # int
# ---------------- text && font ----------------
text = option.text.replace(r"\n", "\n") # str
font = ImageFont.truetype(option.font, fontsize)
# ----- Border color && size configuration -----
text_color = colorset.crgba(option.text_color)
textborder_color = colorset.crgba(option.text_border_color)
imgborder_color = colorset.crgba(option.image_border_color)
textborder_size = option.text_border_size if option.text_border_size >= 0 else fontsize // 40 # int
imgborder_size = option.image_border_size if option.image_border_size >= 0 else fontsize // 20 # int
# ------------------- Image --------------------
mask = Image.new("RGBA", (image_W, image_H), color=(0, 0, 0, 0))
mask_canvas = ImageDraw.Draw(mask)
# --------------- text position ----------------
text_X = None
text_Y = None
if option.text_geometry is None:
    text_X, text_Y = textpos_calculate(imgsz=(image_W, image_H))
else:
    text_X, text_Y = parse_geometry(option.text_geometry, ',')
# -------------- Draw mask rectangle -------------
if option.image_border_radius is None:
    mask_canvas.rectangle([(imgborder_size // 2, imgborder_size // 2), 
                            (mask.size[0] - imgborder_size // 2 - 1, mask.size[1] - imgborder_size // 2 - 1)], 
                            width=imgborder_size,
                            fill=(0, 0, 0, 255))
else:
    mask_canvas.rounded_rectangle([(imgborder_size // 2, imgborder_size // 2), 
                            (mask.size[0] - imgborder_size // 2 - 1, mask.size[1] - imgborder_size // 2 - 1)], 
                            radius=option.image_border_radius, 
                            width=imgborder_size,
                            fill=(0, 0, 0, 255))        
# ------------- Draw base image to mask ----------
image = Image.new("RGBA", (image_W, image_H), color=colorset.crgba("base")) if option.base_image is None else Image.open(option.base_image).convert("RGBA")
result = mask_alpha(mask, image)
canvas = ImageDraw.Draw(result)

# --------------- Draw image border --------------
if imgborder_size > 0:
    if option.image_border_radius is None:
        canvas.rectangle([(imgborder_size // 2, imgborder_size // 2), 
                                (mask.size[0] - imgborder_size // 2 - 1, mask.size[1] - imgborder_size // 2 - 1)], 
                                outline=imgborder_color, 
                                width=imgborder_size)
    else:
        canvas.rounded_rectangle([(imgborder_size // 2, imgborder_size // 2), 
                                (mask.size[0] - imgborder_size // 2 - 1, mask.size[1] - imgborder_size // 2 - 1)], 
                                radius=option.image_border_radius, 
                                outline=imgborder_color, 
                                width=imgborder_size)    

# ---------------- Draw text border --------------
if textborder_size > 0: # if size is 0, not drawing border
    for dx in range(-textborder_size, textborder_size + 1):
        for dy in range(-textborder_size, textborder_size + 1):
            canvas.text((text_X + dx, text_Y + dy), text=text, font=font, fill=textborder_color, align=option.text_align, direction=option.text_direction)
# ----------------- write text -----------------
canvas.text((text_X, text_Y), text, font=font, fill=text_color, align=option.text_align, direction=option.text_direction) # edit this part

# ----------------- Save Image -----------------
result.save(savepath, format=option.format)
