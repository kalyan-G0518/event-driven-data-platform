from pyspark import find_spark_home
from src.processing.streaming.spark_session import SparkSessionBuilder
from src.orchestration.gold_pipeline import GoldPipeline


def main():
    print("STEP 1")

    spark = SparkSessionBuilder.create()

    print("STEP 2")

    pipeline = GoldPipeline(spark)

    print("STEP 3")

    pipeline.run()

    print("STEP 4")

if __name__ == "__main__":
    main()