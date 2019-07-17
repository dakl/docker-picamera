FROM resin/raspberry-pi-python:3

LABEL maintainer "Philipp Schmitt <philipp@schmitt.co>"

RUN pip install picamera

COPY app /app
WORKDIR /app

ENV AUTH_USERNAME=pi RESOLUTION=800x600 FRAMERATE=24

ENTRYPOINT ["/usr/local/bin/python", "/app/run.py"]
