from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[*]")
    .appName("Test")
    .getOrCreate()
)

print("Spark started!")

df = spark.read.parquet("data/silver")

print(df.count())



from pyspark.sql.functions import count, sum, when, col

gold = (
    df
    .groupBy("event_date")
    .agg(
        count("*").alias("total_events"),
        count(
            when(
                col("event_type") == "purchase",
                True
            )
        ).alias("total_orders"),
        sum("total_amount").alias("gross_revenue")
    )
)

gold.write.mode("overwrite").parquet("data/gold_test")

print("SUCCESS")

spark.stop()