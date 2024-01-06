#!/bin/bash

docker-compose stop -t 0
docker-compose down
docker-compose up -d
