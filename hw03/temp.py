#!/usr/bin/env python3

###############################################################################################
# Author: Andrew Weger                                                                        #
# Date last modified: 9/24/2021                                                               #
# Description: This is a program that uses two TMP101, sets T_high and T_low on both and      #
#               prints the temperature if the temperature goes above T_high                   #
# I Andrew Weger pledge that the code below is 100% of my doing, and has not been plagiarized.#
###############################################################################################

import os
import time
import smbus
import gpiod

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
    