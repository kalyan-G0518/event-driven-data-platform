from pyspark.sql import DataFrame
from pyspark.sql import SparkSession


class GoldReader:

    def __init__(
        self,
        spark: SparkSession,
        input_path: str = "data/silver"
    ):
        self.spark = spark
        self.input_path = input_path

    def read(self) -> DataFrame:
        """
        Read the latest Silver dataset.
        """

        return (
            self.spark
            .read
            .parquet(self.input_path)
        )