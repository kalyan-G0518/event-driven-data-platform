from src.processing.streaming.spark_session import SparkSessionBuilder

print("1. Starting program")

print("2. Creating Spark session...")
spark = SparkSessionBuilder.create()

print("3. Spark session created!")

print("Spark Version:", spark.version)

print("4. Stopping Spark...")
spark.stop()

print("5. Finished")