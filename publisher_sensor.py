import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
import random
import socket

# Publisher

broker = "mosquitto"

max_retries = 5
wait_seconds = 2

client = mqtt.Client()

for attemp in range(max_retries):
    try:
        client.connect(broker, 1883, 60)
        print("Connected to MQTT broker")
        break #Successful connection
    except (ConnectionRefusedError, socket.error):
        print(f"Connection failed, retrying in {wait_seconds} seconds... ({attemp + 1}/{max_retries})")
        time.sleep(wait_seconds)

else:
    print("Failed to connect to MQTT broker after multiple attempts.")
    exit(1) 

# Publish temperature and pressure data
while True:
    temp = round(random.uniform(20, 30), 2)
    pressure = round(random.uniform(1,5), 3)

    client.publish("sensors/temp", f"{temp}")
    print(f"Sent T: {temp}", flush=True)

    client.publish("sensors/pressure", f"{pressure}")
    print(f"Sent P: {pressure}", flush=True)

    time.sleep(2)
