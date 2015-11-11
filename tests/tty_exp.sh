#!/bin/bash

docker run -d --name models -p 8001:8000 -v /vagrant/ISA_code/models_server_code:/app --link mysql:db_host tp33/django:devel mod_wsgi-express start-server models_server_code/wsgi.py

docker run -it --name exp -p 8002:8000 -v /vagrant/ISA_code/exp_server_code:/app --link models:models_host tp33/django:devel  
