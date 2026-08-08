from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    count,
    sum,
    avg,
)


class CategoryAnalytics:
    """
    Builds category-level business analytics
    from Product Performance.
    """

    @staticmethod
    def build(product_performance: DataFrame) -> DataFrame:

        return (
            product_performance

            .groupBy(
                "category"
            )

            .agg(

                count("*").alias(
                    "product_count"
                ),

                sum("total_events").alias(
                    "total_events"
                ),

                sum("purchase_events").alias(
                    "purchase_events"
                ),

                sum("units_sold").alias(
                    "units_sold"
                ),

                sum("total_revenue").alias(
                    "total_revenue"
                ),

                avg("average_selling_price").alias(
                    "average_selling_price"
                ),

                sum("inventory_value").alias(
                    "inventory_value"
                )
            )
        )