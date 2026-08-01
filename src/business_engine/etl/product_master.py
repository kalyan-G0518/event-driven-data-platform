from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import (
    col,
    lit,
    regexp_extract,
    regexp_replace,
    round,
    when,
    concat,
    upper,
    monotonically_increasing_id,
    current_timestamp,
    rand,
)
from pyspark.sql.types import IntegerType


class ProductMasterBuilder:
    """
    Builds the ShopSphere Product Master
    from the raw reference dataset.
    """

    def __init__(
        self,
        spark: SparkSession,
        input_path: str = "data/reference/ecommerce_dataset.csv",
        output_path: str = "data/master/products",
    ):
        self.spark = spark
        self.input_path = input_path
        self.output_path = output_path
        self.df = None

    # --------------------------------------------------
    # EXTRACT
    # --------------------------------------------------

    def extract(self):

        self.df = (
            self.spark.read
            .option("header", True)
            .option("multiLine", True)
            .option("escape", "\"")
            .csv(self.input_path)
        )

        return self

    # --------------------------------------------------
    # CLEAN
    # --------------------------------------------------

    def clean(self):

        self.df = (
            self.df
            .dropDuplicates(["product_id"])
            .dropna(subset=["title", "final_price", "category"])
        )

        return self

    # --------------------------------------------------
    # STANDARDIZE
    # --------------------------------------------------

    def standardize(self):

        self.df = (
            self.df

            .withColumnRenamed("title", "product_name")
            .withColumnRenamed("final_price", "selling_price")
            .withColumnRenamed("initial_price", "mrp")
            .withColumnRenamed("rating", "average_rating")
            .withColumnRenamed("ratings_count", "review_count")
            .withColumnRenamed("seller_name", "supplier_name")

            .withColumn(
                "product_name",
                regexp_replace(
                    col("product_name"),
                    "\\s+",
                    " "
                )
            )
        )

        return self

    # --------------------------------------------------
    # ENRICH
    # --------------------------------------------------

    def enrich(self):

        # SKU

        self.df = self.df.withColumn(
            "sku",
            concat(
                lit("SKU-"),
                upper(
                    regexp_extract(
                        col("category"),
                        "([A-Za-z])",
                        1
                    )
                ),
                monotonically_increasing_id()
            )
        )

        # Brand (first word of title)

        self.df = self.df.withColumn(
            "brand",
            regexp_extract(
                col("product_name"),
                r"^([A-Za-z0-9]+)",
                1
            )
        )

        # Numeric prices

        self.df = (
            self.df

            .withColumn(
                "selling_price",
                regexp_replace(
                    col("selling_price"),
                    "[^0-9.]",
                    ""
                ).cast("double")
            )

            .withColumn(
                "mrp",
                regexp_replace(
                    col("mrp"),
                    "[^0-9.]",
                    ""
                ).cast("double")
            )
        )

        # Cost Price
        # (Temporary rule:
        # 70% of selling price)

        self.df = self.df.withColumn(
            "cost_price",
            round(
                col("selling_price") * lit(0.70),
                2
            )
        )

        # Profit Margin

        self.df = self.df.withColumn(
            "profit_margin",
            round(
                col("selling_price")
                - col("cost_price"),
                2
            )
        )

        # Inventory

        self.df = self.df.withColumn(
            "inventory_quantity",
            (
                rand() * 500 + 50
            ).cast(IntegerType())
        )

        # Reorder Level

        self.df = self.df.withColumn(
            "reorder_level",
            lit(50)
        )

        # Warehouse

        self.df = self.df.withColumn(
            "warehouse_id",
            when(rand() < 0.2, "WH001")
            .when(rand() < 0.4, "WH002")
            .when(rand() < 0.6, "WH003")
            .when(rand() < 0.8, "WH004")
            .otherwise("WH005")
        )

        # Supplier ID

        self.df = self.df.withColumn(
            "supplier_id",
            concat(
                lit("SUP-"),
                monotonically_increasing_id()
            )
        )

        # Active

        self.df = self.df.withColumn(
            "is_active",
            lit(True)
        )

        # Timestamp

        self.df = self.df.withColumn(
            "created_at",
            current_timestamp()
        )

        return self

    # --------------------------------------------------
    # EXPORT
    # --------------------------------------------------

    def export(self):

        (
            self.df
            .write
            .mode("overwrite")
            .option("header", True)
            .csv(self.output_path)
        )

        return self

    # --------------------------------------------------
    # BUILD
    # --------------------------------------------------

    def build(self):

        (
            self.extract()
                .clean()
                .standardize()
                .enrich()
                .export()
        )

        print("✅ Product Master generated successfully.")

        return self.df