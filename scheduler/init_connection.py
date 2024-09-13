from airflow import settings
from airflow.models import Connection
from airflow.utils.session import create_session
from secret import secret


def get_connection_by_id(session, conn_id):
    """Retrieve a connection by conn_id."""
    return session.query(Connection).filter_by(conn_id=conn_id).first()


def create_connections():
    # Create HTTP connection
    http_conn = Connection(
        conn_id='etl_http_conn',
        conn_type='http',
        host='http://etl',
        port=5000
    )
    
    # Create PostgreSQL connection
    postgres_conn = Connection(
        conn_id='destination_db_conn',
        conn_type='postgres',
        host='destination_db',
        schema=secret['destination_db']['schema'],
        login=secret['destination_db']['login'],
        password=secret['destination_db']['password'],
        port=5432
    )
    
    # Add connections to the Airflow DB
    with create_session() as session:
        try:
            # Check if the destination_db_conn already exists
            existing_postgres_conn = get_connection_by_id(session, 'destination_db_conn')
            if existing_postgres_conn:
                print("Connection 'destination_db_conn' already exists, skipping creation.")
            else:
                session.add(postgres_conn)

            # Check if the etl_http_conn already exists
            existing_http_conn = get_connection_by_id(session, 'etl_http_conn')
            if existing_http_conn:
                print("Connection 'etl_http_conn' already exists, skipping creation.")
            else:
                session.add(http_conn)

            session.commit()
            print("Airflow connections created successfully!")
        except Exception as e:
            session.rollback()
            print("Error creating Airflow connections: \n{}".format(e))


if __name__ == '__main__':
    create_connections()
