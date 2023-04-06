import random
import time
from typing import Dict

start_id = 111

def create_data() -> Dict[str, any]:
    global start_id
    start_id += 1
    patient = f'Patient {random.randint(1, 100)}'
    data = {
        'id': start_id,
        'patient': patient,
        'time': time.asctime(),
        'heart_rate': int(random.gauss(80, 1)),
        'respiratory_rate': int(random.gauss(12, 2)),
        'heart_rate_variability': 65,
        'body_temperature': random.gauss(99, 0.5),
        'blood_pressure': {
            'systolic': int(random.gauss(105, 2)),
            'diastolic': int(random.gauss(70, 1))
        },
        'activity': random.choice(['Walking', 'Running', 'Cycling', 'Swimming'])
    }
    return data

def print_data(data: Dict[str, any]) -> None:
    print(f"ID: {data['id']}")
    print(f"Patient: {data['patient']}")
    print(f"Time: {data['time']}")
    print(f"Heart rate: {data['heart_rate']}")
    print(f"Respiratory rate: {data['respiratory_rate']}")
    print(f"Heart rate variability: {data['heart_rate_variability']}")
    print(f"Body temperature: {data['body_temperature']}")
    print(f"Blood pressure (systolic): {data['blood_pressure']['systolic']}")
    print(f"Blood pressure (diastolic): {data['blood_pressure']['diastolic']}")
    print(f"Activity: {data['activity']}")
