<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/Catppuccin-Banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="./assets/Catppuccin-Banner-light.png">
  <img alt="Catppuccin-Banner" src="./assets/Catppuccin-Banner-dark.png">
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
| `--image-size` | `str` | Image size in `[width]x[height]` format. | `"1600x600"` |
| `--text-border` | `str` | Color of the text border. Available options [here](#catppuccin-flavours-and-colors). | `"mauve"` |
| `--text-border-size` | `int` | Text border size. Automatically set to `1/40` of font size if < 0. | `-1` |
| `--image-border` | `str` | Color of the image border. Available options [here](#catppuccin-flavours-and-colors). | `"mauve"` |
| `--image-border-size` | `int` | Image border size. Automatically set to `1/20` of font size if < 0. | `-1` |

### Catppuccin Flavours and colors

```python
flavour_choice = [
    "latte", "frappe",
    "macchiatto", "mocha",
]

color_choice = [
    "rosewater", "flamingo", "pink", "mauve", "red",
    "maroon", "peach", "yellow", "green", "teal",
    "sky", "sapphire", "blue", "lavender", "text",
    "subtext1", "subtext0", "overlay2", "overlay1",
    "overlay0", "surface2", "surface1", "surface0",
    "base", "mantle", "crust",
]
```

### Examples

Below are commands to create Dark/Light theme banner images for this repository. Check out the [Mocha theme image](./assets/Catppuccin-Banner-dark.png) and the [Latte theme image](./assets/Catppuccin-Banner-light.png)

1. Dark theme banner

```bash
$ python banner.py \ 
    --path="./assets/Catppuccin-Banner-dark.png" \ 
    --text="Catppuccin\nBanner" \ 
    --flavour=mocha \ 
    --text-color=sky \ 
    --text-border-color=text \ 
    --image-border-color=lavender \ 
    --font="./fonts/Shadows_Into_Light/ShadowsIntoLight-Regular.ttf" \ 
    --image-border-radius=20 \ 
    --text-align=left \ 
    --text-geometry="40,40" 
```

2. Light theme banner

```bash
$ python banner.py\ 
    --path="./assets/Catppuccin-Banner-light.png" \
    --text="Catppuccin\nBanner" \
    --flavour=latte \
    --text-color=lavender \
    --text-border-color=text \
    --image-border-color=sky \
    --font="./fonts/Shadows_Into_Light/ShadowsIntoLight-Regular.ttf" \
    --image-border-radius=20 \
    --text-align=left \
    --text-geometry="40,40"
```

### LICENSE
given default fonts are sourced from [Google Open Source Fonts](https://fonts.google.com/).   
Fonts are licensed under OFL.
