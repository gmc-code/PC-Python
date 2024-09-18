import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import json
import colorsys

currfile_dir = Path(__file__).parent
txt_path = currfile_dir / "turtle_color_names.txt"

# Open the file
with open(txt_path, 'r') as file:
    # Load the dictionary
    colornames_dict = json.load(file)

# Function to convert hex to RGB
def hex_to_rgb(hex_color):
    return [int(hex_color[i:i+2], 16) for i in (1, 3, 5)]

# Convert hex colors to HSV and create a list of tuples (colorname, hexvalue, hsv)
color_tuples = [(colorname, hexvalue, hex_to_rgb(hexvalue)) for colorname, hexvalue in colornames_dict.items()]


# # Build dict from list of tuples
colornames_dict = {t[0]: tuple(t[2]) for t in color_tuples}
# print(colornames_dict)

# Save to file
txt2_path = currfile_dir / "turtle_colornames_rgb.txt"

# Open the file
with open(txt2_path, 'w') as file:
    # Save the dictionary
    json.dump(colornames_dict, file)

# Save to file
txt3_path = currfile_dir / "turtle_rgb_colornames2.txt"


# Create an empty dictionary
new_dict = {}

# Loop through the items of the data object
for name, rgb in colornames_dict.items():
  # Convert the list into a tuple
  rgb_tuple = str(tuple(rgb))
  # Use the tuple as the key and the name as the value of the new dictionary
  new_dict[rgb_tuple] = name

# Open the file
with open(txt3_path, 'w') as file:
    # Save the dictionary
    json.dump(new_dict, file)

