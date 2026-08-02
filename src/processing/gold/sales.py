from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    sum,
    count,
    avg,
    when,
    round,
)


class SalesAnalytics:
    """
    Builds the Sales Summary
    data mart.
    """

    @staticmethod
    def build(df: DataFrame) -> DataFrame:

        return (

            df

            .groupBy(
                "event_date",
                "event_hour",
                "category"
            )

            .agg(

                round(
                    sum(
                        when(
                            col("event_type") == "purchase",
                            col("total_amount")
                        ).otherwise(0)
                    ),
                    2
                ).alias("revenue"),

                count(
                    when(
                        col("event_type") == "purchase",
                        True
                    )
                ).alias("orders"),

                sum(
                    when(
                        col("event_type") == "purchase",
                        col("quantity")
                    ).otherwise(0)
                ).alias("units_sold"),

                round(
                    avg(
                        when(
                            col("event_type") == "purchase",
                            col("unit_price")
                        )
                    ),
                    2
                ).alias("average_selling_price")

            )

        )