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
