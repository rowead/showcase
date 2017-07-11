#!/usr/bin/python
import socket
import time
import json
import urllib
import logmatic
import logging
import Adafruit_DHT

response = urllib.urlopen("http://andrewrowe.online.test.api.s3-ap-southeast-2.amazonaws.com/27.json")
showcase_info = json.loads(response.read().decode())

logger = logging  .getLogger()
log_handler = logging.handlers.WatchedFileHandler('/var/log/showcase/showcase.log')
log_handler.setFormatter(logmatic.JsonFormatter(extra={"hostname":socket.gethostname()}))
logger.addHandler(log_handler)

logger.setLevel(logging.INFO)


while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    logger.info({'Temperature': '{:0.1f}'.format(temperature),
                 'Humidity': '{:0.1f}'.format(humidity)},
                  extra=showcase_info)
    time.sleep(60)
