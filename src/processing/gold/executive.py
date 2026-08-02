from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    count,
    countDistinct,
    sum,
    avg,
    when,
    round,
)


class ExecutiveAnalytics:
    """
    Builds the Executive Summary
    data mart from the Silver layer.
    """

    @staticmethod
    def build(df: DataFrame) -> DataFrame:

        executive_df = (

            df

            .groupBy("event_date")

            .agg(

                # Revenue
                round(
                    sum("total_amount"),
                    2
                ).alias("total_revenue"),

                # Orders
                count(
                    when(
                        col("event_type") == "purchase",
                        True
                    )
                ).alias("total_orders"),

                # Events
                count("*").alias("total_events"),

                # Customers
                countDistinct(
                    "user_id"
                ).alias("unique_customers"),

                # Units Sold
                sum(
                    when(
                        col("event_type") == "purchase",
                        col("quantity")
                    ).otherwise(0)
                ).alias("products_sold"),

                # Average Order Value
                round(
                    avg(
                        when(
                            col("event_type") == "purchase",
                            col("total_amount")
                        )
                    ),
                    2
                ).alias("average_order_value"),

                # Member Purchases
                count(
                    when(
                        (col("event_type") == "purchase") &
                        (col("is_member")),
                        True
                    )
                ).alias("member_orders")
            )

        )

        executive_df = (

            executive_df

            .withColumn(

                "conversion_rate",

                round(

                    col("total_orders")
                    / col("total_events")
                    * 100,

                    2

                )

            )

            .withColumn(

                "member_conversion_rate",

                round(

                    col("member_orders")
                    / col("total_orders")
                    * 100,

                    2

                )

            )

            .withColumn(

                "average_units_per_order",

                round(

                    col("products_sold")
                    / col("total_orders"),

                    2

                )

            )

            .drop("member_orders")

        )

        return executive_df