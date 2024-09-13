DO $$
BEGIN
    -- Check if the user already exists
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'new_user') THEN
        -- Create the user if it does not exist
        EXECUTE 'CREATE USER new_user WITH PASSWORD ''new_password''';
    END IF;

    -- Grant privileges
    EXECUTE 'GRANT CONNECT ON DATABASE destination_db TO new_user';
    EXECUTE 'GRANT USAGE ON SCHEMA public TO new_user';
    EXECUTE 'GRANT SELECT ON ALL TABLES IN SCHEMA public TO new_user';

    -- Ensure the user can select from future tables
    EXECUTE 'ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO new_user';
END $$;
