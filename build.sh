#!/bin/bash

# Nome da imagem do Docker
IMAGE_NAME="pipeline-de-dados:0.0.1"

# Construir a imagem
docker build -t $IMAGE_NAME .