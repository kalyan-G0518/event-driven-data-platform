from pyspark.sql import DataFrame


class SilverTransformer:

    @staticmethod
    def transform(df: DataFrame) -> DataFrame:

        return df