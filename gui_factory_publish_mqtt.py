import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt
import time

# MQTT Broker Configurations
mqtt_broker = "public.mqtthq.com"  # Change this to your MQTT broker address
mqtt_port = 1883
mqtt_topic_slider = "iiot_training/factory/temperature_setpoint"
mqtt_topic_toggle = "iiot_training/factory/machine_command"

# MQTT Client Setup
client = mqtt.Client("FactoryController")
#client.connect(mqtt_broker, mqtt_port)

# Function to handle temperature_setpoint movement
def temperature_setpoint_changed(event):
    pass

# Function to handle toggle button
def machine_command_changed():
    pass

# Function to publish data every 1 second
def publish_data():
    slider_value = temperature_setpoint.get()
    toggle_value = machine_command_var.get()
    
    print(slider_value, " : ", toggle_value)
    try:
        client.connect(mqtt_broker, mqtt_port)
        client.publish(mqtt_topic_slider, slider_value)
        client.publish(mqtt_topic_toggle, str(int(toggle_value)))
    except Exception as e:
        print("Error : ", e)
    
    root.after(1000, publish_data)

# GUI Setup
root = tk.Tk()
root.title("IIoT Factory Controller")
root.geometry("400x150")

# Style for the widgets
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#333", foreground="#fff", padding=10)
style.configure("TButton", background="#555", foreground="#fff")

# temperature_setpoint
temperature_setpoint_frame = ttk.Frame(root, padding="10")
temperature_setpoint_frame.pack(fill="x", padx=10, pady=10)

ttk.Label(temperature_setpoint_frame, text="Temperature Setpoint", style="TLabel").pack(side="left")

temperature_setpoint = ttk.Scale(temperature_setpoint_frame, from_=0, to=100, orient="horizontal", length=200)
temperature_setpoint.pack(side="left", padx=10)

# machine_command Button
machine_command_frame = ttk.Frame(root, padding="10")
machine_command_frame.pack(fill="x", padx=10, pady=10)

ttk.Label(machine_command_frame, text="Machine Command", style="TLabel").pack(side="left")

machine_command_var = tk.BooleanVar()
machine_command_button = ttk.Checkbutton(machine_command_frame, text="Toggle", variable=machine_command_var)
machine_command_button.pack(side="left", padx=10)

# Start publishing data every 1 second
publish_data()

# Run Tkinter event loop
root.mainloop()
