#!/usr/bin/env python3

import gpiod
import time
chip0 = gpiod.Chip('gpiochip0')
chip1 = gpiod.Chip('gpiochip1')
CONSUMER='getset'


rled = chip1.get_lines([28])
gled = chip1.get_lines([18])
bled = chip1.get_lines([19])
yled = chip0.get_lines([4])
rled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
gled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
bled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
yled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)


rbut = chip0.get_lines([30])
gbut = chip0.get_lines([31])
bbut = chip1.get_lines([16])
ybut = chip0.get_lines([5])
rbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
gbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
bbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
ybut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)




while True:
    rval = rbut.get_values()
    gval = gbut.get_values()
    bval = bbut.get_values()
    yval = ybut.get_values()
        
    if rval == [0]:
        rval = [1]
    else: 
        rval = [0]
        
    if gval == [0]:
        gval = [1]
    else: 
        gval = [0]
        
    if bval == [0]:
        bval = [1]
    else: 
        bval = [0]
    
    if yval == [0]:
        yval = [1]
    else: 
        yval = [0]
    
    rled.set_values(rval)
    gled.set_values(gval)
    bled.set_values(bval)
    yled.set_values(yval)