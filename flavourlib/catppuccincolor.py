from catppuccin import Flavour, Colour

class CatppuccinColor:

    def __init__(self, flavour: str):
        self.flavour_name = flavour
        self.flavour = CatppuccinColor.get_flavour(flavour) # error for invalid flavour

    def chex(self, color:str, prefix='#'):
        return prefix + CatppuccinColor.get_color(self.flavour_name, color).hex

    def crgb(self, color:str):
        return CatppuccinColor.get_color(self.flavour_name, color).rgb
    
    def crgba(self, color:str):
        return CatppuccinColor.get_color(self.flavour_name, color).rgba

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

    @staticmethod
    def get_color(flavour:str|Flavour, color:str) -> Colour:
        if color not in CatppuccinColor.color_choice:
            raise ValueError("No such Catppuccin Color")
        f = None
        if isinstance(flavour, str):
            f = CatppuccinColor.get_flavour(flavour)
        else:
            if isinstance(flavour, Flavour):
                f = flavour
            else:
                raise ValueError("Invalid Flavour Type")
        return f.__dict__[color]
        
    @staticmethod
    def get_flavour(flavour: str) -> Flavour:
        if   flavour == "latte":        return Flavour.latte()
        elif flavour == "frappe":       return Flavour.frappe()
        elif flavour == "macchiatto":   return Flavour.macchiato()
        elif flavour == "mocha":        return Flavour.mocha()
        else:       raise ValueError("Invalid Catppuccin Flavour")

if __name__ == "__main__":
    c = CatppuccinColor("mocha")
    print(c.chex("base", prefix='#'))