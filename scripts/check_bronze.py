from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Check Bronze")
    .getOrCreate()
)

df = spark.read.parquet("data/bronze")

print("\n===== RECORD COUNT =====")
print(df.count())

print("\n===== DATA =====")
df.show(10, truncate=False)

print("\n===== SCHEMA =====")
df.printSchema()

spark.stop()