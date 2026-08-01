from pyspark.sql import SparkSession

from src.business_engine.etl.product_master import ProductMasterBuilder


def main():

    spark = (
        SparkSession.builder
        .appName("Product Master Builder")
        .getOrCreate()
    )

    ProductMasterBuilder(spark).build()

    spark.stop()


if __name__ == "__main__":
    main()