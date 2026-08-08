from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    when,
)


class InventoryAnalytics:
    """
    Builds inventory-level analytics from Product Master.
    """

    @staticmethod
    def build(products: DataFrame) -> DataFrame:

        return (
            products

            .select(
                "product_id",
                "product_name",
                "brand",
                "category",
                "subcategory",
                "supplier_name",
                "warehouse_id",
                "inventory_quantity",
                "reorder_level",
                "cost_price",
                "is_active"
            )

            .withColumn(
                "inventory_value",
                col("inventory_quantity") * col("cost_price")
            )

            .withColumn(
                "stock_status",
                when(
                    col("inventory_quantity") <= 0,
                    "OUT_OF_STOCK"
                )
                .when(
                    col("inventory_quantity") <= col("reorder_level"),
                    "LOW_STOCK"
                )
                .otherwise("HEALTHY")
            )

            .withColumn(
                "is_low_stock",
                col("inventory_quantity") <= col("reorder_level")
            )
        )