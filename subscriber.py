import paho.mqtt.client as mqtt
import time
import socket

broker = "mosquitto"

# Subscriber

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


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")


client.subscribe("sensors/temp")
client.on_message = on_message

# client.subscribe("sensors/pressure")
# client.on_message = on_message

client.loop_forever()