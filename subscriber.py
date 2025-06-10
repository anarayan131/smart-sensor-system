import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()}")

client = mqtt.Client()
client.connect("localhost")
client.subscribe("sensors/temp")

client.on_message = on_message

# client.subscribe("sensors/pressure")
# client.on_message = on_message

client.loop_forever()