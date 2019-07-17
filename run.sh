#!/usr/bin/env bash

docker run -d --restart=always \
  --name=picamera \
  --device /dev/vchiq \
  -p 8000:8000 \
  -e AUTH_USERNAME=pi \
  -e AUTH_PASSWORD=picamera \
  -e VFLIP=true \
  dakl/picamera
