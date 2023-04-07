import random
import datetime
from group_6_data_generator import MallTrafficGenerator

start_id = 111


def create_data():
    global start_id
    start_id += 1
    generator = MallTrafficGenerator(intensity=0.5)
    customers = generator.plot_traffic(num_points=12, min_customers=0, max_customers=100)
    payload = {
        "id": start_id,
        "timestamp": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "location": {
            "latitude": round(random.uniform(-90, 90), 6),
            "longitude": round(random.uniform(-180, 180), 6),
            "altitude": round(random.uniform(0, 5000), 1)
        },
        "temperature": round(random.uniform(-40, 50), 1),
        "humidity": round(random.uniform(0, 100), 1),
        "pressure": round(random.uniform(800, 1200), 1),
        "light_level": round(random.uniform(0, 10000), 1),
        "motion_detected": random.choice([True, False]),
        "sound_level": round(random.uniform(0, 100), 1),
        "customers": customers
    }
    return payload


def print_data(payload):
    print(f"ID: {payload['id']}")
    print(f"Timestamp: {payload['timestamp']}")
    print(f"Location: ({payload['location']['latitude']}, {payload['location']['longitude']}) Altitude: {payload['location']['altitude']}")
    print(f"Temperature: {payload['temperature']} C")
    print(f"Humidity: {payload['humidity']} %")
    print(f"Pressure: {payload['pressure']} hPa")
    print(f"Light Level: {payload['light_level']} lux")
    print(f"Motion Detected: {'Yes' if payload['motion_detected'] else 'No'}")
    print(f"Sound Level: {payload['sound_level']} dB")
    print(f"Customers: {payload['customers']}")
