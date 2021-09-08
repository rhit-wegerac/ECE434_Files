#!/usr/bin/env python

import numpy as np
import os
import keyboard as key
import time

def update(grid, gridWidth, gridHeight, xPos, yPos):
    w = gridWidth
    h = gridHeight
    g = grid
    x = xPos
    y = yPos
    g[xPos][yPos] = "x"
    print("   ", end = " ")
    for i in range(w - 1):
        print(str(i) + " ", end = " ")
    print(str(w-1))
    for j in range(h):
        print(str(j) + ": ", end = " ")
        for k in range(w - 1):
            print(str(g[k][j]) + " ", end = " ")
        print(str(g[w - 1][j]))
    return g
            

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Please enter the size of the grid.")
width = input("Width = ")
height = input("Height = ")
widthInt = int(width)
heightInt = int(height)
print("The size of the grid will be " + width + "x" + height + ".")
print("Now select a starting point on the grid, which uses 0 indexing!")
xPos = int(input("X = "))
if(xPos >= widthInt):
    print("X Position is too large, remember it has to be smaller than " + width + "!")
    print("X Position will default to 0.")
    xPos = 0
yPos = int(input("Y = "))
if(yPos >= heightInt):
    print("Y Position is too large, remember it has to be smaller than " + height + "!")
    print("Y Position will default to 0.")
    yPos = 0
grid = np.chararray((widthInt,heightInt), unicode = True)
grid[:] = "."
grid[xPos][yPos] = "x"
""" grid[1][0] = "x"
grid[2][0] = "x"
grid[1][1] = "x"
grid[2][2] = "x" """
print("Now constructing the grid...")
time.sleep(2)
clear()
update(grid,widthInt,heightInt,xPos,yPos)
while(1):
    if key.is_pressed('up'):
        time.sleep(0.1)
        yPos -= 1
        if(yPos < 0):
            yPos = 0
        clear()
        grid = update(grid, widthInt, heightInt, xPos, yPos)
    if key.is_pressed('down'):
        time.sleep(0.1)
        yPos += 1
        if(yPos == heightInt):
            yPos = heightInt - 1
        clear()
        grid = update(grid, widthInt, heightInt, xPos, yPos)
    if key.is_pressed('left'):
        time.sleep(0.1)
        xPos -= 1
        if(xPos < 0):
            xPos = 0
        clear()
        grid = update(grid, widthInt, heightInt, xPos, yPos)
    if key.is_pressed('right'):
        time.sleep(0.1)
        xPos += 1
        if(xPos == widthInt):
            xPos = widthInt - 1
        clear()
        grid = update(grid, widthInt, heightInt, xPos, yPos)
    if key.is_pressed('space'):
        time.sleep(0.1)
        clear()
        grid[:] = "."
        grid = update(grid, widthInt, heightInt, xPos, yPos)