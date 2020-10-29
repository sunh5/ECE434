# Homework 8
-------
# PRU
Run ls /dev/remoteproc/ to setup pru cores. 
# 2.6Blinking an LED
The code is in folder BLink-LED. Set the pinmode and set the direction to out first. Then run the setup.sh. Use command 
"make TARGET=hello.pru0" to run the code. The scope measurement shows on picture "toggle-LED.png". 
The speed can reach 12.5MHz. 
I did not see jitter. 
The wave is stable.
# 5.3 PWM Generator
The code is in folder PWM generator. Set the pinmode and set the direction to out first. Then run the setup.sh. Use command 
"make TARGET=pwm1.pru0" to run the code. The scope measurement shows on picture "PWM-generator.png". 
The highest speed is 50MHz. Std Dev is 116.5kHz.
I dod not see jitter. 
The waveform is stable.
# 5.4 Controlling the PWM Frequency
The code is in folder PWM-freq. Set the pinmode and set the direction to out first. Then run the setup.sh. Use command 
"make TARGET=pwm4.pru0" to run the code. The scope measurement shows on picture "pwm_frequency.png". 
The pins used are P9-28, P9-29, P9-30, P9-31. 
Four bits are used 1<< 0, 1<< 1, 1<< 2, 1<< 3.
The highest frequency is 326.8kHz. 
There is no jitter. 
After I run the pwm-test.c, the off time became longer. Hence it worked. 

# Reading an Input at Regular Intervals
I used a function generator to generate a aquare wave with 3Vpp, and 1kHz. As I increase the frequency to about 1MHz, there is
a 56ns delay between input and output signal. Result shows on picture input-read.png
# Analog Wave Generator
Use the same pruout pin used before. I set the maximum time sample to 10000, them I can see the pattern of wave triangle, sine, and 
sawtooth. The results show in pictures SAWTOOTH.png, SINE.png, and TRIANGLE.png. 
# Speed comparsion
This table includes all the results. 
|Section |speed|
|------|------|
|2.6 Blinking an LED: |12.5MHz |
|5.3 PWM Generator: |50MHz |
|5.4 Controlling the PWM Frequenc: |326.8kHz |
