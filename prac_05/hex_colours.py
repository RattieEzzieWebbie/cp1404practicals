"""
CP1404/CP5632 Practical
Hexadecimal Colour Lookup
"""

HEX_COLOURS = {
    "AliceBlue": "#F0F8FF",
    "AntiqueWhite": "#FAEBD7",
    "Aqua": "#00FFFF",
    "Aquamarine": "#7FFFD4",
    "Azure": "#F0FFFF",
    "Beige": "#F5F5DC",
    "Bisque": "#FFE4C4",
    "Black": "#000000",
    "BlanchedAlmond": "#FFEBCD",
    "Blue": "#0000FF"
}

# Print all colours and their hex codes
for colour_name, hex_code in HEX_COLOURS.items():
    print(f"{colour_name:<15} is {hex_code}")

colour_name = input("Enter colour name: ").strip().title()
while colour_name:
    try:
        print(f"{colour_name} is {HEX_COLOURS[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").strip().title()