from pyspark.sql import DataFrame


class GoldWriter:

    def __init__(
        self,
        output_path="data/gold"
    ):
        self.output_path = output_path

    def write(
        self,
        df: DataFrame
    ):

        (

            df

            .write

            .mode("overwrite")

            .parquet(self.output_path)

        )