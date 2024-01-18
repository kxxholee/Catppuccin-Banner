<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/Catppuccin-Banner-Dark.jpg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/Catppuccin-Banner-Light.jpg">
  <img alt="Catppuccin-Banner" src="./assets/Catppuccin-Banner-Dark.jpg">
</picture>

----------------------------------------------------

### Requirements
|  Library   |          version        |
|------------|-------------------------|
|   `PIL`    |   Recommended:`10.1.0`  |
|`catppuccin`|           `Any`         |

install requirements `pip`

* install catppuccin with `pip`

```bash
$ pip install catppuccin
```

Further resources : 
* [Official Catppuccin Palette](https://github.com/catppuccin/python/tree/main?tab=readme-ov-file)
* [Official Pillow Installation Guide](https://pillow.readthedocs.io/en/latest/installation.html#python-support)

### Usage
The Python code utilizes the argparse library, allowing for various configurations of the image through the terminal. 


| option | type | role | default value |
| ---- | ---- | ---- | ---- |
| `--path` | `str` | Path for saving the generated image. | `"./Catppuccin-Banner.jpg"` |
| `--text` | `str` | Text content for the image. Use `\n` for multi-line text. | `"Catppuccin"` |
| `--text-geometry` | `str` | Text position on the image in `x,y` format. Position is auto-calculated if not specified. | `None` | 
| `--flavour` | `str` | Select catppuccin flavour (background color). Available options [here](#catppuccin-flavours-and-colors).  | `"mocha"` |
| `--font` | `str` | Path to the TrueType text font. | `$FONT_PATH` |
| `--font-size` | `int` | Font size. Automatically set to `1/3` of image height if ≤ 0. | `0` |
| `--image-size` | `str` | set size of the image using format `[width]x[height]`. | `"1600x600"` |
| `--text-border` | `str` | set color of text border. see available options [here](#catppuccin-flavours-and-colors). | `"mauve"` |
| `--text-border-size` | `int` | set size of text border. if the value is 0, text border will not appear. if the value is smaller than 0, border size will automatically be `1//40` of font size. | `-1` |
| `--image-border` | `str` | set color of image border. see available options [here](#catppuccin-flavours-and-colors). | `"mauve"` |
| `--image-border-size` | `int` | set size of image border. If the value is 0, text border will not appear. if the value is smaller than 0, border size will automatically be `1//20` of font size. | `-1` |

### Catppuccin Flavours and colors
```python
flavour_choice = [ # flavour options (background color)
    "latte",
    "frappe",
    "macchiatto",
    "mocha"
]

color_choice = [ # text-border &$ image-border color options
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
    "lavender"
]
```

### Examples

Each commands below creates Dark/Light theme images of the banner of this repository. See results of [Mocha theme image](./assets/Catppuccin-Banner-Dark.jpg) and also [Latte theme image](./assets/Catppuccin-Banner-Light.jpg)

1. Dark theme banner

```bash
$ python banner.py \
    --text-geometry="40,20" \
    --path="./assets/Catppuccin-Banner-Dark.jpg" \
    --text="Catppuccin\nBanner" \
    --text-border="sapphire" \
    --image-border="lavender" \
    --text-border-size=-1 \
    --image-border-size=-1 \
    --flavour="mocha"
```

2. Light theme banner

```bash
$ python banner.py \
    --text-geometry="40,20" \
    --path="./assets/Catppuccin-Banner-Light.jpg" \
    --text="Catppuccin\nBanner" \
    --text-border="lavender" \
    --image-border="sapphire" \
    --text-border-size=-1 \
    --image-border-size=-1 \
    --flavour="latte"
```

### LICENSE
given default fonts are downloaded from [Google Open Source Fonts](https://fonts.google.com/).   
Font licenses are under OFL.
