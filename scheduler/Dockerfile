FROM apache/airflow:latest

# copy the custom entrypoint and make it executable
USER root
COPY *.py /
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# run the entrypoint.sh after the image is build
ENTRYPOINT [ "./entrypoint.sh" ]