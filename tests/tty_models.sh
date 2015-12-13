#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

docker run -it --name models -p 8001:8000 -v $DIR/../models_server_code:/app --link mysql:db_host tp33/django:devel

