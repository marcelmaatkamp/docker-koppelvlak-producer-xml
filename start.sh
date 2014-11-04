#!/bin/bash
docker rm koppelvlak-producer; docker run --name koppelvlak-producer -d -t --link rabbitmq:rabbitmq -v /koppelvlak:/koppelvlak koppelvlak/producer:latest
