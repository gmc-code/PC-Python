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



# Define colors
colornames = list(colornames_dict.keys())
#hex values
hexvals = list(colornames_dict.values())
# rev dict
hex_colname_dict = {}
for k, v in colornames_dict.items():
    if v not in hex_colname_dict:
        hex_colname_dict[v] = [k]
    else:
        hex_colname_dict[v].append(k)

# Function to convert hex to RGB
def hex_to_rgb(hex_color):
    return [int(hex_color[i:i+2], 16) for i in (1, 3, 5)]

# Function to convert RGB to HSV
def rgb_to_hsv(rgb_color):
    return colorsys.rgb_to_hsv(rgb_color[0]/255, rgb_color[1]/255, rgb_color[2]/255)

# Convert hex colors to HSV
hsv_colors = [(color, rgb_to_hsv(hex_to_rgb(color))) for color in hexvals]

# Sort colors by hue
sorted_colors = [color for color, hsv in sorted(hsv_colors, key=lambda x: x[1][0])]

#build dict from hex values
sorted_colornames_dict = {k: hex_colname_dict[key] for key in sorted_colors}

# save to file
txt2_path = currfile_dir / "turtle_color_names2.txt"

# Open the file
with open(txt2_path, 'w') as file:
    # save the dictionary
    json.dump(sorted_colornames_dict, file)



# hex_colname_dict = {v: k for k, v in colornames_dict.items()}



# # Convert hex colors to HSV
# hsv_colors = [(color, rgb_to_hsv(hex_to_rgb(color))) for color in hexvals]

# # Sort colors by hue
# sorted_colors = [color for color, hsv in sorted(hsv_colors, key=lambda x: x[1][0])]

# #build dict from hex values
# sorted_colornames_dict = {hex_colname_dict[key]:key for key in sorted_colors}

# # save to file
# txt2_path = currfile_dir / "turtle_color_names2.txt"

# # Open the file
# with open(txt2_path, 'w') as file:
#     # save the dictionary
#     json.dump(sorted_colornames_dict, file)

