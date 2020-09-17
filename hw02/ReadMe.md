#This file contains answers for part 2,3&4 for homework 2. 

# Buttons and LEDs
See code in Question1.py.

# Measuring a gpio pin on an Oscilloscope
See code in togglegpio.sh
Using shell file
1. What's the min and max voltage?
    3.36V, -120mV
2. What period is it?
    245ms
3. How close is it to 100ms?
    245/2 = 122.5ms, it's 22.5ms longer than the 100ms
4. Why do they differ?
    Because there are other code running on the board. THe chip need some time to execute the code, and transmit to the certain GPIO pin. 
5. Run htop and see how much processor you are using.
    22.2% for togglegpio
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? 
   Make a table of the values you try and the corresponding period and processor usage. 
   Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables
   
    shortest period is 22ms
    |Period   |CPU used   |
    |---------|-----------|
    |0.05     |34.2%      |
    |0.04     |39.6%      |
    |0.03     |45.0%      |
    |0.02     |56.2%      |
    |0.01     |72.1%      |
    |0.001    |95.8%      |
    |0.0001   |100%       |
    
7. How stable is the period?
    The period is pretty stable, it can always stay in the same period. 
8. Try launching something like vi. How stable is the period?
    The period is still stable as before. 
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
    Yes, the period closer to the correct period, which means the period is shorter. For my trail, it changed from 122 to 111ms. 
10. togglegpio uses bash (first line in file). Try using sh. Is the period shorter?
    Yes, the period became shorter, from 10ms to 8 ms. 
11. What's the shortest period you can get? 
    The shortest period I can get is 8.0ms.
    
    
Using Python:
See code in toggle.py
1. What's the min and max voltage?
    3.36V, -120mV
2. What period is it?
    101.2ms
3. How close is it to 100ms?
    It's 1.2ms longer than the 100ms
4. Why do they differ?
    Because there are other code running on the board. THe chip need some time to execute the code, and transmit to the certain GPIO pin. 
5. Run htop and see how much processor you are using.
    3.9% for togglegpio
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? 
   Make a table of the values you try and the corresponding period and processor usage. 
   Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables
   
    shortest period is 0.23ms
    
    |Period   |CPU used for sh|CPU used for python|
    |---------|---------------|-------------------|
    |0.05     |34.2%          |4.0%               |
    |0.04     |39.6%          |5.3%               |
    |0.03     |45.0%          |5.8%               |
    |0.02     |56.2%          |6.8%               |
    |0.01     |72.1%          |6.8%               |
    |0.001    |95.8%          |45.5%              |
    |0.0001   |100%           |68.2%              |
    
7. How stable is the period?
    The perod is stable until it below 10ms
8. Try launching something like vi. How stable is the period?
    The period is more unstable after vi launched.  
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?
    Yes, the period closer to the correct period, which means the period is shorter. For my trail, it changed from 0.23ms to 0.214ms. 
10. togglegpio uses bash (first line in file). Try using sh. Is the period shorter?
     
11. What's the shortest period you can get? 
    The shortest period I can get is 0.214ms.
    
    
    
    
Using C:
See code in togglegpio.c
1. What's the min and max voltage?
    3.36V, -120mV
2. What period is it?
    100.0ms
3. How close is it to 100ms?
    It's totally equal to 100ms.
4. Why do they differ?
    Because there are other code running on the board. THe chip need some time to execute the code, and transmit to the certain GPIO pin. 
5. Run htop and see how much processor you are using.
    2.2% for togglegpio
6. Try different values for the sleep time (2nd argument). What's the shortest period you can get? 
   Make a table of the values you try and the corresponding period and processor usage. 
   Try using markdown tables: https://www.markdownguide.org/extended-syntax/#tables
   
    shortest period is 0.1ms
    
    | Period   | CPU used for sh| CPU used for python| CPU used for C|
    | ------- | ------------- | ----------------- | ------------ |
    | 0.05     | 34.2%          | 4.0%               | 2.6%          |
    | 0.04     | 39.6%          | 5.3%               | 3.9%          |
    | 0.03     | 45.0%          | 5.8%               | 3.3%          |
    | 0.02     | 56.2%          | 6.8%               | 3.3%          |
    | 0.01     | 72.1%          | 6.8%               | 3.4%          |
    | 0.001    | 95.8%          | 45.5%              | 4.2%          |
    | 0.0001   | 100%           | 68.2%              | 22.5%         |
    
7. How stable is the period?
    The perod is stable until it about below 10ms
8. Try launching something like vi. How stable is the period?
    The period is more unstable after vi launched.  
9. Try cleaning up togglegpio.sh and removing unneeded lines. Does it impact the period?

10. togglegpio uses bash (first line in file). Try using sh. Is the period shorter?
     
11. What's the shortest period you can get? 
    The shortest period I can get is 94.7us.
    
  How much faster is it? Add your results to the table
    The fastest toggle I can get is 94.7us.


# GPIOD
 python 1bit :9.31us   2bits: 9.91us
 C      1bit :2.27us   2bits: 2.428us 

The table for the all shortest periods 

|Comparasion of fastest toggles |
|Languages|Period|
|---------|------|
|Shell | 8ms |
|python | 0.214 ms  |
|C     | 0.0947 ms  |
|Gpiod python 1bit| 0.00931 ms  |
|Gpiod python 2bits| 0.00991 ms  |
|Gpiod C 1bit| 0.00227 ms  |
|Gpiod C 2bits| 0.002428 ms  |

# Secrity
  I successfully changed the port to 1911 and changed it back. 
  I also successfully use iptable to block unavaible ips. 
  I configured how to reject ssh connection for few fail attempts.
  
# Etch-a-sketch
  See code etchWithGPIO.py