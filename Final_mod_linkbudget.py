import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define parameters
# distance = 100 # in meters
# transmit_power = 10  # in watts
# transmit_antenna_gain = 10  # in dB 
# receive_antenna_gain = 10  # in dB
# wavelength = 0.024  # in meters
# minimum_acceptable_signal_power = -100  # in dBm

def plot_graph():
    try:
        distance1 = float(input_field.get())
        
        distance = np.arange(distance1, 1000, 10)
        
        tr_pwr = float(input_field1.get())
        
        tr_ant_gain = float(input_field2.get())
        
        re_ant_gain = float(input_field3.get())
        
        WL = float(input_field4.get())
        
        min_acc_sig_pwr = float(input_field5.get())
        
        # Calculate path loss and received signal power
        path_loss = 10 * np.log10((4 * np.pi * distance**2) / (tr_pwr * tr_ant_gain * re_ant_gain * WL**2))
        received_signal_power = tr_pwr + tr_ant_gain + re_ant_gain - path_loss

        # Calculate link margin
        link_margin = received_signal_power - min_acc_sig_pwr

        # Plot results
        fig = plt.figure(figsize=(10, 6))
        plt.plot(distance, link_margin, label='Link Margin (dB)', marker='o', markerfacecolor='red', markevery=10)
        plt.xlabel('Distance (m)')
        plt.ylabel('Link Margin (dB)')
        plt.title('Link Margin vs. Distance')
        plt.grid(True)
        plt.legend()
        plt.show()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()
    except ValueError:
        label2 = tk.Label(root, text="Invalid input. Please enter a numeric value for distance.", font=font_size, fg='red')
        label2.pack(padx=80, pady=20)

root = tk.Tk()
root.title("Wireless_UAV")

font_size = ('Times New Roman', 24, 'bold')
label = tk.Label(root, text="Link Budget Analysis for UAV Assistive Wireless Communication", font=font_size, fg='green')
label1 = tk.Label(root, text="developed by ktk", font=font_size, fg='blue')

# Pack the label to fit the window
font2 = ('Times New Roman', 12)
label.pack(padx=20, pady=20)
label1.pack(padx=20, pady=20)

label2 = tk.Label(root, text="This application can be used for the design and analysis of drone assitive wireless communication system link. Enter your link data with the reference to unit value mentioned, observe the link margin available with respect to different distances", font=font2, fg='purple')
label2.pack(padx=20, pady=20)
# Create input field for distance
input_field = tk.Label(root, text="Enter the Distance of the Drone in metres (For example: 10-1000 metres):", font=font2)
input_field.pack()
input_field = tk.Entry(root, width=20)
input_field.pack()

#Create input field for transmit power
input_field1 = tk.Label(root, text="Enter Transmit power in watts (For example: 10 watts):", font=font2)
input_field1.pack()
input_field1 = tk.Entry(root, width=20)
input_field1.pack()
# input_field1.pack()

#Create input field for transmit antenna gain
input_field2 = tk.Label(root, text="Enter Transmit Antenna Gain in dB (For example: 10 dB):", font=font2)
input_field2.pack()
input_field2 = tk.Entry(root, width=20)
input_field2.pack()
# input_field2 = tk.Label(root, text="(eg. 10 dB)", font=font2)
# input_field2.pack()

#Create input field for receive antenna gain
input_field3 = tk.Label(root, text="Enter Receive Antenna Gain in dB (For example: 10 dB):", font=font2)
input_field3.pack()
input_field3 = tk.Entry(root, width=20)
input_field3.pack()
# input_field3 = tk.Label(root, text="(eg. 10 dB)", font=font2)
# input_field3.pack()

#Create input field for wavelength
input_field4 = tk.Label(root, text="Enter Wavelength in metres (For example: 0.024 metres):", font=font2)
input_field4.pack()
input_field4 = tk.Entry(root, width=20)
input_field4.pack()
# input_field4 = tk.Label(root, text="(eg. 0.024 metres)", font=font2)
# input_field4.pack()

#Create input field for minimum acceptable signal power
input_field5 = tk.Label(root, text="Enter Minimum Acceptable Signal Power in dBm (For example: -100 dBm):", font=font2)
input_field5.pack()
input_field5 = tk.Entry(root, width=20)
input_field5.pack()
# input_field5 = tk.Label(root, text="(eg. -100 dBm)", font=font2)
# input_field5.pack()

# Create plot button
plot_button = tk.Button(root, text="Plot Graph", command=plot_graph, font=font2)
plot_button.pack()

root.mainloop()
