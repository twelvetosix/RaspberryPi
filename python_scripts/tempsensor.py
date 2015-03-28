import time
from datetime import datetime
import time
import MySQLdb

db = MySQLdb.connect(host="localhost",
                     user="root",
					  passwd="skelnjr3",
					  db="raspberrypi")
					  
cur = db.cursor()

while 1:
	i = datetime.now()
	tempfile = open("/sys/bus/w1/devices/28-0014156038ff/w1_slave")
    	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temp = float(tempdata[2:])
	temp = temp / 1000
	temp = temp * 9
	temp = temp / 5
	temp = temp + 32
#	print i.strftime('%Y-%m-%d %H:%M:%S')
#	print temp
	cur.execute("INSERT INTO TempLog (Date, Temp) VALUES ('%s', '%s')" % (i.strftime('%Y-%m-%d %H:%M:%S'), temp))
	db.commit()
	time.sleep(5)

	
