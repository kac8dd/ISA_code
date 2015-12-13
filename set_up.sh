#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker run -d --name kafka --env ADVERTISED_HOST=kafka --env ADVERTISED_PORT=9092 spotify/kafka

docker run -d -p 9200:9200 --name es elasticsearch:2.0 -Des.network.host=es

docker run -d --name models -p 8001:8000 -v $DIR/models_server_code:/app --link mysql:db_host tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes models_server_code/wsgi.py 

docker run -d --name exp -p 8004:8000 -v $DIR/exp_server_code:/app --link models:models_host --link kafka:kafka --link es:es tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes exp_server_code/wsgi.py

docker run -d --name web -p 8003:8000 -v $DIR/web_frontend_server_code:/app --link exp:exp_host tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes web_frontend_server_code/wsgi.py

docker run -d --name batch --link kafka:kafka --link es:es zeizyy/isa_batch python ISA_batch/batch.py

sleep 5

docker start batch
