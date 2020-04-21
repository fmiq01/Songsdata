REST API developed ECECS781P CLOUD COMPUTING(2019/20) Mini-Project This RESTful Application Program Interface (API) is developed using Python and Flask. It provides a simple REST API of over 55000 song lyrics with there artist names.

Below are he steps that were followed and implemented in this project.

            Create a directory
mkdir cloudproject && cd cloudproject

            Install the  python package installer
sudo apt update sudo apt install python3pip 

            Install docker container for cloud deployment.
sudo apt install docker.io

             Set up single node Cassandra inside a docker container
sudo docker pull cassandra:latest

              Run a Cassandra instance in  docker
sudo docker run --name cassandra-test -p 9042:9042 -d cassandra:latest 

          Call dataset into the instance. (songdata.csv can be founf on the link below).
wget -O songdata.csv https://tinyurl.com/sbj72fc 

             Check the first few lines and last few lines of downloaded CSV.
head songdata.csv tail songdata.csv

              Copy the dataset into container.
sudo docker cp songdata.csv cassandra-test:/home/songdata.csv 

            Interacting Cassandra via its native command line shell cliet 'cqlsh' using CQL (Cassandra Quert Language)
sudo docker exec -it cassandra-test cqlsh 

                Create keyspace for the data to be inserted into.
CREATE KEYSPACE songdata WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1};

                    Specify the name and type of column in keyspace
CREATE TABLE songdata.stats (Artist text PRIMARY KEY,Song text,Link text,Text text); 

                     Copy the data from csv into the database.
COPY songdata.stats(Artist,Song,Link,Text) FROM '/home/songdata.csv' WITH DELIMITER=',' AND HEADER=TRUE;

             Connecting Flask to Cassandra 15. Open a new terminal with the same directory
cd cloudproject

Create requirements.txt file (Download from github)
nano requirements.txt 

Create docker file (Download from github)
nano Dockerfile 

Create app.py file (Download from github)
nano app.py 

Build the image
sudo docker build . --tag=cassandrarest:v1 

Run the service
sudo docker run -p 80:80 cassandrarest:v1 

                                        
                                     Sending Http request
In a new terminal and change to current directory.
cd cloudproject
We will now add out request which have been coded in the app.py(Download from github)

GET request
curl -v "insert your IP/Public DNS)

POST request
curl -i -H "Content-Type: application/json" -X POST -d '{"artist":[],"song":"Payphone"}' 'insert your IP/Public DNS)'

DELETE request
curl -X "DELETE" http://localhost:5000/records/ABBA 'insert your IP/Public DNS)'
