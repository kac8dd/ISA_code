#!/bin/bash

docker stop web
docker rm web
docker stop exp
docker rm exp
docker stop models
docker rm models

