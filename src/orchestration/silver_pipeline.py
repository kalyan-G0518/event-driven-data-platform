from pyspark.sql import SparkSession

from src.processing.silver.reader import SilverReader
from src.processing.silver.transformer import SilverTransformer
from src.processing.silver.validator import SilverValidator
from src.processing.silver.writer import SilverWriter


class SilverPipeline:

    def __init__(self, spark: SparkSession):
        self.spark = spark

        self.reader = SilverReader(spark)
        self.transformer = SilverTransformer()
        self.validator = SilverValidator()
        self.writer = SilverWriter()

    def run(self):

        df = self.reader.read()

        df = self.transformer.transform(df)

        df = self.validator.validate(df)

        query = self.writer.write(df)

        query.awaitTermination()