# **Andrew Weger hw02 ReadMe**

The code in this folder has been wired with the following configuration.

|Number in Code|Button|LED|
|---|---|---|
|Button/LED 1|P9_11|P9_12|
|Button/LED 2|P9_13|P9_14|
|Button/LED 3|P9_15|P9_16|
|Button/LED 4|P9_17|P9_18|

## Buttons&LEDs.py
This is the program that uses 4 switches to light up 4 different LEDs.

## pytoggle.py
This is the program that was used to toggle the GPIO pin in python as fast as possible.

## etchwithbuttons.py
This is the program that has the Etch-a-Sketch program from hw01, but has been modified to use hardwired buttons. In the program these buttons do the following actions: 

|Button|Action|
|---|---|
|1|Moves pen up, and lights up LED1|
|2|Moves pen down, and lights up LED2|
|3|Moves pen left, and lights up LED3|
|4|Moves pen right, and lights up LED4|
|1&2|Flashes all 4 LEDS, 3 times. Clears the board.|

### How to Run
To run any of these programs, the user only needs to type `./filename.py` with "filename" being replaced with the name of the file you wish to run. If an error occurs at runtime, run the following command: `chmod +x filename.py` with "filename" being replaced with the name of the file you're wanting to run.  





# hw02 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Buttons and LEDs 
|  7/7 | Etch-a-Sketch works
|      | Measuring a gpio pin on an Oscilloscope 
|  2/2 | Questions answered
|  4/4 | Table complete
|  2/2 | gpiod
|      | Security
|  1/1 | ssh port
|  1/1 | iptables 
|  1/1 | fail2ban
| 20/20   | **Total**

Video looks OK (a bit small)

Security is missing -3
