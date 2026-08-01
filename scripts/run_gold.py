from src.processing.streaming.spark_session import SparkSessionBuilder
from src.orchestration.gold_pipeline import GoldPipeline


def main():

    spark = SparkSessionBuilder.create()

    pipeline = GoldPipeline(spark)

    pipeline.run()


if __name__ == "__main__":
    main()