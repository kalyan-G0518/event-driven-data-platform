from src.processing.streaming.spark_session import SparkSessionBuilder
from src.processing.streaming.kafka_reader import KafkaReader
from src.processing.streaming.parser import EventParser
from src.processing.bronze.bronze_writer import BronzeWriter


class StreamingPipeline:
    """
    End-to-end streaming pipeline.

    Kafka
        ↓
    Spark
        ↓
    Parser
        ↓
    Bronze
    """

    def __init__(self):
        self.spark = SparkSessionBuilder.create()

    def run(self):
        print("Reading from Kafka...")

        reader = KafkaReader(self.spark)

        raw_df = reader.read_stream()

        print("Parsing events...")

        parsed_df = EventParser.parse(raw_df)

        print("Writing to Bronze layer...")

        writer = BronzeWriter()

        query = writer.write(parsed_df)

        print("Streaming started...")

        query.awaitTermination()