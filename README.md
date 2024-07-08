# Wireless UAV Link Budget Analysis Tool

## Overview

The **Wireless UAV Link Budget Analysis Tool** is a Python application designed to assist in the analysis and visualization of the link budget for UAV assistive wireless communication systems. It provides a user-friendly interface built with Tkinter for inputting various communication parameters and utilizes Matplotlib to plot the link margin against distance.

## Features

- **User Input Fields**: Enter values for distance, transmit power, transmit antenna gain, receive antenna gain, wavelength, and minimum acceptable signal power.
- **Graphical Output**: Visualize the link margin over different distances with an interactive plot.
- **Error Handling**: Ensures valid numeric input for all fields.
- **Clear Labels**: Input fields and labels provide clear instructions and units for each parameter.

## How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/kayteekay1412/Link-Budget-Analysis.git
    cd Link-Budget-Analysis
    ```

2. **Install Dependencies**:
    Ensure you have the required libraries installed:
    ```bash
    pip install tkinter matplotlib numpy
    ```

3. **Run the Application**:
    ```bash
    python Final_mod_linkbudget.py
    ```

4. **Enter Parameters**:
    - Enter the distance of the drone in meters.
    - Enter the transmit power in watts.
    - Enter the transmit antenna gain in dB.
    - Enter the receive antenna gain in dB.
    - Enter the wavelength in meters.
    - Enter the minimum acceptable signal power in dBm.

5. **Plot the Graph**:
    - Click the "Plot Graph" button to visualize the link margin versus distance.

## Example

Here is an example of how to use the tool:

1. **Enter the Distance of the Drone in meters**: e.g., 10
2. **Enter Transmit Power in watts**: e.g., 10
3. **Enter Transmit Antenna Gain in dB**: e.g., 10
4. **Enter Receive Antenna Gain in dB**: e.g., 10
5. **Enter Wavelength in meters**: e.g., 0.024
6. **Enter Minimum Acceptable Signal Power in dBm**: e.g., -100

Click the "Plot Graph" button to see the link margin over different distances.

---
