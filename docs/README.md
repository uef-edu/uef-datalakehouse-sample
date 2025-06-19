# UEF Nexus 
UEF Nexus is a platform for building and deploying DataLakeHouse and DataLake solutions.

# Documentation
Documentation for UEF Nexus is available at [docs.nexus.uef.vn](https://docs.nexus.uef.vn).

# Installation
## Dịch vụ:
- MinIO: Object storage tương thích S3 để lưu trữ dữ liệu. 
- Spark: Xử lý dữ liệu batch và streaming, tích hợp Delta Lake.
- Trino: Truy vấn SQL phân tán.
- Hive Metastore: Quản lý metadata, tích hợp với Spark và Trino.
- Postgres: Backend cho Hive Metastore.
- Airflow: Lập lịch và quản lý pipeline.
- Superset: Trực quan hóa dữ liệu (BI).

## Cấu hình:
- Các dịch vụ được liên kết qua một network chung (lakehouse-network). 
- Sử dụng volume để lưu trữ dữ liệu bền vững (MinIO, MySQL).
- Mở các cổng cần thiết để truy cập (ví dụ: MinIO console, Superset UI).

## Yêu cầu:
- Docker và Docker Compose đã được cài đặt. 
- Máy có ít nhất 16GB RAM, 4 CPU, 100GB ổ cứng.

# Truy cập các dịch vụ:
- MinIO: http://localhost:9001 (admin/password).
- Spark UI: http://localhost:8080.
- Trino: http://localhost:8081.
- Airflow: http://localhost:8082 (admin/admin).
- Superset: http://localhost:8088 (khởi tạo qua UI).