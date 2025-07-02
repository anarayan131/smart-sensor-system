import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time
import random

# Publisher

broker = "mosquitto"

client = mqtt.Client()
client.connect(broker, 1883, 60)

while True:
    temp = round(random.uniform(20, 30), 2)
    pressure = round(random.uniform(1,5), 3)

    client.publish("sensors/temp", f"{temp}")
    print(f"Sent T: {temp}", flush=True)


    # publish.single("sensors/pressure", f"{pressure}", hostname="localhost")
    # print(f"Sent P: {pressure}", flush=True)

    # print(f"Pressure: {pressure} Pa", flush=True)
    time.sleep(2)
