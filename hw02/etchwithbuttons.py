#!/usr/bin/env python3
###############################################################################################
# Author: Andrew Weger                                                                        #
# Date last modified: 9/16/2021                                                                #
# Description: This is the Etch-a-sketch program from hw01 in ECE434                          #
# I Andrew Weger pledge that the code below is 100% of my doing, and has not been plagiarized.#
###############################################################################################


import numpy as np
import os
import time
import sys 
from curtsies import Input
import gpiod

chip0 = gpiod.Chip('gpiochip0')
chip1 = gpiod.Chip('gpiochip1')
CONSUMER='getset'
#defines which pins the LEDs use
rled = chip1.get_lines([28])#LED1
gled = chip1.get_lines([18])#LED2
bled = chip1.get_lines([19])#LED3
yled = chip0.get_lines([4])#LED4
#sets the LEDs as outputs
rled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
gled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
bled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)
yled.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_OUT)

#defines which pins the switches are
rbut = chip0.get_lines([30])#button1
gbut = chip0.get_lines([31])#button2
bbut = chip1.get_lines([16])#button3
ybut = chip0.get_lines([5])#button
#sets the switches as inputs
rbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
gbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
bbut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)
ybut.request(consumer=CONSUMER, type = gpiod.LINE_REQ_DIR_IN)

def update(grid, gridWidth, gridHeight, xPos, yPos):
    #The following lines take the inputs to the funtion and assigns them to a different variable
    w = gridWidth
    h = gridHeight
    g = grid
    x = xPos
    y = yPos
    g[xPos][yPos] = "x" #Marks the new position of the pen with a 'x'
    print("   ", end = " ")#Prints the spaces needed in the corner of the grid
    for i in range(w - 1): #This loop and the following line prints the top grid markers
        print(str(i) + " ", end = " ")#prints the number of the column and a space
    print(str(w-1))#prints the final column so that the next row doens't print on the same line.
    for j in range(h):#This loop prints the rest of the grid
        print(str(j) + ": ", end = " ")#Prints the number at the left of the grid
        for k in range(w - 1):#for loop for the individual columns
            print(str(g[k][j]) + " ", end = " ")#prints the 'x' and '.' in the grid
        print(str(g[w - 1][j])) # prints the last grid element so the next line doesn't continue to print on the same line
    print(" ")
    print(" ")
    print("(Controls):    Button1: Moves the pen up.    Button2: Moves the pen down. ")
    print("Button3: Moves the pen to the left.    Button4: Moves the pen to the right.")
    print("                      Buttons 1 & 2: Clears the board.")
    return g #returns the grid back to the while loop so that it can be updated.
            
def clear():#clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
def buttonReset(grid):
    grid2 = grid
    #flashes all 4 lights 3 times
    rled.set_values([1])
    gled.set_values([1])
    bled.set_values([1])
    yled.set_values([1])
    time.sleep(0.25)
    rled.set_values([0])
    gled.set_values([0])
    bled.set_values([0])
    yled.set_values([0])
    time.sleep(0.25)
    rled.set_values([1])
    gled.set_values([1])
    bled.set_values([1])
    yled.set_values([1])
    time.sleep(0.25)
    rled.set_values([0])
    gled.set_values([0])
    bled.set_values([0])
    yled.set_values([0])
    time.sleep(0.25)
    rled.set_values([1])
    gled.set_values([1])
    bled.set_values([1])
    yled.set_values([1])
    time.sleep(0.25)
    rled.set_values([0])
    gled.set_values([0])
    bled.set_values([0])
    yled.set_values([0])
    clear()#clears the screen
    grid2[:] = "."#resets the grid to empty
    grid2 = update(grid2, widthInt, heightInt, xPos, yPos)# update the screen
    return grid2
    

print("Please enter the size of the grid. (Press Enter after entering the size)")
width = input("Width = ")#prompts for the grid width
height = input("Height = ")#prompts fo the grid height
widthInt = int(width)#changes the width to an integer that can be used.
heightInt = int(height)#changes the height to an integer that can be used.
print("The size of the grid will be " + width + "x" + height + ".")
print("Now select a starting point on the grid, which uses 0 indexing! (Press Enter after entering the location)")
xPos = int(input("X = "))#prompts for the x coordinate of the pen
if(xPos >= widthInt):#checks to see if the x position is too large and resets it to 0 if true.
    print("X Position is too large, remember it has to be smaller than " + width + "!")
    print("X Position will default to 0.")
    xPos = 0
yPos = int(input("Y = "))#prompts for the y position of the pen
if(yPos >= heightInt):#checks to see if the y position is too large and resets it to 0 if true.
    print("Y Position is too large, remember it has to be smaller than " + height + "!")
    print("Y Position will default to 0.")
    yPos = 0
grid = np.chararray((widthInt,heightInt), unicode = True)#sets up a grid array of the size indicated to keep the contents of the grid.
grid[:] = "."#fills the grid with '.' to start
grid[xPos][yPos] = "x"#marks the position of the pen in the grid+
print("Now constructing the grid...")
time.sleep(2)#pauses to let the player read the screen.
clear()#clears the screen
update(grid,widthInt,heightInt,xPos,yPos)#updates the screeen with the starting board

while(1):#game loop
    #gets the values of the switches
    rval = rbut.get_values()#button1
    gval = gbut.get_values()#button2
    bval = bbut.get_values()#button3
    yval = ybut.get_values()#button4
    
    if rval == [0]:#if button1 is pressed, do this
        time.sleep(0.25)
        if gval == [0]: #if button2 is also pressed, do this
            grid = buttonReset(grid)
        else:
            rled.set_values([1])#turn on LED1
            time.sleep(0.1)#sleeps to give time for the player to lift off the key
            rled.set_values([0])
            yPos -= 1 #moves the position of the pen in the y direction
            if(yPos < 0): #if the pen goes outside of the boundary, keep it at 0
                yPos = 0
            clear()#clears the screen
            grid = update(grid, widthInt, heightInt, xPos, yPos)#updates the screen with the new grid
    if gval == [0]:#if button2 is pressed, do this
        time.sleep(0.25)
        if rval == [0]:#if button1 is also pressed, do this
            grid = buttonReset(grid)
        else:
            gled.set_values([1])#turn on LED2
            time.sleep(0.1)#sleeps to give time for the player to lift off the key
            gled.set_values([0])#turn off LED2
            yPos += 1#moves the position of the pen in the y direction
            if(yPos == heightInt):#if the pen goes outside the boundary, keep it at the edge fo the grid
                yPos = heightInt - 1
            clear()#clear the screen
            grid = update(grid, widthInt, heightInt, xPos, yPos)#update the screen
    if bval == [0]:#if button3 is pressed, do this
        bled.set_values([1])#turn on LED3
        time.sleep(0.35)#sleeps to give time for the player to lift off the key
        bled.set_values([0])#turn off LED3
        xPos -= 1#moves the pen in the x direction
        if(xPos < 0):#if the pen goes ouside the boundary, keep it at 0
            xPos = 0
        clear()#clear the screen
        grid = update(grid, widthInt, heightInt, xPos, yPos)#update the screen
    if yval == [0]:#if button4 is pressed, do this
        yled.set_values([1])#turn on LED4
        time.sleep(0.35)# sleeps to give time for the player to lift off the key
        yled.set_values([0])#turn off LED 4
        xPos += 1 #moves the pen in the x direction
        if(xPos == widthInt):#if the pen is outside the boundary, keep it at the edge of the grid
            xPos = widthInt - 1
        clear()#clear the screen
        grid = update(grid, widthInt, heightInt, xPos, yPos)#update the screen
    
        