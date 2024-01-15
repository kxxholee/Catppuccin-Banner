<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/Catppuccin-Banner-Dark.jpg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/Catppuccin-Banner-Light.jpg">
  <img alt="Catppuccin-Banner" src="./assets/Catppuccin-Banner-Dark.jpg">
</picture>

----------------------------------------------------

### Installation
1. install pillow v10.1.0 using `pip`
    * install the latest version of Pillow

    ```bash
    $ python3 -m pip install --upgrade Pillow
    ```

    * install specific version of Pillow

    ```bash
    $ python3 -m pip install --upgrade Pillow=10.1.0
    ```

    * see also : [Official Pillow Installation Guide](https://pillow.readthedocs.io/en/latest/installation.html#python-support)

2. install catppuccin palette
    * install catppuccin with `pip`

    ```bash
    $ pip install catppuccin
    ```

    * see also : [Official Catppuccin Palette](https://github.com/catppuccin/python/tree/main?tab=readme-ov-file)

3. clone this repository
    
    ```bash
    $ git clone https://github.com/vanillaPenguin/Catppuccin-Banner.git
    ```

### Usage
The Python code utilizes the argparse library, allowing for various configurations of the image through the terminal. Each commands below creates Dark/Light theme images of [The banner for this repository](./assets/Catppuccin-Banner.jpg)

1. Dark theme banner

```bash
$ python banner.py \
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
$ python banner.py
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