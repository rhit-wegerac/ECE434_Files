**ReadMe for hw06**

**Project Page**
My project page on eLinux is at the address: https://elinux.org/ECE434_Project-_LED_Matrix_Information_Board

**Video**

1. National Instruments
2. Real time kernel patch
3. Running real time and non real time tasks at the same time.
4. They can take a long time to finish.
5. Time it takes an event to occur until the time the task actually executes.
6. A Cyclictest takes a timestamp of when a task is executed and another timestamp of when the task actually executes after a known sleep duration.
7. A histogram of the latency of an RT and non-RT event.
8. Dispatch Latency and Scheduling Latency
   1. Dispatch Latency: amount of time it takes the hardware to fire the interrupt and the thread to be woken up.
   2. Scheduling Latency: Amount of time from the moment the scheduler knows to schedule the task to when the CPU is given that task
9. Running with interrupts disabled.
10. The non-critical IRQ
11. The RT patch had been enabled

**PREEMPT_RT**
I could not complete this part of the homework, I ended up bricking my Beagle twice which caused me to start over and setup the Beagle from scratch with a fresh SD card installation.

# hw06 grading

| Points      | Description |
| ----------- | ----------- |
|  2/2 | Project 
|  5/5 | Questions
|  0/4 | PREEMPT_RT
|  0/2 | Plots to 500 us
|  0/5 | Plots - Heavy/Light load
|  0/2 | Extras
| 7/20 | **Total**

*My comments are in italics. --may*

