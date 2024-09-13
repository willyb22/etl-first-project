#!/bin/bash
set -e
airflow db init
airflow users create \
    --role "$AIRFLOW_ROLE" \
    --username "$AIRFLOW_USERNAME" \
    --password "$AIRFLOW_PASSWORD"  \
    --firstname "$AIRFLOW_FIRSTNAME" \
    --lastname "$AIRFLOW_LASTNAME" \
    --email "$AIRFLOW_EMAIL"

python /init_connection.py

airflow scheduler & 
exec airflow webserver