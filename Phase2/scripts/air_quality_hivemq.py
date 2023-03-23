# Import the necessary libraries
import time
import paho.mqtt.client as mqtt

TOPIC="nist/psiap/ai3/air_quality"

# Define the on_connect function to be called when the client connects to the MQTT broker
def on_connect(client, userdata, flags, rc, properties=None):
    print("MQTT broker connected!")

# Define the on_subscribe function to be called when the client subscribes to a topic
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("topic subscribed!")

# Define the on_message function to be called when a message is received on a subscribed topic
def on_message(client, userdata, msg):
    print(msg.topic + ":\t" + str(msg.payload))

# Create an MQTT client instance
client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)

# Set the client callbacks
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

# Set the client TLS version and credentials
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("nistai3", "nistpscrai3")

# Connect to the MQTT broker
client.connect("030a29b11d714f4dae6fb60c9ab4a2c5.s1.eu.hivemq.cloud", 8883)

# Subscribe to a topic

client.subscribe(TOPIC, qos=1)

# Enter the client network loop and begin listening for messages
client.loop_forever()
