from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

# Initialize Spark with Delta Lake and Hive Metastore
builder = SparkSession.builder.appName("ProcessTaxiData") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://minio:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "admin") \
    .config("spark.hadoop.fs.s3a.secret.key", "password") \
    .config("spark.hadoop.fs.s3a.path.style.access", "true") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hive.metastore.uris", "thrift://hive-metastore:9083") \
    .config("spark.hadoop.fs.s3a.impl.disable.cache", "true") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider") \
    .config("spark.hadoop.fs.s3a.security.credential.provider.path", "") \
    .config("spark.hadoop.hadoop.security.authentication", "simple") \
    .config("spark.hadoop.hadoop.security.authorization", "false") \
    .config("spark.hadoop.java.security.krb5.debug", "true") \
    .config("spark.hadoop.ipc.client.fallback-to-simple-auth-allowed", "true") \
    .config("spark.hadoop.hadoop.rpc.protection", "simple") \
    .config("spark.hadoop.hadoop.security.authentication.simple.anonymous.enable", "true") \
    .config("spark.hadoop.auth_to_local", "") \
    .config("spark.hadoop.dfs.namenode.kerberos.principal", "") \
    .config("spark.hadoop.dfs.datanode.kerberos.principal", "") \
    .config("spark.hadoop.yarn.resourcemanager.principal", "") \
    .config("spark.hadoop.mapreduce.jobhistory.principal", "") \
    .config("spark.hadoop.hadoop.kerberos.kinit.command", "/bin/false") \
    .config("spark.hadoop.fs.hdfs.impl.disable.cache", "true") # Disable cache for HDFS as well, just in case

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
