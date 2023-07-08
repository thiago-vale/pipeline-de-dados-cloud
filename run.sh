#!/bin/bash

# Nome da imagem do Docker
IMAGE_NAME="pipeline-cloud"

# Nome do contêiner
CONTAINER_NAME="docker-lake"

# Porta para mapeamento (altere conforme necessário)
HOST_PORT=8080
CONTAINER_PORT=80

# Executar o contêiner
docker run -d -p $HOST_PORT:$CONTAINER_PORT --name $CONTAINER_NAME $IMAGE_NAME
