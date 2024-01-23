import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Load data from the file
data = np.loadtxt("session_1_5112018105323.txt", skiprows=14)

# Create an array for indexing
uind = np.arange(300)

# Calculate the cumulative sum of the second column of data
ut = np.cumsum(data[uind, 1])

# Create boundaries for the perimeter
boundary = patches.Rectangle((-12.5, -12.5), 25, 25, linewidth=1, edgecolor='black', facecolor='none')

# Define the positions and properties of the pillars
pillar_positions = [(-7.5, 2.5), (-7.5, -7.5), (2.5, 2.5), (2.5, -7.5)]
pillar_colors = ['yellow', 'blue', 'red', 'green']

# Create a list to hold pillar patches
pillar_patches = []

# Create pillar rectangles and add them to the list
for position, color in zip(pillar_positions, pillar_colors):
    pillar = patches.Rectangle(position, 5, 5, linewidth=1, edgecolor=color, facecolor='none')
    pillar_patches.append(pillar)

# Plot the 3rd and 4th columns (x and y coordinates)
fig, ax = plt.subplots()
plt.plot(data[uind, 2], data[uind, 3], marker='o', markeredgecolor='orange', markerfacecolor='orange', markevery=[-1])

# Annotate the numbers 1-6 on the graph
annotations = ["1", "2", "3", "4", "5", "6"]
annotation_positions = [(-5, -8.5), (-8.5, 5), (7.5, -5), (5, 7.5), (5, 1.5), (-5, -2.5)]

for annotation, position in zip(annotations, annotation_positions):
    plt.annotate(annotation, position)

# Add the boundary and pillars to the plot
ax.add_patch(boundary)
for pillar_patch in pillar_patches:
    ax.add_patch(pillar_patch)

# Show the plot
plt.show()
