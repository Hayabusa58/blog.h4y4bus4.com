#!/bin/bash

docker run -u "$(id -u):$(id -g)" -v $PWD:/app --workdir /app -p 8088:8088 ghcr.io/getzola/zola:v0.19.1 serve --interface 0.0.0.0 --port 8088 --base-url localhost
