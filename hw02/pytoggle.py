#!/usr/bin/env python3
import gpiod
import time



chip1 = gpiod.Chip('gpiochip1')


line= chip1.get_lines([28])
line.request(consumer='blink', type = gpiod.LINE_REQ_DIR_OUT)


t = 0.000001

while True:
    line.set_values([0])
    time.sleep(t)
    line.set_values([1])
    time.sleep(t)