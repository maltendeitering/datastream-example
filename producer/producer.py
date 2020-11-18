from kafka import KafkaProducer
from time import sleep
from json import dumps, load, loads
from datetime import datetime
import pandas as pd
import numpy as np
import os

file = os.environ['FILE']

dir = os.path.dirname(__file__)
filename = os.path.join(dir, 'data', file)

print('Producer started')

#Wait for Kafka to be ready
sleep(30)

df = pd.read_csv(filename)
dfarray = df.to_json(orient="records", lines=True).splitlines()

producer = KafkaProducer(bootstrap_servers=['kafka:29092'], value_serializer = lambda x: dumps(x).encode('utf-8'))

for entry in dfarray:
    json = loads(entry)
    json['timestamp'] = datetime.now().isoformat()
    producer.send('stream', value=entry)
    print('data sent: ', json['timestamp'])
    sleep(1)