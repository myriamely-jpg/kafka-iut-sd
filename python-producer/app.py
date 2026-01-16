from kafka import KafkaProducer
import json
import time 

# Define the Kafka broker and topic
broker = 'my-kafka.elyaago18u-dev.svc.cluster.local:9092'
topic = 'my-first-topic'

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=[broker],
   sasl_mechanism='SCRAM-SHA-256',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
     security_protocol='SASL_PLAINTEXT',
     sasl_plain_username='user1',
     sasl_plain_password='t2pJjbfnz3'
)
#producer = KafkaProducer(
 #   bootstrap_servers=[broker],
 #   value_serializer=lambda v: json.dumps(v).encode('utf-8'),
  #  sasl_plain_password = "t2pJjbfnz3",
 #   sasl_plain_username ="user1"

#)
# Define the message to send
message = {
    'key': 'this-is-a-key',
    'value': 'this-is-a-value'
}

i=0
while True : 
    message = { 
        'key' : 'id',
        'value' : i,
        'timestamp' : time.time()}

# Send the message to the Kafka topic
producer.send(topic, value=message)

# Ensure all messages are sent before closing the producer
producer.flush()

print(f"Message sent to topic {topic}")

time.sleep(5)