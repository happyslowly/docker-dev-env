#!/usr/bin/env bash

#docker build \
#    -f ../Dockerfile.base \
#    --build-arg uid=45427 \
#    --build-arg gid=100 \
#    -t xixu/dev-base .

docker build \
    -f ../Dockerfile.ml \
    -t xixu/dev-ml .
