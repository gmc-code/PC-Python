import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import json
import colorsys

currfile_dir = Path(__file__).parent
txt_path = currfile_dir / "turtle_rgb_colornames.txt"

# Open the file
with open(txt_path, 'r') as file:
    # Load the dictionary
    colornames_dict = json.load(file)


colornames = ['red', 'orangered', 'tomato', 'coral', 'salmon', 'darkorange', 'orange', 'goldenrod', 'gold', 'yellow', 'darkgreen', 'forestgreen', 'springgreen', 'lawngreen', 'green', 'navy', 'mediumblue', 'royalblue', 'cornflowerblue', 'skyblue', 'darkviolet', 'purple', 'orchid', 'violet', 'plum', 'deeppink', 'hotpink', 'pink', 'lightpink', 'mistyrose', 'brown', 'saddlebrown', 'chocolate', 'tan', 'wheat', 'black', 'slategrey', 'dimgray', 'lightgray', 'white']


color_dict = {colorname: colornames_dict[colorname] for colorname in colornames}

# Save to file
txt2_path = currfile_dir / "turtle_rgb_colornames_set1.txt"

with open(txt2_path, 'w') as file:
    # Save the dictionary
    json.dump(colornames_dict, file)


##################################

color_dict = {str(tuple(colornames_dict[colorname])): colorname for colorname in colornames}

# Save to file
txt3_path = currfile_dir / "turtle_rgb_colornames_set1.txt"
with open(txt2_path, 'w') as file:
    # Save the dictionary
    json.dump(color_dict, file)

# manually replace "( and )" in text files via ctrl H


