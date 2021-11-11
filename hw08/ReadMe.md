**ReadMe for hw08**

Still Working on hw08

<u>Questions</u>

**<u>2.6 Blinking an LED</u>**

- Starting the PRU code `sudo make TARGET=hello.pru0`
- Stopping PRU code ``sudo make TARGET=hello.pru0 stop` 
- Pin P9_31 is toggling at 12.5MHz
- There is a bit of jitter.
- The pin seems to be stable, the voltage seems to be the same at every toggle.

**<u>5.3 PWM Generator</u>**

![scope1](https://github.com/rhit-wegerac/ECE434_Files/blob/main/hw08/scope1.jpg?raw=true)

*Figure 1: Scope Output for `pwm1.pru0.c`*

- The wave seems to be fairly stable, even though the waveform looks more like a sine wave than a square wave.
- The standard deviation is 2.627V
- When I ran the code at a slower speed, there was jitter, but since this is running at 50MHz, there is not really enough time for jitter, and we don't see any.

**<u>5.4 Controlling the PWM Frequency</u>**

