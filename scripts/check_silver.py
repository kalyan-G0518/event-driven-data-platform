from pyspark.sql import SparkSession


def main():
    spark = (
        SparkSession.builder
        .appName("CheckSilver")
        .master("local[*]")
        .getOrCreate()
    )

    df = spark.read.parquet("data/silver")

    print("\n===== RECORD COUNT =====")
    print(df.count())

    print("\n===== SCHEMA =====")
    df.printSchema()

    print("\n===== SAMPLE DATA =====")
    df.show(truncate=False)

    spark.stop()


if __name__ == "__main__":
    main()