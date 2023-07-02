"""
CP1404 - Hexadecimal colour codes
"""

COLOUR_CODES = {"apricot": "#fbceb1", "aqua": "#00ffff",
                "beige": "#f5f5dc", "bittersweet": "#fe6f5e",
                "boysenberry": "#873260", "bronze": "#cd7f32",
                "bubblegum": "#ffc1cc", "citrine": "#e4d00a",
                "denim": "#1560bd", "eggplant": "#614051"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()
