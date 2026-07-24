import logging
from confluent_kafka.admin import (
    AdminClient,
    NewTopic
)

from src.config.settings import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
    KAFKA_NUM_PARTITIONS,
    KAFKA_REPLICATION_FACTOR,
)


logger = logging.getLogger(__name__)


class TopicManager:
    """
    Handles Kafka topic management.

    Responsibilities:
        - Connect to Kafka Admin API
        - Check topic existence
        - Create topics
        - Ensure required topics exist
    """

    def __init__(self):
        self.admin_client = AdminClient(
            {
                "bootstrap.servers": KAFKA_BOOTSTRAP_SERVERS
            }
        )

    def topic_exists(self, topic_name: str) -> bool:
        """
        Check whether a topic already exists.
        """

        metadata = self.admin_client.list_topics(timeout=10)

        return topic_name in metadata.topics

    def create_topic(
        self,
        topic_name: str,
        partitions: int = KAFKA_NUM_PARTITIONS,
        replication_factor: int = KAFKA_REPLICATION_FACTOR,
    ) -> None:
        """
        Create a Kafka topic.
        """

        logger.info(f"Creating topic '{topic_name}'...")

        new_topic = NewTopic(
            topic=topic_name,
            num_partitions=partitions,
            replication_factor=replication_factor,
        )

        futures = self.admin_client.create_topics([new_topic])

        future = futures[topic_name]

        future.result()

        logger.info(f"Topic '{topic_name}' created successfully.")

    def ensure_topic(self, topic_name: str = KAFKA_TOPIC) -> None:
        """
        Ensure that the topic exists.
        Creates it only if necessary.
        """

        logger.info(f"Checking topic '{topic_name}'...")

        if self.topic_exists(topic_name):
            logger.info(f"Topic '{topic_name}' already exists.")
            return

        self.create_topic(topic_name)