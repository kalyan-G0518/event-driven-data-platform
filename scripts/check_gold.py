from src.processing.streaming.spark_session import SparkSessionBuilder


def main():

    spark = SparkSessionBuilder.create()

    df = spark.read.parquet("data/gold")

    print("\n===== RECORD COUNT =====")
    print(df.count())

    print("\n===== DATA =====")
    df.show(truncate=False)

    print("\n===== SCHEMA =====")
    df.printSchema()


if __name__ == "__main__":
    main()