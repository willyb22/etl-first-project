-- Connect to the destination_db
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM new_user;
REVOKE CONNECT ON DATABASE destination_db FROM new_user;