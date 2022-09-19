#!/bin/bash

echo "##### Build docker-image !#####"

docker build ./myapp2.0 -t  myapp:2.0

sleep 2
echo "###### Run docker-image !###### "

docker run -d -p 5000:80  myapp:2.0

sleep 2
echo "###### Open in browser !##### "

firefox localhost:5000

echo "###### Stopping container ! #####"

for i in $(docker ps | grep "myapp" | cut -d" " -f1 ); do docker stop $i; done  

sleep 2
echo "###### Delete image ! #######"

for i in $(docker images | grep myapp | cut -d" " -f33); do docker rmi -f $i; done

sleep 2
echo "###### End !#######"