import os, time
from dotenv import load_dotenv
from models.model import Model

# Load environment variables from .env file
load_dotenv()

# Example usage of transformation functions
def main():
    source_db_url = os.getenv('SOURCE_DB_URL')
    destination_db_url = os.getenv('DESTINATION_DB_URL')

    # Call your transformation functions
    m = Model(source_db_url, destination_db_url)
    m.transform_zipcensus()
    m.transform_calendar()
    m.load_tables()
    m.transform_orders()
    m.spark.stop()

if __name__ == "__main__":
    main()
    # time.sleep(300)
