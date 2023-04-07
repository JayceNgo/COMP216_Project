import random
import math
import matplotlib.pyplot as plt
import numpy as np
from json import dumps
from time import asctime
import datetime
from group_6_data_generator import MallTrafficGenerator


class group_6_util:
    def __init__(self):
        self.start_id = 111
        self.sensor_id = 1
        self.sensorName = f"Sensor {self.sensor_id}"
        self.location = "Square One"

        self.dataDict = {
            'name': self.sensorName,
             'id': self.start_id,
              'time': asctime(),
              'location': self.location
            }
        self.gen = MallTrafficGenerator()

    def create_data(self):
        self.start_id += 1
        self.sensor_id+=1
        self.dataDict.update({'Customers/Hour':self.gen.plot_traffic()})
        return self.dataDict
    
    def print_data(dataDict):
        print(f'{dataDict} to broker')
