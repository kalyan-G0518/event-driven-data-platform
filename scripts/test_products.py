from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Test Product Master")
    .getOrCreate()
)

df = spark.read.parquet("data/master/products")

print("\n===== SCHEMA =====")
df.printSchema()

print("\n===== COLUMNS =====")
print(df.columns)



spark.stop()