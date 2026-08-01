from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    count,
    sum,
    when,
)


class GoldAggregator:

    @staticmethod
    def aggregate(df: DataFrame) -> DataFrame:
        """
        Generate business metrics
        from Silver events.
        """

        return (

            df

            .groupBy(
                "event_date"
            )

            .agg(

                count("*").alias("total_events"),

                count(
                    when(
                        col("event_type") == "purchase",
                        True
                    )
                ).alias("total_orders"),

                sum("total_amount")
                .alias("gross_revenue")

            )

        )