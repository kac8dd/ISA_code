#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker run -d --name models -p 8001:8000 -v $DIR/../models_server_code:/app --link mysql:db_host tp33/django:devel mod_wsgi-express start-server models_server_code/wsgi.py

docker run -it --name exp -p 8002:8000 -v $DIR/../exp_server_code:/app --link models:models_host tp33/django:devel  
