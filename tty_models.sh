#!/bin/bash

docker run -it --name models -p 8001:8000 -v /home/webmin/ISA_code/models_server_code:/app --link mysql:db_host tp33/django:devel 
