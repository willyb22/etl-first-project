from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow.sensors.time_sensor import TimeSensor
from airflow.utils.dates import days_ago
import time
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'manage_users_and_etl',
    default_args=default_args,
    description='Add users, run ETL at 2 PM, and delete users',
    schedule_interval='@daily',  # Run this DAG manually or on a specific schedule
    catchup=False,
    start_date=datetime.now()
)

# Step 1: Create new user and grant read permissions using SQL file
create_user = PostgresOperator(
    task_id='create_user',
    postgres_conn_id='destination_db_conn',
    sql='./tasks/create_user.sql',  # Path to the SQL file
    dag=dag,
)

# Step 2: Wait for a specified time (e.g., 1 week)
wait_time = PythonOperator(
    task_id='wait_for_time',
    python_callable=lambda: time.sleep(60 * 60* 5),  # Sleep for 5 hours 
    dag=dag,
)

# Step 3: Revoke permissions and delete the user
delete_user = PostgresOperator(
    task_id='delete_user',
    postgres_conn_id='destination_db_conn',
    sql='./tasks/delete_user.sql',  # Another SQL file for deletion
    dag=dag,
)

# Step 4: Dummy start and end tasks
start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

# Define your ETL task
run_etl = SimpleHttpOperator(
    task_id='run_etl',
    http_conn_id='etl_http_conn',
    endpoint='start_etl',  # Endpoint configured in the ETL container
    method='POST',
    dag=dag,
)

# DAG Workflow
start >> create_user >> wait_time >> delete_user >> end
start >> run_etl >> end
