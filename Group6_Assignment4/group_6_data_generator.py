import random
import math
import matplotlib.pyplot as plt
import numpy as np
from json import dumps
import datetime


class MallTrafficGenerator:
    def __init__(self, intensity=0.5):
        self.intensity = intensity  # Normalized intensity (0 to 1)

    def _generate_normalized_value(self):
        # Using Gauss to generate scaled value
        # Generate random value around the intensity using a normal distribution
        value = random.gauss(self.intensity, 0.1)
        # Clip the value to 0-1 range
        value = max(0, min(value, 1))
        return value

    # public property that generates values using private normalized value
    def generate_value(self, min_customers=0, max_customers=100):
        # Generate a normalized value and transform it to the desired range
        normalized_value = self._generate_normalized_value()
        value_range = max_customers - min_customers
        value = min_customers + math.floor(normalized_value * value_range)
        return value

    # method that plots the graph
    def plot_traffic(self, num_points=12, min_customers=0, max_customers=100):
        # Generate the data
        data = [self.generate_value(min_customers=min_customers, max_customers=max_customers) for i in range(num_points)]
        
        # Plot the data
        plt.plot(data)
        plt.xlabel('Time')
        plt.ylabel('Customers')
        plt.title('Mall Traffic')

        plt.gcf().autofmt_xdate()
        # Show the plot
        plt.show()
        
        return dumps(data, indent=2)


generator = MallTrafficGenerator(intensity=0.5)
generator.plot_traffic(num_points=12, min_customers=0, max_customers=100)
