#!/usr/bin/env bash
docker buildx rm
docker buildx create --use
docker buildx build --no-cache -t tg-client:1.0 --load --progress=plain .

docker tag tg-client:1.0 sigeshuo/tg-client:1.0
docker tag tg-client:1.0 sigeshuo/tg-client:latest