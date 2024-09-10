FROM postgres:15

# Copy the custom entrypoint script
COPY ./custom-entrypoint.sh /docker-entrypoint-initdb.d/custom-entrypoint.sh

RUN chmod +x /docker-entrypoint-initdb.d/custom-entrypoint.sh
