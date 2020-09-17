#!/usr/bin/env python3
#in this program, when a button is pushed, the corresponding LED will be on
#
import Adafruit_BBIO.GPIO as GPIO
import time
#Set gpios to LED
Led1 = "P9_11"
Led2 = "P9_12"
Led3 = "P9_13"
Led4 = "P9_15"   
#Set gpios to push button
pushButton1 = "P8_7"
pushButton2 = "P8_8"
pushButton3 = "P8_9"
pushButton4 = "P8_10"       #connection to buttons


#Set input for pushbutton and output for LEDs
GPIO.setup(Led1, GPIO.OUT)
GPIO.setup(Led2, GPIO.OUT)
GPIO.setup(Led3, GPIO.OUT)
GPIO.setup(Led4, GPIO.OUT) 
GPIO.setup(pushButton1, GPIO.IN)
GPIO.setup(pushButton2, GPIO.IN)
GPIO.setup(pushButton3, GPIO.IN)
GPIO.setup(pushButton4, GPIO.IN)    
#Set flags to interrupt
interflag1 = 0;
interflag2 = 0;
interflag4 = 0;
interflag3 = 0;
# print("lalala")


def callback(a):
    global interflag1;
    global interflag2;
    global interflag3;
    global interflag4;
    
    if(a==pushButton1):
        if(interflag1 == 1):
            GPIO.output(Led1,GPIO.LOW), GPIO.output(Led2,GPIO.LOW), GPIO.output(Led3,GPIO.LOW), GPIO.output(Led4,GPIO.LOW)
            interflag1 = 0
        else:
            GPIO.output(Led1,GPIO.HIGH), GPIO.output(Led2,GPIO.LOW), GPIO.output(Led3,GPIO.LOW), GPIO.output(Led4,GPIO.LOW)
            interflag1 = 1
    if(a==pushButton2):
        if(interflag2 == 1):
            GPIO.output(Led1,GPIO.LOW), GPIO.output(Led2,GPIO.LOW), GPIO.output(Led3,GPIO.LOW), GPIO.output(Led4,GPIO.LOW)
            interflag2 = 0
        else:
            GPIO.output(Led2,GPIO.HIGH), GPIO.output(Led1,GPIO.LOW), GPIO.output(Led3,GPIO.LOW), GPIO.output(Led4,GPIO.LOW)
            interflag2 = 1
    if(a==pushButton3):
        if(interflag3 == 1):
            GPIO.output(Led1,GPIO.LOW), GPIO.output(Led2,GPIO.LOW), GPIO.output(Led3,GPIO.LOW), GPIO.output(Led4,GPIO.LOW)
            interflag3 = 0
        else:
            GPIO.output(Led3,GPIO.HIGH), GPIO.output(Led2,GPIO.LOW), GPIO.output(Led1,GPIO.LOW), GPIO.output(Led4,GPIO.LOW)
            interflag3 = 1
    if(a==pushButton4):
        if(interflag4 == 1):
            GPIO.output(Led1,GPIO.LOW), GPIO.output(Led2,GPIO.LOW), GPIO.output(Led3,GPIO.LOW), GPIO.output(Led4,GPIO.LOW)
            interflag4= 0
        else:
            GPIO.output(Led4,GPIO.HIGH), GPIO.output(Led2,GPIO.LOW), GPIO.output(Led3,GPIO.LOW), GPIO.output(Led1,GPIO.LOW)
            interflag4= 1
    

#GPIO.remove_event_detect(BT1)
GPIO.add_event_detect(pushButton1, GPIO.BOTH, callback=callback) 
GPIO.add_event_detect(pushButton2, GPIO.BOTH, callback=callback) 
GPIO.add_event_detect(pushButton3, GPIO.BOTH, callback=callback) 
GPIO.add_event_detect(pushButton4, GPIO.BOTH, callback=callback) 

 
while True:
    time.sleep(100)
GPIO.cleanup()