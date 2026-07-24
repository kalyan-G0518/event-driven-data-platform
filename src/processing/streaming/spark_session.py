from pyspark.sql import SparkSession


class SparkSessionBuilder:
    """
    Creates and configures a Spark Session
    for Structured Streaming with Kafka.
    """

    @staticmethod
    def create() -> SparkSession:
        spark = (
            SparkSession.builder
            .appName("EventDrivenDataPlatform")
            .master("local[*]")
            .config(
                "spark.jars.packages",
                "org.apache.spark:spark-sql-kafka-0-10_2.13:4.2.0"
            )
            .config("spark.sql.shuffle.partitions", "4")
            .getOrCreate()
        )

        spark.sparkContext.setLogLevel("WARN")

        return spark