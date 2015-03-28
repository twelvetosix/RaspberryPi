#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO_OUT = 4

GPIO.setup(17, GPIO.OUT)

try:
	while 1:
		GPIO.output(17, GPIO.LOW)
		print "Setting Low"
		time.sleep(1)
		GPIO.output(17, GPIO.HIGH)
		print "Setting High"		
		time.sleep(5)

except KeyboardInterrupt:
	print "Quit"
	GPIO.cleanup()
	
	