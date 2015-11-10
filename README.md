# ISA_code

A ticket hosting website. By Kevin Clark, Kyle O'Donnell and Ian Zheng

(kac8dd@virginia.edu, kpo4fz@virginia.edu, yz9fy@virginia.edu)


This directory contains a number of scripts designed to help initialize/debug/build our website


	sh set_up_kafka.sh 
- starts all three layers(models, exp, web front-end) with mod_wsgi-express and the containers for Kafka, Batch and Elastic Search.

- need to modify the -v tag to mount your file path onto the container in the set_up_kafka.sh file.

	sh tear_down_kafka.sh 
- stops, and then removes all six containers
