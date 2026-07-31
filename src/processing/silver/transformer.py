from pyspark.sql import DataFrame
from pyspark.sql.functions import col, to_date, hour


class SilverTransformer:

    @staticmethod
    def transform(df: DataFrame) -> DataFrame:
        """
        Apply Silver-layer transformations.

        Current transformations:
        - Add event_date
        - Add event_hour
        - Add total_amount
        """

        return (
            df
            .withColumn("event_date", to_date(col("event_timestamp")))
            .withColumn("event_hour", hour(col("event_timestamp")))
            .withColumn(
                "total_amount",
                col("quantity") * col("unit_price")
            )
        )