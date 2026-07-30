from pyspark.sql import DataFrame
from pyspark.sql import SparkSession

from src.common.commerce_schema import COMMERCE_EVENT_SCHEMA


class SilverReader:

    def __init__(
        self,
        spark: SparkSession,
        input_path="data/bronze"
    ):
        self.spark = spark
        self.input_path = input_path

    def read(self) -> DataFrame:

        return (
            self.spark
            .readStream
            .schema(COMMERCE_EVENT_SCHEMA)
            .parquet(self.input_path)
        )