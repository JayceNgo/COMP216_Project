import paho.mqtt.client as mqtt
from time import sleep
from group_6_util import group_6_util
from json import dumps

class publisher:
    def __init__(self, delay=0.75, topic='Mall Traffic per Hour'):
        self.gen = group_6_util()
        self.client = mqtt.Client()
        self.topic = topic
        self.delay = delay
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.publish()

    def stop(self):
        self.running = False

    def publish(self):
        data = dumps(self.gen.create_data())
        print(f'{data} to broker')
        self.client.connect('localhost', 1883)
        self.client.publish(self.topic, payload=data)
        sleep(self.delay)
        self.client.disconnect()

pub = publisher()
pub.start()
