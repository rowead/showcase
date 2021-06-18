#!/usr/bin/python
import socket
import time
import json
import urllib
import logmatic
import logging
import Adafruit_DHT

# set showcase_info to empty json

# @TODO: turn the following into a function that only updates showcase_info if successful
response = urllib.request.urlopen("http://andrewrowe.online.test.api.s3-ap-southeast-2.amazonaws.com/showcases.json")
showcase_info = json.loads(response.read().decode())

logger = logging.getLogger()
log_handler = logging.handlers.WatchedFileHandler('/var/log/showcase/showcase.log')
# @TODO: get rid of unused fields logged by logmatic
log_handler.setFormatter(logmatic.JsonFormatter(fmt="%(message)",extra={"hostname": socket.gethostname()}))
logger.addHandler(log_handler)

logger.setLevel(logging.INFO)

while True:
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)
	# @TODO: check for strange readings and try again.
	num_tries = 0
	while (humidity == 0 or humidity > 100) and num_tries <= 5:
		humidity, temperature = Adafruit_DHT.read_retry(11, 4)
		num_tries += 1
	# @TODO: update showcase_info here and log an error and or log the staleness of the showcase_info maybe in the message field or http response code as additional field.
	offset = 0.0
	for showcase in showcase_info["Showcases"]:
		temp = temperature + offset
		hum = humidity + offset
		offset += 2.0
		logger.info({'Temperature': '{:0.1f}'.format(temp), 'Humidity': '{:0.1f}'.format(hum)}, extra=showcase)
	time.sleep(30)
