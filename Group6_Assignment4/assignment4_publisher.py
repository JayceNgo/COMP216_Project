import paho.mqtt.client as mqtt
import json
import time
from assignment4_util import create_data

BROKER_ADDRESS = "localhost"
BROKER_PORT = 1883
TOPIC = "health/monitoring"
QOS = 0

client = mqtt.Client()

client.connect(BROKER_ADDRESS, BROKER_PORT)

try:
    while True:
        payload = create_data()
        payload["id"] += 1  # Increment id
        message = json.dumps(payload)
        client.publish(TOPIC, message, qos=QOS)
        print("Published message:", message)
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping publisher...")
finally:
    client.disconnect()
