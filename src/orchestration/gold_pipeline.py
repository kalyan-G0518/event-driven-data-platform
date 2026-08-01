from pyspark.sql import SparkSession

from src.processing.gold.reader import GoldReader
from src.processing.gold.aggregator import GoldAggregator
from src.processing.gold.writer import GoldWriter


class GoldPipeline:

    def __init__(self, spark: SparkSession):

        self.reader = GoldReader(spark)

        self.aggregator = GoldAggregator()

        self.writer = GoldWriter()

    def run(self):

        print("Reading Silver...")

        df = self.reader.read()

        print("Aggregating...")

        df = self.aggregator.aggregate(df)

        print("Writing Gold...")

        self.writer.write(df)

        print("Gold Layer Created Successfully!")