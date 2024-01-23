<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/Catppuccin-Banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="./assets/Catppuccin-Banner-light.png">
  <img alt="Catppuccin-Banner" src="./assets/Catppuccin-Banner-dark.png">
</picture>

----------------------------------------------------

### Requirements
|  Library   |          version        |     Required      |                 Purpose                |
|------------|-------------------------|-------------------|----------------------------------------|
|   `PIL`    |   Recommended:`10.1.0`  |        True       |             Image processing           |
|`catppuccin`|           `Any`         |        True       |       Provide catppuccin palettes      |
| `libraqm`  |           `Any`         |      Optional     |    To use `--text-direction` option    |

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


| option                | type  | role                                                                                       | default value  |
|-----------------------|-------|--------------------------------------------------------------------------------------------|----------------|
| `--path`              | str   | Path to save the generated banner image.                                                   | "Banner.png"   |
| `--format`            | str   | File format for the output image. Automatically detected if not specified.                 | None           |
| `--text`              | str   | Text to be displayed on the banner.                                                        | "Catppuccin"   |
| `--text-geometry`     | str   | Starting position (x,y) of the text on the banner.                                         | None           |
| `--text-align`        | str   | Alignment of the text. Options: 'left', 'center', 'right'.                                 | "left"         |
| `--text-direction`    | str   | Direction of the text. Requires libraqm. Options: 'ltr', 'rtl', 'ttb'.                     | None           |
| `--flavour`           | str   | Catppuccin color theme. Options in Github README.                                         | "mocha"        |
| `--base-image`        | str   | Path to a base image for the banner background.                                           | None           |
| `--font`              | str   | Path to the '.ttf' font file for the text.                                                 | None (required)|
| `--font-size`         | int   | Font size for the text. Automatically calculated if not specified.                         | 0              |
| `--image-size`        | str   | Size of the banner image. Format: 'widthxheight'.                                          | "1600x600"     |
| `--text-color`        | str   | Color of the text. Options in Github README.                                               | "text"         |
| `--text-border-color` | str   | Color of the text border. Options in Github README.                                        | "mauve"        |
| `--image-border-color`| str   | Color of the image border. Options in Github README.                                       | "mauve"        |
| `--text-border-size`  | int   | Size of the text border. Automatically calculated if not specified or below 0.             | -1             |
| `--image-border-size` | int   | Size of the image border. Automatically calculated if not specified or below 0.            | -1             |
| `--image-border-radius`| int  | Radius of the image border corners. Rectangle is drawn if not specified.                   | None           |


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
