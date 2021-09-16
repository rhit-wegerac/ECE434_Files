#!/usr/bin/env python3
import gpiod
import time


#selects which gpio chip we need
chip1 = gpiod.Chip('gpiochip1')


line= chip1.get_lines([28])#sets line to be the GPIO pin
line.request(consumer='blink', type = gpiod.LINE_REQ_DIR_OUT)#sets the pin as output


t = 0.000001 #time for sleep

while True:
    line.set_values([0]) #turns pin off
    time.sleep(t) #system sleeps
    line.set_values([1]) #turns pin on
    time.sleep(t) #system sleeps