# -*- coding: utf-8 -*-

"""
Title: Cell Towers Dag
Author: Simon Weiss
Description: Download and creation auf Full Cell Towers Csv in HDFS and MySQL
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.operators.http_download_operations import HttpDownloadOperator
from airflow.operators.zip_file_operations import UnzipFileOperator
from airflow.operators.hdfs_operations import HdfsPutFileOperator, HdfsMkdirFileOperator
from airflow.operators.filesystem_operations import ClearDirectoryOperator

args = {
    'owner': 'airflow'
}

dag = DAG('cell_towers_create_full_db', default_args=args, description='Project',
          schedule_interval='56 18 * * *',
          start_date=datetime(2022, 11, 21), catchup=False, max_active_runs=1)

# ----------- Hadoop Filesystem Aufgaben ----------

create_local_import_dir = BashOperator(
    task_id='create_import_dir',
    bash_command='mkdir -p /home/airflow/opencellid/raw',
    dag=dag,
)

clear_local_import_dir = ClearDirectoryOperator(
    task_id='clear_import_dir',
    directory='/home/airflow/opencellid/raw',
    pattern='cell_towers.*',
    dag=dag,
)

# download_cell_towers = HttpDownloadOperator(
#     task_id='download_cell_towers',
#     download_uri='https://opencellid.org/ocid/downloads?token=pk.fda3225a822fea93e9da4e4c6ba0c9ed&type=full&file=cell_towers.csv.gz', #muss durch die offizielle URL getauscht werden!
#     save_to='/home/airflow/opencellid/raw/cell_towers_full.csv.gz',
#     dag=dag,
# )

unzip_cell_towers = UnzipFileOperator(
    task_id='unzip_cell_towers',
    zip_file='/home/airflow/opencellid/raw/cell_towers_full.csv.gz',
    extract_to='/home/airflow/opencellid/raw/cell_towers_full.csv',
    dag=dag,
)

create_hdfs_cell_towers_partition_dir = HdfsMkdirFileOperator(
    task_id='create_hdfs_cell_towers_partition_dir',
    directory='/user/hadoop/opencellid/cell_towers',
    hdfs_conn_id='hdfs',
    dag=dag,
)

hdfs_put_tower_cells = HdfsPutFileOperator(
    task_id='upload_tower_cells_to_hdfs',
    local_file='/home/airflow/opencellid/raw/cell_towers_full.csv',
    remote_file='/user/hadoop/opencellid/cell_towers/cell_towers_full.csv',
    hdfs_conn_id='hdfs',
    dag=dag,
)

pyspark_cell_towers = SparkSubmitOperator(
    task_id='pyspark_cell_towers',
    conn_id='spark',
    application='/home/airflow/airflow/python/pyspark_cell_towers.py',
    total_executor_cores='2',
    executor_cores='2',
    executor_memory='2g',
    num_executors='2',
    name='spark_cell_towers',
    verbose=True,
    application_args=['--hdfs_source_dir', '/user/hadoop/opencellid/cell_towers/', '--hdfs_target_dir', '/user/hadoop/opencellid/final', '--hdfs_target_format', 'csv', '--full_or_diff', 'full'],
    dag = dag
)

# ---------------------------------------------------------------------------------------------



# -------------------- Workflow --------------------

create_local_import_dir >> clear_local_import_dir >> unzip_cell_towers
unzip_cell_towers >> create_hdfs_cell_towers_partition_dir >> hdfs_put_tower_cells >> pyspark_cell_towers