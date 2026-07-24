from pyspark.sql import DataFrame
from pyspark.sql import SparkSession


class KafkaReader:
    """
    Reads streaming events from Kafka.
    """

    def __init__(
        self,
        spark: SparkSession,
        bootstrap_servers: str = "localhost:9092",
        topic: str = "commerce-events",
    ):
        self.spark = spark
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic

    def read_stream(self) -> DataFrame:
        """
        Returns a streaming DataFrame
        connected to the Kafka topic.
        """

        df = (
            self.spark.readStream
            .format("kafka")
            .option("kafka.bootstrap.servers", self.bootstrap_servers)
            .option("subscribe", self.topic)
            .option("startingOffsets", "latest")
            .load()
        )

        return df