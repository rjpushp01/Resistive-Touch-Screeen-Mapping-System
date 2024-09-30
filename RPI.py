import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pyautogui
import time

# GPIO Pin assignments
switchPin1 = 17  # GPIO pin connected to the switch for sin(x)
switchPin2 = 27  # GPIO pin connected to the switch for cos(x)
switchPin3 = 22  # GPIO pin connected to the switch for x^2
switchPin4 = 23  # GPIO pin connected to the switch for circle x^2 + y^2 = 5
switchPin5 = 24  # GPIO pin connected to the switch for y^2 = 4ax

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
    x = np.linspace(-5, 5, 1000)
    y = f(x)
   
    # Close all open figures
    plt.close('all')

    # Set the overall figure size
    plt.figure(figsize=(10, 10))

    # Plot the function
    plt.plot(x, y, label=f'Function: {func_str}')
    plt.title(f'Plot of {func_str} with Highlighted Grid Cells')

    # Customize the grid
    plt.grid(False)

    # List to store the locations of the red grid cells
    red_grid_cells = []

    # Draw the grid and highlight cells where the function is present
    for x_i in np.arange(min(x), max(x), grid_size):
        for y_i in np.arange(min(y), max(y), grid_size):
            in_cell = ((x >= x_i) & (x < x_i + grid_size) & (y >= y_i) & (y < y_i + grid_size)).any()
            if in_cell:
                plt.gca().add_patch(plt.Rectangle((x_i, y_i), grid_size, grid_size,
                                                  edgecolor='red', facecolor='none', linewidth=1.5))
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

# Function to read which switch was pressed and return the corresponding function string
def read_function_from_gpio():
    if GPIO.input(switchPin1) == GPIO.HIGH:
        return "sin(x)"
    elif GPIO.input(switchPin2) == GPIO.HIGH:
        return "cos(x)"
    elif GPIO.input(switchPin3) == GPIO.HIGH:
        return "x**2"
    elif GPIO.input(switchPin4) == GPIO.HIGH:
        return "sqrt(25 - x**2)"  # Circle equation
    elif GPIO.input(switchPin5) == GPIO.HIGH:
        return "sqrt(4 * 1 * x)"  # y^2 = 4ax where a=1
    else:
        return None

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(switchPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchPin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchPin3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchPin4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchPin5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Main program loop
try:
    while True:
        # Read function string from GPIO switches
        func_str = read_function_from_gpio()
       
        if func_str:
            # Plot the function and grid
            plot_func_with_grid(func_str, grid_size=0.1)

            # Optionally perform an action based on the received function string
            pyautogui.typewrite(func_str)
            pyautogui.press('enter')

        # Small delay to debounce switch input
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program interrupted")

finally:
    GPIO.cleanup()  # Clean up GPIO pins on exit
