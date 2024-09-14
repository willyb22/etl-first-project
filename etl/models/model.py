from pyspark.sql import SparkSession
# from sqlalchemy import create_engine

from .transform_zipcensus import process as tzi
from .transform_calendar import process as tca
from .load_tables import process as lt
from .transform_orders import process as tor

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

    def load_tables(self):
        table_names = ['campaigns', 'customers']
        for tn in table_names:
            lt(self.spark, tn, self.source_db_url, self.destination_db_url)
    
    def transform_zipcensus(self):
        tzi(self.spark, self.source_db_url, self.destination_db_url)

    def transform_calendar(self):
        tca(self.spark, self.source_db_url, self.destination_db_url)

    def transform_orders(self):
        tor(self.spark, self.source_db_url, self.destination_db_url)