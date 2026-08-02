from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import (
    col,
    lit,
    rand,
    when,
    concat,
    current_timestamp,
    round,
    expr,
)
from pyspark.sql.types import IntegerType


class CustomerMasterBuilder:
    """
    Builds the Customer Master dataset.
    """

    def __init__(
        self,
        spark: SparkSession,
        num_customers: int = 10000,
        output_path: str = "data/master/customers",
    ):
        self.spark = spark
        self.num_customers = num_customers
        self.output_path = output_path
        self.df = None

    def extract(self):

        self.df = (
            self.spark.range(1, self.num_customers + 1)
            .withColumnRenamed("id", "customer_id")
        )

        return self

    def clean(self):
        return self

    def standardize(self):
        return self

    def enrich(self):

        self.df = (

            self.df

            .withColumn(
                "first_name",
                concat(lit("Customer_"), col("customer_id"))
            )

            .withColumn(
                "last_name",
                lit("ShopSphere")
            )

            .withColumn(
                "email",
                concat(
                    lit("customer"),
                    col("customer_id"),
                    lit("@shopsphere.com")
                )
            )

            .withColumn(
                "age",
                (rand()*42 + 18).cast(IntegerType())
            )

            .withColumn(
                "gender",
                when(rand() < 0.5, "Male")
                .otherwise("Female")
            )

            .withColumn(
                "membership",
                when(rand() < 0.60, "Bronze")
                .when(rand() < 0.85, "Silver")
                .when(rand() < 0.97, "Gold")
                .otherwise("Platinum")
            )

            .withColumn(
                "preferred_category",
                expr("""
                    CASE
                        WHEN rand() < 0.20 THEN 'Electronics'
                        WHEN rand() < 0.35 THEN 'Fashion'
                        WHEN rand() < 0.50 THEN 'Home & Kitchen'
                        WHEN rand() < 0.65 THEN 'Sports'
                        WHEN rand() < 0.80 THEN 'Beauty'
                        ELSE 'Books'
                    END
                """)
            )

            .withColumn(
                "avg_order_value",
                round(rand()*450 + 50,2)
            )

            .withColumn(
                "purchase_probability",
                round(rand(),2)
            )

            .withColumn(
                "discount_affinity",
                round(rand(),2)
            )

            .withColumn(
                "country",
                lit("USA")
            )

            .withColumn(
                "state",
                lit("Florida")
            )

            .withColumn(
                "city",
                lit("Tampa")
            )

            .withColumn(
                "signup_date",
                expr("date_sub(current_date(), CAST(rand()*1000 AS INT))")
            )

            .withColumn(
                "is_active",
                lit(True)
            )

            .withColumn(
                "created_at",
                current_timestamp()
            )

        )

        return self

    def export(self):

        (
            self.df.write
            .mode("overwrite")
            .parquet(self.output_path)
        )

        return self

    def build(self):

        (
            self.extract()
                .clean()
                .standardize()
                .enrich()
                .export()
        )

        print("✅ Customer Master generated successfully.")

        return self.df