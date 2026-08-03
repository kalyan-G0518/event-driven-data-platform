from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    count,
    when,
    sum,
    avg,
    max,
)


class CustomerAnalytics:
    """
    Builds customer-level business analytics
    by combining Silver events with Customer Master.
    """

    @staticmethod
    def build(
        events: DataFrame,
        customers: DataFrame,
    ) -> DataFrame:

        # Alias both DataFrames
        events = events.alias("e")
        customers = customers.alias("c")

        joined = (

            events

            .join(

                customers,

                col("e.user_id") == col("c.user_id"),

                "left"

            )

        )

        return (

            joined

            .groupBy(

                col("e.user_id").alias("user_id"),

                col("c.customer_name"),

                col("c.membership_type"),

                col("c.gender"),

                col("c.city"),

                col("c.country")

            )

            .agg(

                # Overall activity
                count("*").alias("total_events"),

                # Event counts
                count(
                    when(
                        col("e.event_type") == "login",
                        True
                    )
                ).alias("login_events"),

                count(
                    when(
                        col("e.event_type") == "search",
                        True
                    )
                ).alias("search_events"),

                count(
                    when(
                        col("e.event_type") == "product_view",
                        True
                    )
                ).alias("view_events"),

                count(
                    when(
                        col("e.event_type") == "add_to_cart",
                        True
                    )
                ).alias("cart_events"),

                count(
                    when(
                        col("e.event_type") == "purchase",
                        True
                    )
                ).alias("purchase_events"),

                sum(
                    col("e.quantity")
                ).alias("total_quantity"),

                sum(
                    col("e.total_amount")
                ).alias("total_revenue"),

                avg(
                    col("e.total_amount")
                ).alias("average_order_value"),

                max(
                    col("e.event_timestamp")
                ).alias("last_activity")

            )

            .withColumn(

                "is_active_customer",

                col("purchase_events") > 0

            )

        )