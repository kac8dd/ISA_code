#!/bin/bash

#########################################################
## This script is meant to test the experience api server
##	from outside the container using curl responses
##############
## currently it asks the api for the homepage service
##	and the eventpage service for event.id=1
#########################################################

curl localhost:8002/api/v1/home/ > response.html && firefox *html
echo"hello"; 
echo ""; echo ""

#curl localhost:8002/api/v1/view_event/event=1/
echo ""; echo "" 
