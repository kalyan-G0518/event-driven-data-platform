from pyspark.sql import SparkSession

from src.business_engine.etl.customer_master import CustomerMasterBuilder


def main():

    spark = (
        SparkSession.builder
        .appName("Customer Master Builder")
        .getOrCreate()
    )

    CustomerMasterBuilder(spark).build()

    spark.stop()


if __name__ == "__main__":
    main()