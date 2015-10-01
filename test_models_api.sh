#!/bin/bash

#############################################################
## This script does the following for each type of model
## 	create new object and save to the database 
## 	get that object back from the database
## 	update that object and save to the database
## 	get updated version of that object back from the database
#############
## If one of the curl commands below is not working properly
## 	append the command with " > response.html && firefox response.html" 
##	then rerun the script and observe the debug output in firefox
############################################################# 
curl localhost:8001/api/v1/create/event/ --data "name=test_event_1&description=test_description&start_time=2015-12-03&location=test_location"
 
echo "";echo "" 

curl localhost:8001/api/v1/get/event/1/
echo "";echo "" 

curl localhost:8001/api/v1/update/event/1/ --data "name=updated_name&description=updated_description&start_time=2050-12-03&location=updated_location" 
echo "";echo "" 

curl localhost:8001/api/v1/get/event/1/
echo "";echo ""

curl localhost:8001/api/v1/create/ticket/ --data "name=ticket_name&price=10.5&event_id=1&amount=200"  
echo "";echo""

curl localhost:8001/api/v1/get/ticket/1/
echo "";echo""

curl localhost:8001/api/v1/update/ticket/1/ --data "name=updated_ticket_name&price=15.5&event_id=1&amount=250"
echo "";echo ""

curl localhost:8001/api/v1/get/ticket/1/
echo "";echo ""

curl localhost:8001/api/v1/create/user/ --data "username=test_username&password=test_password&firstname=John&lastname=Doe"  
echo "";echo ""

curl localhost:8001/api/v1/get/user/1/ 
echo "";echo ""

curl localhost:8001/api/v1/update/user/1/ --data "password=updated_password&firstname=Jane&lastname=Philips" 
 
 
echo "";echo ""

curl localhost:8001/api/v1/get/user/1/
echo "";echo ""

curl localhost:8001/api/v1/create/purchase/ --data "user_id=1&ticket_id=1" 
echo "";echo ""

curl localhost:8001/api/v1/get/purchase/1/ 
 
