import logging

from src.ingestion.producer.producer_service import ProducerService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

service = ProducerService()

try:
    service.run()

except KeyboardInterrupt:
    print("\nProducer stopped.")