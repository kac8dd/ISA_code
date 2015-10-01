#!/bin/bash

docker run -it --name models -p 8001:8000 -v /home/webmin/ISA_code:/app --link mysql:db tp33/django:devel 

