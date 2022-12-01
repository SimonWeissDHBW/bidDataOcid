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

Now you can open the server with
[Your VM IP-adress]:[port]

Here are the correspondings ports - the website -> 3000 - hadoop -> 9870 - airflow -> 8080

List of Dags

ocid*full
create_download_dir*{full or diff}
Erstellt ein Ordner, in den die Downloads importiert werden

download*cell_towers*{full or diff}
Downloaded die verpackte Cell-Towers CSV in den erstellten Ordner

unzip*cell_towers*{full or diff}
Entpackt die verpackte Cell-Towers CSV

create*hdfs_raw_dir*{full or diff}
Erstellt eine Ordner im Hadoop File System für den Import der CSV Datei

hdfs*put_cell_towers*{full or diff}
Kopiert die CSV Datei in den frisch erstellten Ornder nach Hadoop

pyspark*cell_towers*{full or diff}
Führt die Pyspark Datei aus. Diese Datei speichert die Tabelle partitioniert in HDFS ab und erstellt daraus mehrere MYSQL Table.

ocid_diff
