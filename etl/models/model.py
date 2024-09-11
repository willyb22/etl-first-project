from pyspark.sql import SparkSession
# from sqlalchemy import create_engine

from .transform_zip_to_stab_census import process as tzs

class Model:
    def __init__(self, source_db_url='', destination_db_url=''):
        print('oke')
        self.source_db_url = source_db_url
        self.destination_db_url = destination_db_url
        self.spark = SparkSession.builder \
            .appName("ETL Project") \
            .config("spark.jars", "/opt/spark/jars/postgresql-42.2.23.jar") \
            .getOrCreate()
        self.engine = None # create_engine(self.destination_db_url)

    def transform_zip_to_stab_census(self):
        tzs(self.spark, self.source_db_url, self.destination_db_url)