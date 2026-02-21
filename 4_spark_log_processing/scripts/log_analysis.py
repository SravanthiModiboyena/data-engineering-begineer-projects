from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract, col, count

# Create Spark Session
spark = SparkSession.builder \
    .appName("Spark Log Processing Project") \
    .getOrCreate()

# Read log file
logs = spark.read.text("../data/sample_logs.txt")

# Extract fields using regex
logs_df = logs.select(
    regexp_extract('value', r'^(\S+)', 1).alias('ip'),
    regexp_extract('value', r'\"(\S+)', 1).alias('method'),
    regexp_extract('value', r'\"[A-Z]+ (\S+)', 1).alias('endpoint'),
    regexp_extract('value', r'(\d{3})$', 1).alias('status')
)

print("===== Sample Extracted Data =====")
logs_df.show()

print("===== Status Code Count =====")
logs_df.groupBy("status").count().show()

print("===== Top IP Addresses =====")
logs_df.groupBy("ip").count().orderBy(col("count").desc()).show()

spark.stop()
