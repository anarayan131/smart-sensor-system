import time
import random

while True:
    temp = round(random.uniform(20, 30), 2)
    pressure = round(random.uniform(1,5),3)
    print(f"Temperature: {temp} °C")
    print(f"Pressure: {pressure} Pa")
    time.sleep(2)
