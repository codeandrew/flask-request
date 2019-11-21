#!/bin/sh

docker build -t flask-request .
docker run -p 8001:80  -v /Users/jeanandrewfuentes/Repo/flask-request:/usr/src/app flask-request 
