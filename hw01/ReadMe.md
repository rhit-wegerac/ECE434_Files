<u>**Andrew Weger's Etch-a-Sketch program**</u>

The program first asks for the size of the grid that you want to use, and then repeats back the grid size. Next, the program will prompt for a starting location on the grid. After that, the game creates the board and displays it in the terminal. The row and column numbers are shown in the terminal, and a spot that has not been "drawn" on will be a '.' (I used this instad of a blank space because the space threw off the alignment of the grid), and a "drawn space" will be an 'x'. The player uses the arrow keys on the keyboard to move the pen around the grid. When the player wants to erase the grid and start over, they can press the space bar, and the board will clear and leave a single 'x' where the pen is. 


 To run the program, run the install.sh script. Then, type ./hw01.py or "python hw01.py" into the terminal and the program should run. 

# hw01 grading

| Points      | Description | Comment
| ----------- | ----------- | -------
|  8 | Etch-a-Sketch works | 
|  2 | Code documented (including name) |
|  1 | Includes #!/usr/bin/env python3 and chmod +x | Wasn't first line in file
|  2 | install.sh included if needed | Should use pip3
|  2 | Used hw01 directory |
|  2 | ReadMe.md included |
|  2 | Name in gitLearn and gitLearnFork | 
| 19 | **Total**