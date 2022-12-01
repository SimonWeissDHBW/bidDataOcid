# Big Data Open Cell ID

## Installing and Running

Clone the repo into your VM.

```
git clone https://github.com/SimonWeissDHBW/bigDataOcid.git
```

Move into the docker container

```
cd bigDataOcid/docker
```

Create the docker containers with a docker compose

```
docker-compose up -d
```

Enter the hadoop docker and start hadoop

```
docker exec -it hadoop bash
sudo su hadoop
cd
start-all.sh
```

Now you can unpause the dags to fill the database. For that open [ip-of-your-vm]:8080 and press the on/off toggle of cell_towers_create_full_db and cell_towers_add_diff_db . The cell_towers_create_full_db dag will be triggered immediately and create the base for your database. This can take some time (up to 2 hours) because of the huge amount of data. The cell_towers_add_diff_db dab will be triggered everyday at 5 am and put the newest diff data into the table.

Now you can open the server with
[ip-of-your-vm]:[port]

Here are the correspondings ports - the website -> 3000 - hadoop -> 9870 - airflow -> 8080

List of Dags

ocid\*full
create_download_dir\_{full or diff}
Creates a directory, which the csv file will be downloaded into
Erstellt ein Ordner, in den die Downloads importiert werden

download_cell_towers\_{full or diff}
Downloads the (zipped) csv file from the opencellid api

unzip_cell_towers\_{full or diff}
Unzips the downloaded file to create a csv file

create_hdfs_raw_dir\_{full or diff}
Creates a directory in HDFS for the import of the csv
Erstellt eine Ordner im Hadoop File System für den Import der CSV Datei

hdfs_put_cell_towers\_{full or diff}
Copies the csv file to the created HDFS directory
Kopiert die CSV Datei in den frisch erstellten Ornder nach Hadoop

pyspark_cell_towers\_{full or diff}
Executes pyspark_cell_towers.py. In this file the data is partitioned saved as a parquet file in HDFS and put into multiple MySQL tables.
