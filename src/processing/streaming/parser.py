from pyspark.sql import DataFrame
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    IntegerType,
)


class EventParser:
    """
    Parses Kafka JSON messages into
    structured Spark DataFrames.
    """

    @staticmethod
    def schema() -> StructType:
        """
        Spark schema matching CommerceEvent.
        """

        return StructType([
            StructField("event_id", StringType(), True),
            StructField("timestamp", StringType(), True),
            StructField("event_type", StringType(), True),

            StructField("user_id", StringType(), True),
            StructField("session_id", StringType(), True),

            StructField("product_id", StringType(), True),
            StructField("category", StringType(), True),

            StructField("price", DoubleType(), True),
            StructField("quantity", IntegerType(), True),

            StructField("payment_method", StringType(), True),
        ])

    @classmethod
    def parse(cls, kafka_df: DataFrame) -> DataFrame:
        """
        Converts Kafka binary payload into
        structured columns.
        """

        parsed = (
            kafka_df
            .selectExpr("CAST(value AS STRING) AS json")
            .select(
                from_json(
                    col("json"),
                    cls.schema()
                ).alias("data")
            )
            .select("data.*")
        )

        return parsed