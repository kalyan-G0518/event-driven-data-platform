
from confluent_kafka.admin import AdminClient, NewTopic

from src.config.settings import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
)


def create_topic():
    admin = AdminClient(
        {
            "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS
        }
    )

    metadata = admin.list_topics(timeout=5)

    if KAFKA_TOPIC in metadata.topics:
        print(f"Topic '{KAFKA_TOPIC}' already exists.")
        return

    topic = NewTopic(
        KAFKA_TOPIC,
        num_partitions=3,
        replication_factor=1,
    )

    futures = admin.create_topics([topic])

    for _, future in futures.items():
        future.result()

    print(f"Created topic '{KAFKA_TOPIC}'")