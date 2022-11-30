FROM marcelmittelstaedt/airflow:latest

COPY ./mysql-connector-j-8.0.31.jar /home/airflow/spark/jars

COPY --chown=airflow ./airflow/plugins /home/airflow/airflow/plugins
COPY --chown=airflow ./airflow/dags /home/airflow/airflow/dags
COPY --chown=airflow ./airflow/python /home/airflow/airflow/python