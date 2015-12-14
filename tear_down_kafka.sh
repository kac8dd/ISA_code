#!/bin/bash

docker stop web_1 
docker rm web_1 

docker stop web_2
docker rm web_2

docker stop exp_1 
docker rm exp_1 

docker stop exp_2
docker rm exp_2

docker stop models_1 
docker rm models_1

docker stop models_2
docker rm models_2 

docker stop batch
docker rm batch

docker stop es
docker rm es

docker stop kafka
docker rm kafka

docker stop web_lb 
docker rm web_lb

docker stop exp_lb
docker rm exp_lb

docker stop models_lb
docker rm models_lb


