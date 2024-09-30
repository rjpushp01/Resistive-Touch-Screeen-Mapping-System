import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import serial
import pyautogui
import time


# Function to convert a string expression to a numerical function using SymPy
def str_to_func(expr_str, var='x'):
    x = sp.symbols(var)
    expr = sp.sympify(expr_str)
    return sp.lambdify(x, expr)


# Function to plot and highlight grid cells
def plot_func_with_grid(func_str, grid_size=0.0002):
    # Convert string to SymPy function
    f = str_to_func(func_str)
   
    # Generate x values
    x = np.linspace(-5, 5, 1000)  # Adjust as needed for different function domains
    y = f(x)
   
    # Close all open figures
    plt.close('all')


    # Set the overall figure size
    plt.figure(figsize=(10, 10))


    # Plot the function
    plt.plot(x, y, label=f'Function: {func_str}')
    plt.title(f'Plot of {func_str} with Highlighted Grid Cells')


    # Customize the grid
    plt.grid(False)  # Turn off the default grid


    # List to store the locations of the red grid cells
    red_grid_cells = []


    # Draw the grid and highlight cells where the function is present
    for x_i in np.arange(min(x), max(x), grid_size):
        for y_i in np.arange(min(y), max(y), grid_size):
            # Check if any point of the function falls within this cell
            in_cell = ((x >= x_i) & (x < x_i + grid_size) & (y >= y_i) & (y < y_i + grid_size)).any()
            if in_cell:
                # Highlight the cell
                plt.gca().add_patch(plt.Rectangle((x_i, y_i), grid_size, grid_size,
                                                  edgecolor='red', facecolor='none', linewidth=1.5))
                # Store the location of the red grid cell
                red_grid_cells.append((x_i, y_i))


    # Plot regular grid lines
    for xi in np.arange(min(x), max(x), grid_size):
        plt.axvline(x=xi, color='gray', linestyle='--', linewidth=0.5)
    for yi in np.arange(min(y), max(y), grid_size):
        plt.axhline(y=yi, color='gray', linestyle='--', linewidth=0.5)


    # Set the limits and labels
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()


    # Display the plot
    plt.show()


    # Close the figure to release memory
    plt.close('all')


    # Calculate the number of cells along the x-axis and y-axis
    num_x_cells = int((max(x) - min(x)) / grid_size)
    num_y_cells = int((max(y) - min(y)) / grid_size)


    # Calculate the total number of cells
    total_cells = num_x_cells * num_y_cells


    # Print the number of total grid cells
    print(f"Total number of grid cells: {total_cells}")


    # Print the locations of the red grid cells
    print("Red grid cell locations (xi, yi):")
    for cell in red_grid_cells:
        print(cell)


# Function to read function string from Arduino
def read_function_from_arduino():
    ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's serial port
    time.sleep(2)  # Allow time for serial communication to establish
   
    if ser.in_waiting > 0:
        function_str = ser.readline().decode('utf-8').strip()
        print("Received function string:", function_str)
        return function_str
    else:
        return None


# Main program loop
if __name__ == "__main__":
    while True:
        # Read function string from Arduino
        func_str = read_function_from_arduino()
       
        if func_str:
            # Plot the function and grid
            plot_func_with_grid(func_str, grid_size=0.1)
           
            # Example: Perform action based on the received function string
            pyautogui.typewrite(func_str)
            pyautogui.press('enter')
