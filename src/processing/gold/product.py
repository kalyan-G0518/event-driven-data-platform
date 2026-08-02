from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    count,
    when,
    sum,
    avg,
)


class ProductAnalytics:
    """
    Builds Product Performance analytics by
    combining Silver events with Product Master.
    """

    @staticmethod
    def build(
        events: DataFrame,
        products: DataFrame,
    ) -> DataFrame:

        joined = (

            events
            .drop("category")

            .join(
                products,
                on="product_id",
                how="left"
            )

        )

        return (

            joined

            .groupBy(

                "product_id",
                "product_name",
                "brand",
                "category",
                "subcategory",
                "supplier_name",
                "warehouse_id",
                "inventory_quantity",
                "cost_price"

            )

            .agg(

                # Overall activity

                count("*").alias("total_events"),

                # Event counts

                count(
                    when(
                        col("event_type") == "login",
                        True
                    )
                ).alias("login_events"),

                count(
                    when(
                        col("event_type") == "search",
                        True
                    )
                ).alias("search_events"),

                count(
                    when(
                        col("event_type") == "product_view",
                        True
                    )
                ).alias("view_events"),

                count(
                    when(
                        col("event_type") == "add_to_cart",
                        True
                    )
                ).alias("cart_events"),

                count(
                    when(
                        col("event_type") == "purchase",
                        True
                    )
                ).alias("purchase_events"),

                count(
                    when(
                        col("event_type") == "payment",
                        True
                    )
                ).alias("payment_events"),

                # Business KPIs

                sum("quantity").alias("units_sold"),

                sum("total_amount").alias("total_revenue"),

                avg("unit_price").alias("average_selling_price")

            )

            .withColumn(

                "inventory_value",

                col("inventory_quantity") * col("cost_price")

            )

        )