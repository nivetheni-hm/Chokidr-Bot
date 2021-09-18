import logging
import json
import time
from kafka import KafkaProducer
from nanoid import generate
import ipfshttpclient
import incident_block

producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

import ipfshttpclient
client = ipfshttpclient.connect("/ip4/127.0.0.1/tcp/5002")

res = client.add_json(incident_block.IIncident)
print(res)

# Producing the messages to incident_manager topic
def kafka_producer(producer, hash):
    producer.send('incident_manager_topic', hash)
    # producer.send('incident_manager', {"incident_id": "1002", "incident_type": "fire", "organisation_DID": "101", "location_id": "10001", "timestamp": "1594823427.159446"})
    # producer.send('incident_manager', {"incident_id": "1003", "incident_type": "collision", "organisation_DID": "102", "location_id": "10002", "timestamp": "1594823428.159446"})
    # producer.send('incident_manager', {"incident_id": "1004", "incident_type": "fire", "organisation_DID": "102", "location_id": "10002", "timestamp": "1594823429.159446"})
    producer.flush()

logging.basicConfig(
    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
    '%(levelname)s:%(process)d:%(message)s',
    level=logging.INFO
)   


kafka_producer(producer, res)