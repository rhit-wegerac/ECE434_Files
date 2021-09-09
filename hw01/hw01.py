###############################################################################################
# Author: Andrew Weger                                                                        #
# Date last modified: 9/9/2021                                                                #
# Description: This is the Etch-a-sketch program from hw01 in ECE434                          #
# I Andrew Weger pledge that the code below is 100% of my doing, and has not been plagiarized.#
###############################################################################################

#!/usr/bin/env python

import numpy as np
import os
import time
import sys 
from curtsies import Input

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
        print("(Controls):    Up Arrow: Moves the pen up.    Down Arrow: Moves the pen down. ")
        print("Left Arrow: Moves the pen to the left.    Right Arrow: Moves the pen to the right.")
        print("                           Spacebar: Clears the board.")
    return g #returns the grid back to the while loop so that it can be updated.
            
def clear():#clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')

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
    with Input(keynames='curses')as input_generator:#detects if there was a key pressed 
        for e in input_generator:
            if str(e) == 'KEY_UP': #checks if the up arrow was pressed
                time.sleep(0.1)#sleeps to give time for the player to lift off the key
                yPos -= 1 #moves the position of the pen in the y direction
                if(yPos < 0): #if the pen goes outside of the boundary, keep it at 0
                    yPos = 0
                clear()#clears the screen
                grid = update(grid, widthInt, heightInt, xPos, yPos)#updates the screen with the new grid
            if str(e) == "KEY_DOWN":#checks if the down arrow was pressed
                time.sleep(0.1)#sleeps to give time for the player to lift off the key
                yPos += 1#moves the position of the pen in the y direction
                if(yPos == heightInt):#if the pen goes outside the boundary, keep it at the edge fo the grid
                    yPos = heightInt - 1
                clear()#clear the screen
                grid = update(grid, widthInt, heightInt, xPos, yPos)#update the screen
            if str(e) == "KEY_LEFT":#checks if the left arrow was pressed
                time.sleep(0.1)#sleeps to give time for the player to lift off the key
                xPos -= 1#moves the pen in the x direction
                if(xPos < 0):#if the pen goes ouside the boundary, keep it at 0
                    xPos = 0
                clear()#clear the screen
                grid = update(grid, widthInt, heightInt, xPos, yPos)#update the screen
            if str(e) == "KEY_RIGHT":#checks if the right arrow was pressed
                time.sleep(0.1)# sleeps to give time for the player to lift off the key
                xPos += 1 #moves the pen in the x direction
                if(xPos == widthInt):#if the pen is outside the boundary, keep it at the edge of the grid
                    xPos = widthInt - 1
                clear()#clear the screen
                grid = update(grid, widthInt, heightInt, xPos, yPos)#update the screen
            if str(e) == ' ':#check if the spacebar was pressed
                time.sleep(0.1)#gives time for the player to lift off the key
                clear()#clears the screen
                grid[:] = "."#resets the grid to empty
                grid = update(grid, widthInt, heightInt, xPos, yPos)#update the screen
            