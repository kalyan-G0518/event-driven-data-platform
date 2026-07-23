from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parents[2]

# Kafka
KAFKA_BOOTSTRAP_SERVERS = "localhost:9092"
KAFKA_TOPIC = "commerce-events"

# Simulator
EVENT_DELAY_SECONDS = 1