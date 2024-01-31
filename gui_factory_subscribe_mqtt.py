import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt

# MQTT Broker Configurations
mqtt_broker = "public.mqtthq.com"  # Change this to your MQTT broker address
mqtt_port = 1883
mqtt_topic_slider = "iiot_training/factory/temperature_setpoint"
mqtt_topic_toggle = "iiot_training/factory/machine_command"

# MQTT Client Setup
client = mqtt.Client("FactorySubscriber")
client.connect(mqtt_broker, mqtt_port)

# Function to handle MQTT messages
def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload.decode("utf-8")
    if topic == mqtt_topic_slider:
        update_slider_value(payload)
    elif topic == mqtt_topic_toggle:
        update_toggle_value(payload)

# Function to update slider value
def update_slider_value(value):
    slider_textbox.delete(1.0, "end")
    slider_textbox.insert("end", value)

# Function to update toggle value
def update_toggle_value(value):
    toggle_textbox.delete(1.0, "end")
    toggle_textbox.insert("end", value)

# GUI Setup
root = tk.Tk()
root.title("IIoT Factory Monitor")
root.geometry("400x200")

# Style for the widgets
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#333", foreground="#fff", padding=10)

# Slider Text Box
slider_frame = ttk.Frame(root, padding="10")
slider_frame.pack(fill="x", padx=10, pady=10)

ttk.Label(slider_frame, text="Slider Input", style="TLabel").pack(side="left")

slider_textbox = tk.Text(slider_frame, height=1, width=10)
slider_textbox.pack(side="left", padx=10)

# Toggle Text Box
toggle_frame = ttk.Frame(root, padding="10")
toggle_frame.pack(fill="x", padx=10, pady=10)

ttk.Label(toggle_frame, text="Toggle Input", style="TLabel").pack(side="left")

toggle_textbox = tk.Text(toggle_frame, height=1, width=10)
toggle_textbox.pack(side="left", padx=10)

# Subscribe to MQTT topics
client.on_message = on_message
client.subscribe([(mqtt_topic_slider, 0), (mqtt_topic_toggle, 0)])

# Run MQTT client loop
client.loop_start()

# Run Tkinter event loop
root.mainloop()
