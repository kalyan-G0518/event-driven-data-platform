from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    to_date,
    hour,
    lower,
    upper,
    initcap,
    when,
)


class SilverTransformer:

    @staticmethod
    def transform(df: DataFrame) -> DataFrame:
        """
        Apply Silver-layer transformations.

        Transformations:
        - Derived columns
        - Data normalization
        """

        return (
            df

            # ------------------------
            # Derived Columns
            # ------------------------
            .withColumn("event_date", to_date(col("event_timestamp")))
            .withColumn("event_hour", hour(col("event_timestamp")))
            .withColumn("total_amount", col("quantity") * col("unit_price"))
            .withColumn(
                "is_purchase",
                when(col("event_type") == "purchase", True).otherwise(False)
            )

            # ------------------------
            # Normalization
            # ------------------------
            .withColumn("country", upper(col("country")))
            .withColumn("city", initcap(col("city")))
            .withColumn("device", lower(col("device")))
            .withColumn("platform", lower(col("platform")))
            .withColumn("category", lower(col("category")))
            .withColumn("event_source", lower(col("event_source")))
            .withColumn("event_type", lower(col("event_type")))
        )