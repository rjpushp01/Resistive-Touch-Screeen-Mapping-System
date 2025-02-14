# Resistive Touch Screen Mapping System

## Overview
This project implements a resistive touch screen system that enables users to create maps based on their touch inputs. The system utilizes an Arduino, Raspberry Pi, and Python-based visualization to capture and analyze touch data, which is then processed into a graphical representation.

## Features
- **Touch Data Collection**: Uses a resistive touch screen to collect user input.
- **Real-Time Graphing**: Captures touch coordinates and visualizes them on a plotted grid.
- **Function Recognition**: Detects predefined mathematical functions based on user input.
- **Serial Communication**: Uses an Arduino to send data to a Raspberry Pi or a PC for processing.
- **GPIO-Controlled Function Selection**: Switches on the Raspberry Pi select mathematical functions for visualization.

## Components Used

### Hardware
- **Resistive Touch Screen**: Captures user touch data.
- **Arduino**: Reads touch screen inputs and sends data via serial communication.
- **Raspberry Pi**: Processes received data and handles visualization.
- **Switches (GPIO)**: Selects predefined functions.

### Software
- **Arduino IDE**: For programming the Arduino.
- **Python (Matplotlib, NumPy, SymPy, PyAutoGUI, Serial, RPi.GPIO)**: For data processing and visualization.

## File Structure
- **`proto_arduino.ino`**: Arduino script for reading touch inputs and sending them via serial communication.
- **`Arduino_pyth.py`**: Python script for receiving function strings from Arduino, processing, and plotting data.
- **`Graph plotting for the user input.py`**: Script for plotting a mathematical function and highlighting grid cells.
- **`RPI.py`**: Raspberry Pi script for handling GPIO switch inputs to select functions and visualize data.

## How It Works

### 1. Capturing Touch Inputs
- The resistive touch screen captures user input.
- The Arduino processes the touch signals and determines the corresponding function or coordinate data.
- The processed data is sent to the Raspberry Pi via serial communication.

### 2. Processing the Data
- The Raspberry Pi receives function strings or coordinate data.
- It processes the input using NumPy and SymPy.
- The data is visualized as a 2D graph using Matplotlib.

### 3. Function Selection via GPIO (Raspberry Pi)
- Physical switches are assigned to different mathematical functions (e.g., `sin(x)`, `cos(x)`, `x^2`).
- When a switch is pressed, the corresponding function is plotted.

## Setup Instructions

### 1. Hardware Setup
- Connect the resistive touch screen to the Arduino.
- Connect the Arduino to the Raspberry Pi via a serial interface.
- Connect switches to the GPIO pins of the Raspberry Pi.

### 2. Software Setup

#### **Arduino**
1. Upload `proto_arduino.ino` to the Arduino board.

#### **Python Environment**
1. Install required libraries:
   ```sh
   pip install matplotlib numpy sympy pyautogui serial RPi.GPIO

