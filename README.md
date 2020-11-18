# Datastream Example

I needed an exemplary datastream based on Apache Kafka and Python for a project. As I couldn't find something suitable I created this docker-compose App that provides an exemplary datastream. Maybe someone else finds this useful. The datastream periodically inserts data to a kafka topic called 'stream'

Data should be placed in the data folder. The filename must be specified in the Dockerfile.

## Requirements
- kafka-python (https://pypi.org/project/kafka-python/)

## Start/Stop the datastream
- Build the App (only first time and code changes): docker-compose build
- Start the App: docker-compose up
- Stop the App: STRG-C

## Read Events from the datastream
- Run the file consumer.py

After starting the App it takes about 30sec for the producer to send data to Kafka.
