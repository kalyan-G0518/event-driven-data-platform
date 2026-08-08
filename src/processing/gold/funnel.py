from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    count,
    when,
)


class FunnelAnalytics:
    """
    Builds event funnel analytics from Silver events.
    """

    @staticmethod
    def build(events: DataFrame) -> DataFrame:

        return (
            events

            .agg(

                count(
                    when(
                        events.event_type == "login",
                        True
                    )
                ).alias("login_events"),

                count(
                    when(
                        events.event_type == "search",
                        True
                    )
                ).alias("search_events"),

                count(
                    when(
                        events.event_type == "product_view",
                        True
                    )
                ).alias("product_view_events"),

                count(
                    when(
                        events.event_type == "add_to_cart",
                        True
                    )
                ).alias("add_to_cart_events"),

                count(
                    when(
                        events.event_type == "purchase",
                        True
                    )
                ).alias("purchase_events"),

                count(
                    when(
                        events.event_type == "payment",
                        True
                    )
                ).alias("payment_events")
            )
        )