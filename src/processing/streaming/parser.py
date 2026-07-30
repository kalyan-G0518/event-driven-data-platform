
from pyspark.sql.types import TimestampType
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, from_json
from src.common.commerce_schema import COMMERCE_EVENT_SCHEMA
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    IntegerType,
    BooleanType,
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

        StructField("event_type", StringType(), True),

        StructField("event_timestamp", TimestampType(), True),

        StructField("ingestion_timestamp", TimestampType(), True),

        StructField("user_id", IntegerType(), True),

        StructField("session_id", StringType(), True),

        StructField("product_id", IntegerType(), True),

        StructField("category", StringType(), True),

        StructField("quantity", IntegerType(), True),

        StructField("unit_price", DoubleType(), True),

        StructField("payment_method", StringType(), True),

        StructField("country", StringType(), True),

        StructField("city", StringType(), True),

        StructField("device", StringType(), True),

        StructField("platform", StringType(), True),

        StructField("event_source", StringType(), True),

        StructField("is_member", BooleanType(), True),
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
                    COMMERCE_EVENT_SCHEMA
                ).alias("data")
            )
            .select("data.*")
        )

        return parsed