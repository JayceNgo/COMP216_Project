import json
import paho.mqtt.client as mqtt
from group_6_util import group_6_util

class subscriber:
    def __init__(self, topic='Mall Traffic per Hour'):
        self.client = mqtt.Client()
        self.client.on_message = subscriber.message_handler
        self.client.connect('localhost', 1883)
        self.client.subscribe(topic)
        self.group_6_util = group_6_util()
        print(f'Subscriber listening to : {topic}\n...')
    
    @staticmethod
    def message_handler(client, userdat, message):       #handler for on_message
        decoded_message = message.payload.decode('utf-8')
        message_dict = json.loads(decoded_message)
        group_6_util.print_data(message_dict)

    def block(self):
        self.client.loop_forever()

sub = subscriber()
sub.block()