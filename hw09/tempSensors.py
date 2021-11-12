#!/usr/bin/env python
import time

# w1="/sys/bus/w1/devices/28-00000114ef1b/w1_slave"
w1 = "/sys/class/hwmon/hwmon0/temp1_input"
w2 = "/sys/class/hwmon/hwmon1/temp1_input"
w3 = "/sys/class/hwmon/hwmon2/temp1_input"
while True:
    print "******************************************************"
    raw = open(w1, "r").read()
    print "Temperature sensor 1 is "+str(float(raw.split("t=")[-1])/1000)+" degrees"
    raw = open(w2, "r").read()
    print "Temperature sensor 2 is "+str(float(raw.split("t=")[-1])/1000)+" degrees"
    raw = open(w3, "r").read()
    print "Temperature sensor 3 is "+str(float(raw.split("t=")[-1])/1000)+" degrees"
    time.sleep(1)
