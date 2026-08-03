from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, concat_ws


class CustomerMasterReader:

    def __init__(
        self,
        spark: SparkSession,
        input_path="data/master/customers"
    ):
        self.spark = spark
        self.input_path = input_path

    def read(self) -> DataFrame:

        return (
            self.spark
            .read
            .parquet(self.input_path)

            .withColumnRenamed("customer_id", "user_id")

            .withColumn(
                "customer_name",
                concat_ws(
                    " ",
                    col("first_name"),
                    col("last_name")
                )
            )

            .withColumnRenamed(
                "membership",
                "membership_type"
            )
        )