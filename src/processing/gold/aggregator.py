from pyspark.sql import DataFrame

from src.processing.gold.executive import ExecutiveAnalytics
from src.processing.gold.sales import SalesAnalytics

class GoldAggregator:
    """
    Orchestrates all Gold analytics
    data marts.
    """

    @staticmethod
    def aggregate(df: DataFrame) -> dict[str, DataFrame]:

        gold_datasets = {}

        # Executive Summary
        gold_datasets["executive_summary"] = (
            ExecutiveAnalytics.build(df)
        )
        gold_datasets["sales_summary"] = (
    SalesAnalytics.build(df)
)

        return gold_datasets