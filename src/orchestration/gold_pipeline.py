from pyspark.sql import SparkSession

from src.processing.gold.reader import GoldReader
from src.processing.master.product_reader import ProductMasterReader
from src.processing.master.customer_reader import CustomerMasterReader
from src.processing.gold.customer import CustomerAnalytics
from src.processing.gold.aggregator import GoldAggregator
from src.processing.gold.product import ProductAnalytics

from src.processing.gold.writer import GoldWriter
from src.processing.gold.inventory import InventoryAnalytics
from src.processing.gold.category import CategoryAnalytics
from src.processing.gold.geography import GeographyAnalytics
from src.processing.gold.funnel import FunnelAnalytics

class GoldPipeline:

    def __init__(self, spark: SparkSession):

        self.silver_reader = GoldReader(spark)

        self.product_reader = ProductMasterReader(spark)
        self.customer_reader = CustomerMasterReader(spark)

        self.customer_aggregator = CustomerAnalytics()

        self.summary_aggregator = GoldAggregator()
        self.inventory_aggregator = InventoryAnalytics()
        self.category_aggregator = CategoryAnalytics()
        self.geography_aggregator = GeographyAnalytics()
        self.funnel_aggregator = FunnelAnalytics()

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

        product_metrics = self.product_aggregator.build(
            silver_df,
            product_df
        )
        print("Building Customer Performance...")

        customer_metrics = self.customer_aggregator.build(
            silver_df,
            customer_df
        )
        print("Building Inventory Analytics...")

        inventory_summary = self.inventory_aggregator.build(
            product_df
        )

        print("Building Category Analytics...")

        category_summary = self.category_aggregator.build(
            product_metrics
        )

        print("Building Geography Analytics...")

        geography_summary = self.geography_aggregator.build(
            customer_metrics
        )

        print("Building Funnel Analytics...")

        funnel_summary = self.funnel_aggregator.build(
            silver_df
        )

        summary_datasets["product_performance"] = product_df
        summary_datasets["customer_metrics"] = customer_metrics
        summary_datasets["inventory_summary"] = inventory_summary
        summary_datasets["category_summary"] = category_summary
        summary_datasets["geography_summary"] = geography_summary
        summary_datasets["funnel_summary"] = funnel_summary

        self.writer.write(summary_datasets)

        print("Gold Layer Created Successfully!")