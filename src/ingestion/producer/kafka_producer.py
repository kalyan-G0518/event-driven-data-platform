import json

from confluent_kafka import Producer

from src.config.settings import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
)


class KafkaProducer:

    def __init__(self):
        self.producer = Producer(
            {
                "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS
            }
        )

    def _delivery_report(self, err, msg):
        if err is not None:
            print(f"❌ Delivery failed: {err}")
        else:
            print(
                f"✅ Sent to {msg.topic()} "
                f"[Partition {msg.partition()}]"
            )

    def send(self, event):
        payload = event.model_dump(mode="json")

        self.producer.produce(
            topic=KAFKA_TOPIC,
            value=json.dumps(payload),
            callback=self._delivery_report,
        )

        # Trigger callbacks
        self.producer.poll(0)

    def flush(self):
        self.producer.flush()