import logging
import random
import time

from src.config.settings import EVENT_DELAY_SECONDS
from src.ingestion.producer.kafka_producer import KafkaProducer
from src.ingestion.producer.topic_manager import TopicManager
from src.ingestion.simulator.generator import generate_session

logger = logging.getLogger(__name__)


class ProducerService:
    """
    Continuously generates shopping sessions
    and publishes them to Kafka.
    """

    def __init__(self):
        self.topic_manager = TopicManager()
        self.producer = KafkaProducer()

    def publish_session(self):

        user_id = random.randint(100000, 999999)

        events = generate_session(user_id)

        logger.info(
            "Publishing session with %d events.",
            len(events)
        )

        for event in events:
            self.producer.send(event)

        self.producer.flush()

        logger.info("Session published successfully.")

    def run(self):

        logger.info("Starting Producer Service...")

        self.topic_manager.ensure_topic()

        logger.info("Producer Service is running.")

        while True:

            try:
                self.publish_session()

            except Exception:
                logger.exception("Failed to publish session.")

            time.sleep(EVENT_DELAY_SECONDS)