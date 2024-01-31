import tkinter as tk
from tkinter import ttk
import paho.mqtt.client as mqtt

# MQTT Broker Configurations
mqtt_broker = "public.mqtthq.com"  # Change this to your MQTT broker address
mqtt_port = 1883
mqtt_topic = "/iiot_training/slider/value"

def on_connect(client, userdata, flags, rc):
    print("Connected.")

# MQTT Client Setup
client = mqtt.Client("SliderPublisher")
client.on_connect = on_connect
while True:
    try:
        client.connect(mqtt_broker, mqtt_port, 60)
        client.publish(mqtt_topic+'/connection/', "Hello")
        break
    except Exception as e:
        print("Error : ", e)

# Function to handle slider movement
def slider_changed(event):
    global client
    slider_value = slider.get()

    client.connect(mqtt_broker, mqtt_port)
    client.publish(mqtt_topic, 10)

# GUI Setup
root = tk.Tk()
root.title("Slider Publisher")

# Slider
slider = ttk.Scale(root, from_=0, to=100, orient="horizontal")
slider.bind("<ButtonRelease-1>", slider_changed)
slider.pack(pady=20)

# Run Tkinter event loop
root.mainloop()
