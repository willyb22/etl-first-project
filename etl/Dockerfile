# Use an official PySpark base image
FROM apache/spark-py:latest

# Download PostgreSQL JDBC Driver
RUN mkdir -p /opt/spark/jars
COPY ./jars/postgresql-42.2.23.jar /opt/spark/jars/postgresql-42.2.23.jar
# Install Python dependencies
COPY requirements.txt /app/requirements.txt

USER root
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy your ETL script into the container
COPY main.py /app/main.py

# Set the working directory
WORKDIR /app

# Define the entry point for the container
ENTRYPOINT ["python3", "/app/main.py"]
