import paho.mqtt.client as mqtt
import json
from assignment4_util import print_data

# MQTT broker settings
BROKER_ADDRESS = 'localhost'
BROKER_PORT = 1883
TOPIC = 'group6/data'

# Define callback function for incoming messages
def on_message(client, userdata, message):
    # Decode message payload from bytes to string
    payload_str = message.payload.decode('utf-8')
    # Convert JSON string to dict
    payload_dict = json.loads(payload_str)
    # Print message
    print(f"Received message on topic {message.topic}:")
    print_data(payload_dict)

# Create MQTT client
client = mqtt.Client()

# Assign on_message callback function
client.on_message = on_message

# Connect to broker
client.connect(BROKER_ADDRESS, BROKER_PORT)

# Subscribe to topic
client.subscribe(TOPIC)

# Print message
print(f"Subscribed to topic {TOPIC}")

# Enter loop to process incoming messages
client.loop_forever()
