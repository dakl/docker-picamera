FROM resin/raspberry-pi-python:3

ENV READTHEDOCS=True
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /code
COPY . /code

ENV AUTH_USERNAME=pi RESOLUTION=800x600 FRAMERATE=24

CMD ["python", "run.py"]
