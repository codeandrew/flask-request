#!/bin/sh

docker build -t flask-request .
docker run -p 8001:80 flask-request
