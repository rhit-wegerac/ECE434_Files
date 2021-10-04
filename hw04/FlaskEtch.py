#!/usr/bin/env python3

import os
import time
import smbus
import gpiod
import numpy as np
import sys 
from curtsies import Input
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2, eQEP2b, eQEP0
from flask import Flask, render_template, request



upEnc = RotaryEncoder(eQEP2)
upEnc.setAbsolute()
upEnc.enable()

sideEnc = RotaryEncoder(eQEP1)
sideEnc.setAbsolute()
sideEnc.enable()

chip1 = gpiod.Chip('gpiochip1')
CONSUMER='getset'
rotBut = chip1.get_lines([16])
rotBut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)


upEncPos = upEnc.position
sideEncPos = sideEnc.position

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

app = Flask(__name__)
@app.route('/')
def index():
        templateData = {
              'title' : 'Etch-a-Sketch',
        }
        return render_template('index.html')
        
@app.route("/<direction>/")
def action(direction):
    
    if direction == "up": #checks if the up arrow was pressed
        print("HELP")
        time.sleep(0.1)
        upEncPos = upEnc.position
        yPos = yPos + 1
        yPosB = yPosB * 2
        if (yPos > height):
            yPos = height - 1
            yPosB = yPosB / 2
        if (matrixGrid[xPos] & row[yPos] != row[yPos]):
            matrixGrid[xPos] = matrixGrid[xPos] + yPosB
            bus.write_i2c_block_data(matrix,0, matrixGrid)
            bus.write_byte_data(matrix, 0xFF, 0)
        
    if direction == "down":
        time.sleep(0.1)#sleeps to give time for the player to lift off the key
        upEncPos = upEnc.position
        yPos = yPos - 1
        yPosB = int(yPosB / 2)
        if (yPos < 0):
            yPos = 0
            yPosB = 1 
        if (matrixGrid[xPos] & row[yPos] != row[yPos]):
            matrixGrid[xPos] = matrixGrid[xPos] + yPosB
            bus.write_i2c_block_data(matrix,0, matrixGrid)
            bus.write_byte_data(matrix, 0xFF, 0)
    if direction == "left":
        time.sleep(0.1)#sleeps to give time for the player to lift off the key
        sideEncPos = sideEnc.position
        xPos = xPos - 2
        if (xPos < 0):
            xPos = 0
        if (matrixGrid[xPos] & row[yPos] != row[yPos]):
            matrixGrid[xPos] = matrixGrid[xPos] + yPosB
            bus.write_i2c_block_data(matrix,0, matrixGrid)
            bus.write_byte_data(matrix, 0xFF, 0)
    if direction == "right":
        time.sleep(0.1)# sleeps to give time for the player to lift off the key
        sideEncPos = sideEnc.position
        xPos = xPos + 2
        if (xPos >= width * 2):
            xPos = (width * 2)
        if (matrixGrid[xPos] & row[yPos] != row[yPos]):
            matrixGrid[xPos] = matrixGrid[xPos] + yPosB
            bus.write_i2c_block_data(matrix,0, matrixGrid)
            bus.write_byte_data(matrix, 0xFF, 0)
            
            
    
    if direction == "clear":
        time.sleep(0.1)#gives time for the player to lift off the key
        matrixGrid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        bus.write_i2c_block_data(matrix,0, matrixGrid)
        bus.write_byte_data(matrix, 0xFF, 0)
    return render_template('index.html')
            
if __name__ == '__main__':
    app.run(debug=True, port=8081, host='0.0.0.0')