cat << 'EOF' > airflow-entrypoint.sh
#!/bin/bash
# Fix permissions for /opt/airflow/logs
mkdir -p /opt/airflow/logs/scheduler
chown -R airflow:airflow /opt/airflow/logs
chmod -R u+rwX /opt/airflow/logs
# Initialize Airflow database and admin user
airflow db init
airflow users create \
  --username admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com \
  --password admin || true
# Start Airflow webserver
exec airflow webserver
EOF