#!/usr/bin/env python3

import gpiod
import time
#sets the gpio chips that we need
chip0 = gpiod.Chip('gpiochip0')
chip1 = gpiod.Chip('gpiochip1')
CONSUMER='getset'

#sets which pins are hooked to leds
rled = chip1.get_lines([28])
gled = chip1.get_lines([18])
bled = chip1.get_lines([19])
yled = chip0.get_lines([4])
#sets the pins as outputs
rled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
gled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
bled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
yled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)

#sets which pins are hooked to leds
rbut = chip0.get_lines([30])
gbut = chip0.get_lines([31])
bbut = chip1.get_lines([16])
ybut = chip0.get_lines([5])
#sets the pins as inputs
rbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
gbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
bbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
ybut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)




while True:
    #checks whether a switch has been pressed
    rval = rbut.get_values()
    gval = gbut.get_values()
    bval = bbut.get_values()
    yval = ybut.get_values()
    
    #inverts the switch value to turn on when pressed
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
    
    #sets the led to the value previously determined
    rled.set_values(rval)
    gled.set_values(gval)
    bled.set_values(bval)
    yled.set_values(yval)