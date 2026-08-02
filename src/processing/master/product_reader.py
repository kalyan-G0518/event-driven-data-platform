from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


class ProductMasterReader:

    def __init__(
        self,
        spark: SparkSession,
        input_path: str = "data/master/products"
    ):
        self.spark = spark
        self.input_path = input_path

    def read(self) -> DataFrame:

        return (
            self.spark.read.parquet(self.input_path)
        )