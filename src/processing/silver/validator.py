from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class SilverValidator:

    @staticmethod
    def validate(df: DataFrame) -> DataFrame:
        """
        Apply Silver-layer data quality validation.

        Current validations:
        - quantity > 0
        - unit_price >= 0
        - event_id is not null
        - user_id is not null
        - session_id is not null
        """

        return (
            df
            .filter(col("quantity") > 0)
            .filter(col("unit_price") >= 0)
            .filter(col("event_id").isNotNull())
            .filter(col("user_id").isNotNull())
            .filter(col("session_id").isNotNull())
        )