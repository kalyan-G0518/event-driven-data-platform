from pyspark.sql import DataFrame


class SilverValidator:

    @staticmethod
    def validate(df: DataFrame) -> DataFrame:

        return df