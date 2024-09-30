import matplotlib.pyplot as plt
import numpy as np
import math


# Close all open figures
plt.close('all')


# Turn off interactive mode
plt.ioff()


# Sample data
x = np.linspace(0, math.pi, 1000)  # Increased points for better resolution
y = np.sin(x)


# Set the overall figure size
plt.figure(figsize=(10, 5))


# Plot the sine wave
plt.plot(x, y, label='Sine Wave')
plt.title('Sine Wave with Highlighted Grid Cells')


# Customize the grid
plt.grid(False)  # Turn off the default grid


# Define grid size
grid_size = 0.0002


# List to store the locations of the red grid cells
red_grid_cells = []


# Draw the grid and highlight cells where the sine wave is present
for xi in np.arange(0, math.pi, grid_size):
    for yi in np.arange(-1, 1, grid_size):
        # Check if any point of the sine wave falls within this cell
        in_cell = ((x >= xi) & (x < xi + grid_size) & (y >= yi) & (y < yi + grid_size)).any()
        if in_cell:
            # Highlight the cell
            plt.gca().add_patch(plt.Rectangle((xi, yi), grid_size, grid_size,
                                              edgecolor='red', facecolor='none', linewidth=1.5))
            # Store the location of the red grid cell
            red_grid_cells.append((xi, yi))


# Plot regular grid lines
for xi in np.arange(0, math.pi, grid_size):
    plt.axvline(x=xi, color='gray', linestyle='--', linewidth=0.5)
for yi in np.arange(-1, 1, grid_size):
    plt.axhline(y=yi, color='gray', linestyle='--', linewidth=0.5)


# Set the limits and labels
plt.xlim([0, math.pi])
plt.ylim([-1, 1])
plt.xlabel('x (radians)')
plt.ylabel('y')
plt.legend()


plt.show()


# Close the figure to release memory
plt.close('all')


# Print the locations of the red grid cells
# print("Red grid cell locations (xi, yi):")
# for cell in red_grid_cells:
#     print(cell)
# Calculate the number of cells along the x-axis and y-axis
num_x_cells = int((math.pi - 0) / grid_size)
num_y_cells = int((1 - (-1)) / grid_size)


# Calculate the total number of cells
total_cells = num_x_cells * num_y_cells


# Print the number of total grid cells
print(f"Total number of grid cells: {total_cells}")
