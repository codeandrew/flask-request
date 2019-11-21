#!/bin/sh

docker build -t codeandrew/flask-request:$1 .
docker push codeandrew/flask-request:$1
