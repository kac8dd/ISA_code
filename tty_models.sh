#!/bin/bash

docker run -it --name models -p 8001:8000 -v /home/webmin/ISA_code/exp_server_code:/app --link mysql:mysql_host tp33/django:devel python manage.py runserver 0.0.0.0:8000 
