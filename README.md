# ISA_code

A ticket hosting website. By Kevin Clark, Kyle O'Donnell and Ian Zheng

(kac8dd@virginia.edu, kpo4fz@virginia.edu, yz9fy@virginia.edu)


This directory contains a number of scripts designed to help initialize/debug/build our website


	sh set_up_kafka.sh 
- starts all three layers(models, exp, web front-end) with mod_wsgi-express and the containers for Kafka, Batch and Elastic Search.

** need to modify the -v tag to mount your file path onto the container in the set_up_kafka.sh file.

	sh tear_down_kafka.sh 
- stops, and then removes all six containers

	sh tty_[models | exp | web].sh 
- starts all layers below the one selected and then
				starts and attaches to the container layer in
				the script's name 
- this is useful if you want to see the django debug server's output
				as you are communicating with it. You will still have to run
				'~$ python manage.py runserver 0.0.0.0:8000' manually to start the
				uppermost layer

	sh test_models_api.sh 
- sends curl requests to the models server (port forwarded through localhost:8001)
			For each type of model in our database, the script uses the api to
			'create' and object, then 'get' that object, then 'update' that object, then
			'get' that object again. The two 'get's are used to confirm the api properly saves
			updates to the database.
- output will be a confirmation message in json indicating a successfull create/update or all the object's data fields represented in json 

	sh test_exp_api.sh 
- sends curl requests the the two implemented experience services, the homepage service
			and the eventpage service.

	test_get_latest.sh 
- sends curl requests to the models layer to make 7 user, event, and ticket objects
			It then calls the models layer to get the latest 5 events. This functionality
			was implemented at the models layer to optimize the homepage service. This script
			is ALSO useful for initializing the database with enough objects so that the
			visiting the homepage service in a browser will work correctly 
