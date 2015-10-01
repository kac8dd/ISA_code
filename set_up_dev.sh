#!/bin/bash

docker run -d --name models -p 8001:8000 -v /home/webmin/ISA_code/models_api:/app --link mysql:db_host tp33/django:devel mod_wsgi-express start-server models_api/wsgi.py 

docker run -d --name exp -p 8001:8000 -v /home/webmin/ISA_code/exp_server_code:/app --link models:models_host tp33/django:devel mod_wsgi-express start-server models_api/wsgi.py

docker run -d --name models -p 8001:8000 -v /home/webmin/ISA_code/web_frontend_server_code:/app --link exp:exp_host tp33/django:devel mod_wsgi-express start-server models_api/wsgi.py


