from catppuccin import Flavour
from PIL import Image, ImageDraw, ImageFont
import argparse

# pillow 10.1.0 
# install catppuccin via https://github.com/catppuccin/python/tree/main?tab=readme-ov-file
# change default font before making it public

flavour_choice = [
    "latte",
    "frappe",
    "macchiatto",
    "mocha"
]

color_choice = [
    "rosewater",
    "flamingo",
    "pink",
    "mauve",
    "red",
    "maroon",
    "peach",
    "yellow",
    "green",
    "teal",
    "sky",
    "sapphire",
    "blue",
    "labender"
]

parser = argparse.ArgumentParser(description="Catppuccin Typography")
parser.add_argument("--path", type=str, default="./Catppuccin-Banner.jpg")
parser.add_argument("--format", type=str, default=None) # save format of the image, let 'Image.save' guess by default
parser.add_argument("--text", type=str, default="Catppuccin")
parser.add_argument("--flavour", type=str, default="mocha", choices=flavour_choice)
parser.add_argument("--font", type=str, default="./fonts/Firacode/static/FiraCode-Regular.ttf")
parser.add_argument("--font-size", type=int, default=0) # negative or zero -> use default settings : 1//3 of image height
parser.add_argument("--image-size", type=str, default="1600x600")
parser.add_argument("--text-border", type=str, default="mauve", choices=color_choice)
parser.add_argument("--text-border-size", type=int, default=0) # negative value -> use default settings : 1//40 of font size
parser.add_argument("--image-border", type=str, default="mauve", choices=color_choice)
parser.add_argument("--image-border-size", type=int, default=0) # negative value -> use default settings : 1//20 of font size

def get_flavour(flavour: str) -> Flavour:
    if   flavour == "latte":        return Flavour.latte()
    elif flavour == "frappe":       return Flavour.frappe()
    elif flavour == "macchiatto":   return Flavour.macchiato()
    elif flavour == "mocha":        return Flavour.mocha()
    else:       raise ValueError("Invalid Catppuccin Flavour")

def geometry(geometry: str) -> tuple[int, int]:
    dim = geometry.split('x')
    return (int(dim[0]), int(dim[1]))

def textposition(imgsz:tuple[int, int], text:str, fontsize:int, spacing:int=10) -> tuple[int, int]:
    lines = text.split('\n')
    height = (len(lines) - 1) * spacing + len(lines) * fontsize
    return (spacing * 5, (imgsz[1] - height) // 2)


option = parser.parse_args()
# --------------- basic settings ---------------
savepath = option.path # str
flavour = get_flavour(option.flavour)
# -------------------- size --------------------
image_W, image_H = geometry(option.image_size) # int, int
fontsize_t = option.font_size if option.font_size > 0 else image_H // 3 # int
# ---------------- text && font ----------------
text = option.text.replace(r"\n", "\n") # str
font = ImageFont.truetype(option.font, fontsize_t)
# ----- Border color && size configuration -----
textborder_color = flavour.__dict__[option.text_border].rgb
imgborder_color = flavour.__dict__[option.image_border].rgb
textborder_size = option.text_border_size if option.text_border_size >= 0 else fontsize_t // 40 # int
imgborder_size = option.image_border_size if option.image_border_size >= 0 else fontsize_t // 20 # int
# ------------------- Image --------------------
image = Image.new("RGB", (image_W, image_H), color=flavour.base.rgb)
canvas = ImageDraw.Draw(image)
# --------------- text position ----------------
text_X, text_Y = textposition(
    imgsz=(image_W, image_H),
    text=text,
    fontsize=fontsize_t
)
# -------------- Draw text border --------------
if textborder_size > 0: # if size is 0, not drawing border
    for dx in range(-textborder_size, textborder_size + 1):
        for dy in range(-textborder_size, textborder_size + 1):
            canvas.text((text_X + dx, text_Y + dy), text=text, font=font, fill=textborder_color)
# ----------------- write text -----------------
canvas.text((text_X, text_Y), text, font=font, fill=flavour.text.rgb)

# -------------- Draw image border -------------
if imgborder_size > 0:
    canvas.rectangle([(imgborder_size // 2, imgborder_size // 2), 
                      (image.size[0] - imgborder_size // 2 - 1, image.size[1] - imgborder_size // 2 - 1)], 
                      outline=imgborder_color, 
                      width=imgborder_size)

# ----------------- Save Image -----------------
image.save(savepath, format=option.format)
