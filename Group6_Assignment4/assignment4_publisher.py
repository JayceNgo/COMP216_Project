import paho.mqtt.client as mqtt
import json
from time import sleep
from assignment4_util import create_data, print_data, start_id

# MQTT broker settings
BROKER_ADDRESS = 'localhost'
BROKER_PORT = 1883
TOPIC = 'group6/data'

# Create MQTT client
client = mqtt.Client()

# Connect to broker
client.connect(BROKER_ADDRESS, BROKER_PORT)

# Publish data to the broker
for i in range(5):
    # Create payload
    data = create_data(start_id+i)
    # Convert payload to JSON string
    json_payload = json.dumps(data)
    # Publish message
    client.publish(TOPIC, json_payload)
    # Print message
    print(f"Published message with ID {start_id+i}:")
    print_data(data)
    # Sleep for 1 second
    sleep(1)

# Disconnect from broker
client.disconnect()
