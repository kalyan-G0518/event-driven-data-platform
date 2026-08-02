from pyspark.sql import DataFrame


class GoldWriter:

    def __init__(
        self,
        output_path="data/gold"
    ):
        self.output_path = output_path

    def write(
        self,
        datasets: dict[str, DataFrame]
    ):

        for dataset_name, df in datasets.items():

            (
                df
                .write
                .mode("overwrite")
                .parquet(
                    f"{self.output_path}/{dataset_name}"
                )
            )

            print(f"✓ Written {dataset_name}")