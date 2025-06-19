from pyspark.sql import SparkSession
# from delta import configure_spark_with_delta_pip
from delta.pip_utils import configure_spark_with_delta_pip

# Initialize Spark with Delta Lake and Hive Metastore
builder = SparkSession.builder.appName("ProcessTaxiData") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "password") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hive.metastore.uris", "thrift://hive-metastore:9083")
spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Read CSV from MinIO
df = spark.read.csv("s3a://raw/sample_taxi.csv", header=True, inferSchema=True)

# Transform: Clean and filter data
df_cleaned = df.dropna().filter(df.passenger_count > 0)

# Save as Delta table
df_cleaned.write.format("delta").mode("overwrite").save("s3a://processed/taxi_data")

# Register table in Hive Metastore
spark.sql("CREATE TABLE IF NOT EXISTS taxi_data USING DELTA LOCATION 's3a://processed/taxi_data'")

print("Data processed and saved as Delta table")
spark.stop()