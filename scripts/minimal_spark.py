from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("Spark Test")
    .getOrCreate()
)

print("=" * 50)
print("Spark Started!")
print("Version:", spark.version)
print("=" * 50)

spark.stop()