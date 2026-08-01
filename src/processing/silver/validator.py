from pyspark.sql import DataFrame
from pyspark.sql.functions import col


class SilverValidator:

    @staticmethod
    def validate(df: DataFrame) -> DataFrame:
        """
        Silver-layer validation.

        Rules:
        - Required IDs must exist
        - Quantity must be positive
        - Price cannot be negative
        - Purchase events require payment_method
        """

        valid_record = (
            (col("quantity") > 0)
            & (col("unit_price") >= 0)
            & col("event_id").isNotNull()
            & col("user_id").isNotNull()
            & col("session_id").isNotNull()
        )

        purchase_rule = (
            (col("event_type") != "purchase")
            | col("payment_method").isNotNull()
        )

        return (
            df
            .filter(valid_record & purchase_rule)
            .dropDuplicates(["event_id"])
        )