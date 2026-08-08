from pyspark.sql import SparkSession
from src.processing.streaming.spark_session import SparkSessionBuilder


DATASETS = [
    "executive_summary",
    "sales_summary",
    "product_performance",
    "customer_metrics",
    "inventory_summary",
    "category_summary",
    "geography_summary",
    "funnel_summary",
]


def main():

    spark = SparkSessionBuilder.create()

    print("\n" + "=" * 70)
    print("GOLD LAYER VALIDATION")
    print("=" * 70)

    for dataset in DATASETS:

        path = f"data/gold/{dataset}"

        print("\n" + "-" * 70)
        print(f"DATASET: {dataset}")
        print("-" * 70)

        df = spark.read.parquet(path)

        print("\nSchema:")
        df.printSchema()

        print(f"Row count: {df.count()}")

        print("\nSample:")
        df.show(5, truncate=False)

        print("\nNull counts:")

        null_counts = df.select([
            __import__("pyspark").sql.functions.sum(
                __import__("pyspark").sql.functions.col(c).isNull().cast("int")
            ).alias(c)
            for c in df.columns
        ])

        null_counts.show(truncate=False)

    print("\n" + "=" * 70)
    print("GOLD VALIDATION COMPLETE")
    print("=" * 70)

    spark.stop()


if __name__ == "__main__":
    main()