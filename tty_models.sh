#!/bin/bash


docker run -it --name $1 -p 8001:8000 -v /home/webmin/ISA_code/"$1"_server_code:/app --link mysql:db_host tp33/django:devel  
