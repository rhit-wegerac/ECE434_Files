#!/usr/bin/env python3

###############################################################################################
# Author: Andrew Weger                                                                        #
# Date last modified: 9/24/2021                                                               #
# Description: This is a etch-a-sketch program that is displayed on a 8x8 matrix and          #
#               and controlled by two rotary encoders                                         #
# I Andrew Weger pledge that the code below is 100% of my doing, and has not been plagiarized.#
###############################################################################################


import os
import time
import smbus
import gpiod
import numpy as np
import sys 
from curtsies import Input

bus = smbus.SMBus(2)
matrix = 0x70

matrixGrid = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
                

row = [0b00000001, 0b00000010, 0b00000100, 0b00001000, 0b00010000, 0b00100000, 0b01000000, 0b10000000]

width = 7;
height = 7;

xPos = 0;
yPos = 0;
yPosB = 1;

bus.write_i2c_block_data(matrix,0, matrixGrid)

bus.write_byte_data(matrix, 0xFF, 0)

while(1):#game loop
    with Input(keynames='curses')as input_generator:#detects if there was a key pressed 
        for e in input_generator:
            if str(e) == 'KEY_UP': #checks if the up arrow was pressed
                time.sleep(0.1)#sleepsto give time for the player to lift off the key
                yPos = yPos + 1
                yPosB = yPosB * 2
                if (yPos > height):
                    yPos = height - 1
                    yPosB = yPosB / 2
                if (matrixGrid[xPos] & row[yPos] != row[yPos]):
                    matrixGrid[xPos] = matrixGrid[xPos] + yPosB
                    bus.write_i2c_block_data(matrix,0, matrixGrid)
                    bus.write_byte_data(matrix, 0xFF, 0)
                
            if str(e) == "KEY_DOWN":#checks if the down arrow was pressed
                time.sleep(0.1)#sleeps to give time for the player to lift off the key
                yPos = yPos - 1
                yPosB = int(yPosB / 2)
                if (yPos < 0):
                    yPos = 0
                    yPosB = 1 
                if (matrixGrid[xPos] & row[yPos] != row[yPos]):
                    matrixGrid[xPos] = matrixGrid[xPos] + yPosB
                    bus.write_i2c_block_data(matrix,0, matrixGrid)
                    bus.write_byte_data(matrix, 0xFF, 0)
            if str(e) == "KEY_LEFT":#checks if the left arrow was pressed
                time.sleep(0.1)#sleeps to give time for the player to lift off the key
                xPos = xPos - 2
                if (xPos < 0):
                    xPos = 0
                if (matrixGrid[xPos] & row[yPos] != row[yPos]):
                    matrixGrid[xPos] = matrixGrid[xPos] + yPosB
                    bus.write_i2c_block_data(matrix,0, matrixGrid)
                    bus.write_byte_data(matrix, 0xFF, 0)
            if str(e) == "KEY_RIGHT":#checks if the right arrow was pressed
                time.sleep(0.1)# sleeps to give time for the player to lift off the key
                xPos = xPos + 2
                if (xPos >= width * 2):
                    xPos = (width * 2)
                if (matrixGrid[xPos] & row[yPos] != row[yPos]):
                    matrixGrid[xPos] = matrixGrid[xPos] + yPosB
                    bus.write_i2c_block_data(matrix,0, matrixGrid)
                    bus.write_byte_data(matrix, 0xFF, 0)
            if str(e) == ' ':#check if the spacebar was pressed
                time.sleep(0.1)#gives time for the player to lift off the key
                matrixGrid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
                0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
                bus.write_i2c_block_data(matrix,0, matrixGrid)
                bus.write_byte_data(matrix, 0xFF, 0)
            
