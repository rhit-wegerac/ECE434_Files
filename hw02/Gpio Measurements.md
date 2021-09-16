
|./togglegpio.sh 60 0.1|            |  
|----------------------|------------|   
|Vmin| -190 mV |                        
|Vmax| 3.44 V |                         
|Period| 240 ms|                       
|Frequency| 4.15 Hz|                    
|How close to 100 ms| Not very close.|  
| htop| 3.2% CPU|                     


|./togglegpio.sh 60 0.001 | | 
|-----------------------|------|
 |Vmin| -190 mV|
 |Vmax| 3.44 V|
 |Period| 45 ms|
 |Frequency| 22.2 Hz|
 |How close to 100ms| Closer than before, it's now less than 100 ms |
 |htop| 22.6 % CPU|
Period is not very stable
After launching vi it seems that the period is much more stable
Cleaning up togglegpio.sh the period is down to 41 ms
When using sh, the period actually seems to be slower at 43ms.
The shortest period I could manage was 41 ms.
