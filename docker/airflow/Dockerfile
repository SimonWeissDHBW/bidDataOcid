FROM marcelmittelstaedt/airflow:latest

COPY ./mysql-connector-j-8.0.31.jar /home/airflow/spark/jars

COPY --chown=airflow ./airflow/ /home/airflow/airflow