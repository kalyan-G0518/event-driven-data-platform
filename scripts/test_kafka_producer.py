from src.ingestion.producer.kafka_producer import KafkaProducer
from src.ingestion.simulator.generator import generate_session

producer = KafkaProducer()

for event in generate_session(user_id=1):
    producer.send(event)

producer.flush()