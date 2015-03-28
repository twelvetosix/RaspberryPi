#!/usr/bin/python

from datetime import datetime
import serial
import time
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
					  passwd="skelnjr3",
					  db="raspberrypi")
					  
cur = db.cursor()

ser = serial.Serial('/dev/ttyACM0',9600)
ser.open()
ser.readline()

while 1:	
	i = datetime.now()
	data = ser.readline()
	print i.strftime('%Y-%m-%d %H:%M:%S') + " " + data
	if data <= 0:
		# do nothing
		print "ERROR"	
	else:		
		floatTemp = float(data)
		cur.execute("INSERT INTO LogTable (Date, Temp) VALUES ('%s', '%f')" % (i.strftime('%Y-%m-%d %H:%M:%S'), floatTemp))
		db.commit()
	time.sleep(5)
	

	
	
