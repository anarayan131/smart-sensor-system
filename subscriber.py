import paho.mqtt.client as mqtt

broker = "mosquitto"

# Subscriber


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

client = mqtt.Client()
client.connect(broker, 1883, 60)
client.subscribe("sensors/temp")

client.on_message = on_message

# client.subscribe("sensors/pressure")
# client.on_message = on_message

client.loop_forever()