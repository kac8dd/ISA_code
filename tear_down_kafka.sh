#!/bin/bash

docker stop web
docker rm web

docker stop exp
docker rm exp

docker stop models
docker rm models

docker stop batch
docker rm batch

docker stop es
docker rm es

docker stop kafka
docker rm kafka




