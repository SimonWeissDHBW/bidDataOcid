"""
Title: Full Cell Towers Dag
Author: Simon Weiss
Description: Downloads, Entpackt und kopiert Full Cell Towers nach HDFS
"""

from airflow import DAG
from datetime import datetime
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.http_download_operations import HttpDownloadOperator
from airflow.operators.zip_file_operations import UnzipFileOperator
from airflow.operators.hdfs_operations import HdfsPutFileOperator, HdfsMkdirFileOperator

args = {
    'owner': 'airflow'
}

dag = DAG('cell_towers_create_full_db', default_args=args, description='Project',
          schedule_interval='@once',
          start_date=datetime(2022, 12, 1), catchup=False, max_active_runs=1)

# ---Dags for Full Cell Towers---

create_download_dir_full = BashOperator(
    task_id='create_import_dir',
    bash_command='mkdir -p /home/airflow/opencellid/raw/full',
    dag=dag,
)

download_cell_towers_full = HttpDownloadOperator(
    task_id='download_cell_towers',
    download_uri='https://opencellid.org/ocid/downloads?token=pk.fda3225a822fea93e9da4e4c6ba0c9ed&type=full&file=cell_towers.csv.gz', #muss durch die offizielle URL getauscht werden!
    save_to='/home/airflow/opencellid/raw/full/cell_towers_full.csv.gz',
    dag=dag,
)

unzip_cell_towers_full = UnzipFileOperator(
    task_id='unzip_cell_towers',
    zip_file='/home/airflow/opencellid/raw/full/cell_towers_full.csv.gz',
    extract_to='/home/airflow/opencellid/raw/full/cell_towers_full.csv',
    dag=dag,
)

create_hdfs_raw_dir_full = HdfsMkdirFileOperator(
    task_id='create_hdfs_cell_towers_partition_dir',
    directory='/user/hadoop/opencellid/raw/full',
    hdfs_conn_id='hdfs',
    dag=dag,
)

hdfs_put_cell_towers_full = HdfsPutFileOperator(
    task_id='upload_tower_cells_to_hdfs',
    local_file='/home/airflow/opencellid/raw/full/cell_towers_full.csv',
    remote_file='/user/hadoop/opencellid/raw/full/cell_towers_full.csv',
    hdfs_conn_id='hdfs',
    dag=dag,
)

pyspark_cell_towers_full = SparkSubmitOperator(
    task_id='pyspark_cell_towers',
    conn_id='spark',
    application='/home/airflow/airflow/python/pyspark_cell_towers.py',
    total_executor_cores='2',
    executor_cores='2',
    executor_memory='2g',
    num_executors='2',
    name='spark_cell_towers',
    verbose=True,
    application_args=['--hdfs_source_dir', '/user/hadoop/opencellid/raw/full/', '--hdfs_target_dir', '/user/hadoop/opencellid/final/full', '--hdfs_target_format', 'csv', '--full_or_diff', 'full'],
    dag = dag
)

# ---Workflow----

create_download_dir_full >>  download_cell_towers_full >> unzip_cell_towers_full
unzip_cell_towers_full >> create_hdfs_raw_dir_full >> hdfs_put_cell_towers_full >> pyspark_cell_towers_full