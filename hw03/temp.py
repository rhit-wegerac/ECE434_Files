#!/usr/bin/env python3

import os
import time
import smbus
import gpiod

# while True:
#     time.sleep(0.5)
#     temp1 = os.popen('sudo i2cget -y 2 0x4a 00').read()
#     temp2 = os.popen('sudo i2cget -y 2 0x48 00').read()
#     temp1int = (int(temp1,base=16) * 1.8) + 32
#     temp2int = (int(temp2,base=16) * 1.8) + 32
#     print("Temp 1: " + str(round(temp1int,2)) + "\N{DEGREE SIGN}" + "F")
#     print("Temp 2: " + str(round(temp2int,2)) + "\N{DEGREE SIGN}" + "F")
#     print("*********************")

bus = smbus.SMBus(2)
address1 = 0x4a
address2 = 0x48

os.system("sudo i2cset -y 2 0x4a 1 0x00")
os.system("sudo i2cset -y 2 0x4a 2 0x1D")
os.system("sudo i2cset -y 2 0x4a 3 0x1E")
os.system("sudo i2cset -y 2 0x48 1 0x00")
os.system("sudo i2cset -y 2 0x48 2 0x1D")
os.system("sudo i2cset -y 2 0x48 3 0x1E")

chip0 = gpiod.Chip('gpiochip0')
CONSUMER='getset'
sens1 = chip0.get_lines([30])
sens2 = chip0.get_lines([31])
sens1.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
sens2.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)

test = bus.read_byte_data(address1,1)
test1 = bus.read_byte_data(address1,2)
test2 = bus.read_byte_data(address1,3)
while True:
    # temp1 = bus.read_byte_data(address1,0)
    # temp2 = bus.read_byte_data(address2,0)
    # print(str(temp1) + " " + str(temp2), end="\r")
    # time.sleep(0.25)
    temp1 = sens1.get_values()
    temp2 = sens2.get_values()
    if temp1 == [0]:
        temp1 = (bus.read_byte_data(address1,0) * 1.8) + 32;
        print("Temperature Sensor 1: " + str(temp1) + "\N{DEGREE SIGN}" + "F")
        time.sleep(0.5)
        
    if temp2 == [0]:
        temp2 = (bus.read_byte_data(address2,0) * 1.8) + 32;
        print("Temperature Sensor 2: " + str(temp2) + "\N{DEGREE SIGN}" + "F")
        time.sleep(0.5)
    