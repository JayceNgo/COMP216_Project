import paho.mqtt.client as mqtt
import json
from assignment4_util import print_data

# callback function to print received messages
def on_message(client, userdata, message):
    decoded_message = message.payload.decode('utf-8')
    data_dict = json.loads(decoded_message)
    print_data(data_dict)

# create client instance
client = mqtt.Client()

# set callback function
client.on_message = on_message

# connect to broker
client.connect('localhost', 1883)

# subscribe to topic
client.subscribe('health/monitoring')

# print message
print('Subscriber is running...')

# start client loop to receive messages
client.loop_forever()
