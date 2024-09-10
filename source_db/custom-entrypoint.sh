#!/bin/bash
set -e
echo "Beginning Entrypoint "
echo "Using PostgreSQL user: $POSTGRES_USER"
# Run the original PostgreSQL entrypoint script to initialize the database
# /usr/local/bin/docker-entrypoint.sh postgres &

# until psql -U "$POSTGRES_USER" -c '\l'; do
#     >&2 echo "PostgreSQL is starting up"
#     sleep 1
# done
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
