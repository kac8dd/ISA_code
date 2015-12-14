ISA_code
========

A ticket hosting website by Kevin Clark, Kyle O'Donnell and Ian Zheng.

(kac8dd@virginia.edu, kpo4fz@virginia.edu, yz9fy@virginia.edu)

Set Up
------
- For Developers (who have the code checked out and database configured)
```
sh set_up_kafka.sh
```

- For Others (who have an empty database named 'cs4501', user 'www' and password 'S3cure')
```
sh scratch_setup.sh
sh initialize_db.sh 
```
In either case the shell script starts all three layers(models, exp, web front-end) with mod_wsgi-express and the containers for Kafka, Batch and Elastic Search. The shell script uses UNIX pwd command to mount to the corresponding directory so that there is no need to modify the -v flag when starting the docker containers. It also takes into account all the gliches of the Kafka so that you only need to run the script once and everything will be set up properly. The Web App can be accessed at the following URL when after the set-up.
```
http://localhost:8050		
	
	This request will hit the front load balancer, to directly communicate with
	a specifc container, examine set_up.sh to see which port should be used 
```

Tear Down
---------
```
sh tear_down_kafka.sh
```
- stops, and then removes all containers
