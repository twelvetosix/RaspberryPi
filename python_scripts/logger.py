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
	cur.execute("INSERT INTO TempLog (Date, Temp) VALUES ('%s', '%s')" % (i.strftime('%Y-%m-%d %H:%M:%S'), data))
	db.commit()
	time.sleep(5)
	

	
	
