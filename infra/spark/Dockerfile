FROM bitnami/spark:4.0.0
USER root

# Install curl
RUN install_packages curl

# Install nano
RUN install_packages nano

# Create the spark user home directory
RUN mkdir -p /home/spark && chown 1001:1001 /home/spark

# Set environment variables
ENV HOME=/home/spark
ENV USER=spark
ENV SPARK_HOME=/opt/bitnami/spark

# Persist environment variables
RUN echo "export HOME=/home/spark" >> /opt/bitnami/spark/.bashrc
RUN echo "export USER=spark" >> /opt/bitnami/spark/.bashrc
RUN echo "export SPARK_HOME=/opt/bitnami/spark" >> /opt/bitnami/spark/.bashrc

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir delta-spark==4.0.0

# Download Delta Lake and Hadoop JARs
RUN curl -O https://repo1.maven.org/maven2/io/delta/delta-spark_2.13/4.0.0/delta-spark_2.13-4.0.0.jar && \
    curl -O https://repo1.maven.org/maven2/io/delta/delta-storage/4.0.0/delta-storage-4.0.0.jar && \
    curl -O https://repo1.maven.org/maven2/io/delta/delta-connect-client_2.13/4.0.0/delta-connect-client_2.13-4.0.0.jar && \
    curl -O https://repo1.maven.org/maven2/io/delta/delta-connect-common_2.13/4.0.0/delta-connect-common_2.13-4.0.0.jar && \
#    curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/3.3.6/hadoop-common-3.3.6.jar && \
#    curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-hdfs/3.3.6/hadoop-hdfs-3.3.6.jar && \
#    curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar && \
    mv delta-spark_2.13-4.0.0.jar delta-storage-4.0.0.jar delta-connect-client_2.13-4.0.0.jar delta-connect-common_2.13-4.0.0.jar /opt/bitnami/spark/jars/
#    mv delta-spark_2.13-4.0.0.jar delta-storage-4.0.0.jar hadoop-common-3.3.6.jar hadoop-hdfs-3.3.6.jar hadoop-aws-3.3.6.jar /opt/bitnami/spark/jars/

# Remove conflicting Hadoop JARs
#RUN rm -f /opt/bitnami/spark/jars/hadoop-client* /opt/bitnami/spark/jars/hadoop-aws-3.3.4.jar

# Create Ivy cache directory
RUN mkdir -p /opt/bitnami/spark/ivy_cache && chown 1001:1001 /opt/bitnami/spark/ivy_cache

# Configure Spark
#RUN echo "spark.jars.ivy /opt/bitnami/spark/ivy_cache" >> /opt/bitnami/spark/conf/spark-defaults.conf
#RUN echo "spark.sql.extensions io.delta.sql.DeltaSparkSessionExtension" >> /opt/bitnami/spark/conf/spark-defaults.conf
#RUN echo "spark.sql.catalog.spark_catalog org.apache.spark.sql.delta.catalog.DeltaCatalog" >> /opt/bitnami/spark/conf/spark-defaults.conf

# Configure Hadoop
RUN #echo "<configuration><property><name>fs.defaultFS</name><value>file:///</value></property><property><name>hadoop.security.authentication</name><value>simple</value></property></configuration>" > /opt/bitnami/spark/conf/core-site.xml

# Optional: Add S3A credentials (replace with environment variables or AWS credentials file)
# RUN echo "spark.hadoop.fs.s3a.access.key YOUR_ACCESS_KEY" >> /opt/bitnami/spark/conf/spark-defaults.conf
# RUN echo "spark.hadoop.fs.s3a.secret.key YOUR_SECRET_KEY" >> /opt/bitnami/spark/conf/spark-defaults.conf
# RUN echo "spark.hadoop.fs.s3a.endpoint s3.amazonaws.com" >> /opt/bitnami/spark/conf/spark-defaults.conf

USER 1001