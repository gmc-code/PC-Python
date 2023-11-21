import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import json


currfile_dir = Path(__file__).parent
txt_path = currfile_dir / "turtle_color_names2.txt"

# Open the file
with open(txt_path, "r") as file:
    # Load the dictionary
    colornames_dict = json.load(file)


# Define colors
colornames = list(colornames_dict.keys())
# hex values
colors = list(colornames_dict.values())

# Create data
data = np.array(colors).reshape(-1, 4)
# Create data
textdata = np.array(colornames).reshape(-1, 4)

# Create a figure and a set of subplots, 6in by 8 in
fig, ax = plt.subplots(figsize=(6.2, 32))
# Create a table and add it to the specified axes
table = plt.table(cellText=textdata, loc="center")

# Set the font and cell colors
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.0, 1.0)  # (1.2, 1.6)

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        cell = table[i, j]
        cell_color = colors[i * 4 + j]
        cell.set_facecolor(cell_color)  # Set cell background color
        # get rgb from hexadecimal
        # r, g, b = int(cell_color[1:3], 16), int(cell_color[3:5], 16), int(cell_color[5:7], 16)
        r, g, b = (
            int(cell_color[1:3], 16) * 16,
            int(cell_color[3:5], 16) * 16,
            int(cell_color[5:7], 16) * 16,
        )
        # Calculate brightness of cell color using standard coefficients used in the luminosity function
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        # Set text color based on brightness
        cell.get_text().set_color("white" if brightness < 128 else "black")
        cell.set_text_props(
            horizontalalignment="center", verticalalignment="center"
        )  # Center the text

# Hide axes
ax.axis("off")

# Adjust figure extent
# plt.tight_layout()

# Save the figure
plt.savefig("colored_table.png", dpi=600)
