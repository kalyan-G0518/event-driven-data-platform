from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType,
    BooleanType,
    TimestampType,
)

COMMERCE_EVENT_SCHEMA = StructType([
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