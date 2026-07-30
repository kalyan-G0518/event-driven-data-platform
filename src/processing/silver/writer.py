from pyspark.sql import DataFrame


class SilverWriter:

    def __init__(
        self,
        output_path="data/silver",
        checkpoint_path="checkpoints/silver"
    ):
        self.output_path = output_path
        self.checkpoint_path = checkpoint_path

    def write(self, df: DataFrame):

        query = (
            df.writeStream
            .format("parquet")
            .option("path", self.output_path)
            .option("checkpointLocation", self.checkpoint_path)
            .outputMode("append")
            .start()
        )

        return query