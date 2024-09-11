import os
from pyspark.sql import SparkSession
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

destination_db_url = os.getenv('DESTINATION_DB_URL')

# Create a SparkSession
spark = SparkSession.builder \
    .appName("ETL Project") \
    .config("spark.some.config.option", "config-value") \
    .getOrCreate()

engine = create_engine(destination_db_url)