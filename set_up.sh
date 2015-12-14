#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker run -d --name kafka --env ADVERTISED_HOST=kafka --env ADVERTISED_PORT=9092 spotify/kafka

docker run -d -p 9200:9200 --name es elasticsearch:2.0 -Des.network.host=es

docker run -d --name models_1 -p 8000:8000 -v $DIR/models_server_code:/app --link mysql:db_host tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes models_server_code/wsgi.py 

docker run -d --name models_2 -p 8001:8000 -v $DIR/models_server_code:/app --link mysql:db_host tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes models_server_code/wsgi.py

docker run -d --name models_lb -p 8052:80 --link models_1:models_1  --link models_2:models_2 tutum/haproxy

docker run -d --name exp_1 -p 8002:8000 -v $DIR/exp_server_code:/app --link models_lb:models_host --link kafka:kafka --link es:es tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes exp_server_code/wsgi.py

docker run -d --name exp_2 -p 8003:8000 -v $DIR/exp_server_code:/app --link models_lb:models_host --link kafka:kafka --link es:es tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes exp_server_code/wsgi.py

echo "hello"

docker run -d --name exp_lb -p 8051:80 --link exp_1:exp_1 --link exp_2:exp_2 tutum/haproxy

docker run -d --name web_1 -p 8004:8000 -v $DIR/web_frontend_server_code:/app --link exp_lb:exp_host tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes web_frontend_server_code/wsgi.py

docker run -d --name web_2 -p 8005:8000 -v $DIR/web_frontend_server_code:/app --link exp_lb:exp_host tp33/django:1.1 mod_wsgi-express start-server --reload-on-changes web_frontend_server_code/wsgi.py

docker run -d --name web_lb -p 8050:80 --link web_1:web_1 --link web_2:web_2 tutum/haproxy 

docker run -d --name batch --link kafka:kafka --link es:es zeizyy/isa_batch python ISA_batch/batch.py

sleep 5

docker start batch
