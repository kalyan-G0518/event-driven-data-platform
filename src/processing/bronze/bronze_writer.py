from pyspark.sql import DataFrame


class BronzeWriter:
    """
    Writes parsed streaming data
    into the Bronze layer.
    """

    def __init__(
        self,
        output_path: str = "data/bronze",
        checkpoint_path: str = "checkpoints/bronze",
    ):
        self.output_path = output_path
        self.checkpoint_path = checkpoint_path

    def write(self, df: DataFrame):
        """
        Starts the streaming write.
        """

        query = (
            df.writeStream
            .format("parquet")
            .option("path", self.output_path)
            .option("checkpointLocation", self.checkpoint_path)
            .outputMode("append")
            .start()
        )

        return query