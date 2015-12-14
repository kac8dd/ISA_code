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

for ((i=1; i <= 7 ; i++))
do
	curl localhost:8001/api/v1/create/user/ --data "username=test_username$i&password=test_password&firstname=John&lastname=Doe" 
	echo "";echo "" 


	curl localhost:8001/api/v1/create/event/ --data "name=test_event_$i&description=test_description&start_time=2015-12-03&location=test_location&creator_id=1"  
	echo "";echo "" 
	
	curl localhost:8001/api/v1/create/ticket/ --data "price=25.00&event_id=$i&amount=33"
	echo "";echo ""
done
	
curl localhost:8001/api/v1/get/latest/5/ 
echo "";echo "" 
