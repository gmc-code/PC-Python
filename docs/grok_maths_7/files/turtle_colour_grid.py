import matplotlib.pyplot as plt
import numpy as np


# Define colors
colornames = [
    ["red", "orangered", "tomato", "coral", "salmon"],
    ["darkorange", "orange", "goldenrod", "gold", "yellow"],
    ["darkgreen", "forestgreen", "springgreen", "lawngreen", "green"],
    ["navy", "mediumblue", "royalblue", "cornflowerblue", "skyblue"],
    ["darkviolet", "purple", "orchid", "violet", "plum"],
    ["deeppink", "hotpink", "pink", "lightpink", "mistyrose"],
    ["brown", "saddlebrown", "chocolate", "tan", "wheat"],
    ["black", "slategrey", "dimgray", "lightgray", "white"]
]
#hex values
colors = [
    "#FF0000", "#FF4500", "#FF6347", "#FF7F50", "#FA8072",
    "#FF8C00", "#FFA500", "#DAA520", "#FFD700", "#FFFF00",
    "#013220", "#228B22", "#00FF7F", "#7CFC00", "#00FF00",
    "#000080", "#0000CD", "#002366", "#6495ED", "#87CEEB",
    "#9400D3", "#800080", "#DA70D6", "#EE82EE", "#DDA0DD",
    "#FF1493", "#FF69B4", "#FFC0CB", "#FFB6C1", "#FFE4E1",
    "#A52A2A", "#8B4513", "#D2691E", "#D2B48C", "#F5DEB3",
    "#000000", "#708090", "#696969", "#D3D3D3", "#FFFFFF"
]

# Create data
data = np.array(colors).reshape(-1, 5)
# Create data
textdata = np.array(colornames).reshape(-1, 5)

# Create a figure and a set of subplots, 6in by 8 in
fig, ax = plt.subplots(figsize=(6, 2.9))
# Create a table and add it to the specified axes
table = plt.table(cellText=textdata, loc='center')

# Set the font and cell colors
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.6)
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        cell = table[i, j]
        cell_color = colors[i*5+j]
        cell.set_facecolor(cell_color)  # Set cell background color
        # get rgb from hexadecimal
        r, g, b = int(cell_color[1:3], 16), int(cell_color[3:5], 16), int(cell_color[5:7], 16)
        # Calculate brightness of cell color using standard coefficients used in the luminosity function
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        # Set text color based on brightness
        cell.get_text().set_color("white" if brightness < 128 else "black")
        cell.set_text_props(horizontalalignment='center', verticalalignment='center')  # Center the text

# Hide axes
ax.axis('off')

# Adjust figure extent
plt.tight_layout()

# Save the figure
plt.savefig("colored_table.png", dpi=600)

