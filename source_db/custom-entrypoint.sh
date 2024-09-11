#!/bin/bash
set -e
echo "Beginning Entrypoint "
echo "Using PostgreSQL user: $POSTGRES_USER"

# # Read password from Docker Secrets file
# if [ -f /run/secrets/source_db_password ]; then
#   export POSTGRES_PASSWORD=$(cat /run/secrets/source_db_password)
# elif [ -f /run/secrets/destination_db_password ]; then
#   export POSTGRES_PASSWORD=$(cat /run/secrets/destination_db_password)
# fi

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    GRANT ALL PRIVILEGES ON DATABASE "$POSTGRES_DB" TO "$POSTGRES_USER";
EOSQL

if !psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\dt'; then
    echo "Database $POSTGRES_DB exists, no need to load."
else
    echo "Database $POSTGRES_DB's table does not exist, loading..."
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -f /initial-data/LoadPostgres.sql
fi

# Keep the container running
wait
