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

# Function to convert RGB to HSV
def rgb_to_hsv(rgb_color):
    return colorsys.rgb_to_hsv(rgb_color[0]/255, rgb_color[1]/255, rgb_color[2]/255)

# Convert hex colors to HSV and create a list of tuples (colorname, hexvalue, hsv)
color_tuples = [(colorname, hexvalue, rgb_to_hsv(hex_to_rgb(hexvalue))) for colorname, hexvalue in colornames_dict.items()]

# Sort colors by hue
sorted_colors = sorted(color_tuples, key=lambda x: x[2][0])

# Build dict from sorted list of tuples
sorted_colornames_dict = {t[0]: t[1] for t in sorted_colors}

# Save to file
txt2_path = currfile_dir / "turtle_color_names2.txt"

# Open the file
with open(txt2_path, 'w') as file:
    # Save the dictionary
    json.dump(sorted_colornames_dict, file)
