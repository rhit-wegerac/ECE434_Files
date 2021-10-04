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
app = Flask(__name__)








@app.route('/')
def index():
        
        templateData = {
              'title' : 'Etch-a-Sketch',
              'xPos' : xPos
        }
        return render_template('index.html',**templateData)
        
@app.route("/<direction>/")
def action(direction):
    global xPos, yPos, yPosB, matrixGrid, height, width
    if direction == "up": #checks if the up arrow was pressed
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
        xPos = xPos - 2
        if (xPos < 0):
            xPos = 0
        if (matrixGrid[xPos] & row[yPos] != row[yPos]):
            matrixGrid[xPos] = matrixGrid[xPos] + yPosB
            bus.write_i2c_block_data(matrix,0, matrixGrid)
            bus.write_byte_data(matrix, 0xFF, 0)
            
    if direction == "right":
        xPos = xPos + 2
        if (xPos >= width * 2):
            xPos = (width * 2)
        if (matrixGrid[xPos] & row[yPos] != row[yPos]):
            matrixGrid[xPos] = matrixGrid[xPos] + yPosB
            bus.write_i2c_block_data(matrix,0, matrixGrid)
            bus.write_byte_data(matrix, 0xFF, 0)
    
    if direction == "clear":
        matrixGrid = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        bus.write_i2c_block_data(matrix,0, matrixGrid)
        bus.write_byte_data(matrix, 0xFF, 0)
        
    templateData = {
              'title' : 'Etch-a-Sketch',
              'xPos' : xPos
        }
    return render_template('index.html', **templateData)
    
   
if __name__ == '__main__':
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
    bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
    bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
    bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)
    bus.write_i2c_block_data(matrix,0, matrixGrid)
    
    bus.write_byte_data(matrix, 0xFF, 0)
    app.run(debug=True, port=8081, host='0.0.0.0')