from kafka import KafkaConsumer
import json

# Define the Kafka broker and topic
broker = 'my-kafka.elyaago18u-dev.svc.cluster.local:9092'
topic = 'my-first-topic'

# Create a Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[broker],
    security_protocol='SASL_PLAINTEXT',
    sasl_mechanism='SCRAM-SHA-256',
    sasl_plain_username='user1',
    sasl_plain_password='t2pJjbfnz3',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print(f"Listening to topic {topic}")

# Poll messages from the Kafka topic
for message in consumer:
    print(f"Received message: {message.value}")