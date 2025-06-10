import paho.mqtt.publish as publish
import time
import random

while True:
    temp = round(random.uniform(20, 30), 2)
    pressure = round(random.uniform(1,5),3)

    publish.single("sensors/temp", f"{temp}", hostname="localhost")
    print(f"Sent T: {temp}", flush=True)

    # publish.single("sensors/pressure", f"{pressure}", hostname="localhost")
    # print(f"Sent P: {pressure}", flush=True)

    # print(f"Pressure: {pressure} Pa", flush=True)
    time.sleep(2)
