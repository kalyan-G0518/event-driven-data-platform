import logging
import random
import time

from src.config.settings import EVENT_DELAY_SECONDS

from src.ingestion.producer.kafka_producer import (
    KafkaProducer,
)

from src.ingestion.producer.topic_manager import (
    TopicManager,
)

from src.business_engine.simulation.business_simulator import (
    BusinessSimulator,
)

logger = logging.getLogger(__name__)


class ProducerService:
    """
    Continuously generates shopping sessions
    and publishes them to Kafka.
    """

    def __init__(self):

        self.topic_manager = TopicManager()

        self.producer = KafkaProducer()

        self.simulator = BusinessSimulator()

    def publish_session(self):

        events = self.simulator.generate_session()

        logger.info(
            "Publishing session with %d events.",
            len(events),
        )

        for event in events:

            self.producer.send(event)

        self.producer.flush()

        logger.info(
            "Session published successfully."
        )

    def run(self):

        logger.info(
            "Starting Producer Service..."
        )

        self.topic_manager.ensure_topic()

        logger.info(
            "Producer Service is running."
        )

        while True:

            try:

                self.publish_session()

            except Exception:

                logger.exception(
                    "Failed to publish session."
                )

            time.sleep(
                EVENT_DELAY_SECONDS
            )