FROM dakl/arm32-python-alpine-qemu:3.7.1-slim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY app /app
WORKDIR /app

ENV AUTH_USERNAME=pi RESOLUTION=800x600 FRAMERATE=24

ENTRYPOINT ["/usr/local/bin/python", "/app/run.py"]
