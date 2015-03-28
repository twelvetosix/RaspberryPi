import time

while 1:
	tempfile = open("/sys/bus/w1/devices/28-0014156038ff/w1_slave")
    	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temp = float(tempdata[2:])
	temp = temp / 1000
	temp = temp * 9
	temp = temp / 5
	temp = temp + 32
	print temp

	time.sleep(3)
