from src.processing.streaming.spark_session import SparkSessionBuilder
from src.orchestration.silver_pipeline import SilverPipeline


def main():

    spark = SparkSessionBuilder.create()

    pipeline = SilverPipeline(spark)

    pipeline.run()


if __name__ == "__main__":
    main()