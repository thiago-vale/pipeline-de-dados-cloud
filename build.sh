#!/bin/bash

# Nome da imagem do Docker
IMAGE_NAME="pipeline-cloud"

# Construir a imagem
docker build -t $IMAGE_NAME .