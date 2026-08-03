from pyspark.sql import SparkSession

from src.processing.gold.reader import GoldReader
from src.processing.master.product_reader import ProductMasterReader
from src.processing.master.customer_reader import CustomerMasterReader
from src.processing.gold.customer import CustomerAnalytics
from src.processing.gold.aggregator import GoldAggregator
from src.processing.gold.product import ProductAnalytics

from src.processing.gold.writer import GoldWriter


class GoldPipeline:

    def __init__(self, spark: SparkSession):

        self.silver_reader = GoldReader(spark)

        self.product_reader = ProductMasterReader(spark)
        self.customer_reader = CustomerMasterReader(spark)

        self.customer_aggregator = CustomerAnalytics()

        self.summary_aggregator = GoldAggregator()

        self.product_aggregator = ProductAnalytics()

        self.writer = GoldWriter()

    def run(self):

        print("Reading Silver...")

        silver_df = self.silver_reader.read()

        print("Reading Product Master...")

        product_df = self.product_reader.read()
        print("Reading Customer Master...")

        customer_df = self.customer_reader.read()

        print("Building Executive Summary...")

        summary_datasets = self.summary_aggregator.aggregate(
            silver_df
        )

        product_df = self.product_aggregator.build(
            silver_df,
            product_df
        )
        print("Building Customer Performance...")

        customer_metrics = self.customer_aggregator.build(
            silver_df,
            customer_df
        )

        summary_datasets["product_performance"] = product_df
        summary_datasets["customer_metrics"] = customer_metrics

        self.writer.write(summary_datasets)

        print("Gold Layer Created Successfully!")