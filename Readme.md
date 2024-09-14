Here's my first etl project using the data that i download from Linoff's book "Data Analysis Using SQL and Excel"

You can download the zipfile and extract only the txt files and move those to ./source_db/initial-data/.

Here's the services that i use:
- source_db: using postgres 15 image, contains all data that are loaded from initial-data.
- destination_db: using postgres 15 image, contains all data that are transformed by etl services.
- etl: using apache/spark-py image, the Models module extracts source_db, transforms it, and loads it to destination_db.
- scheduler: using apache/airflow, contains the dags that is managing the new_user role (grant and revoke the previllage of the notebooks user to use select command of destination_db) and also do trigger the etl.
- notebooks: using jupyter, as new_user do data science on destination_db

You can read the overview of this project in the etl-first-project-overview.pdf

