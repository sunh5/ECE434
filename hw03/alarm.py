#!/usr/bin/env python3
#This file is to use interrupt detect the limit temperatures. As long as the temperature exceeds the limit value
#The callback will be triggered to warn. 
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time 

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4a
alert1 = "P8_15"
alert2 = "P8_16"

GPIO.setup(alert1, GPIO.IN)
GPIO.setup(alert2, GPIO.IN)
#Check the limit temperatures
tmpH = bus.read_byte_data(address1,3) 
tmpL = bus.read_byte_data(address1,2)
tmpConfig = bus.read_byte_data(address1,1)
print(tmpH, " lala234 ",  tmpL, "   ", tmpConfig)
print()
#Define the calback function
def callBack1(a):
    tmp1 = bus.read_byte_data(address1,0)
    tmp2 = bus.read_byte_data(address2,0)
    # tmp1 = tmp1*9/5+32
    # tmp2 = tmp2*9/5+32
    print(tmp1, " Warnning: Too High or Too Low ", tmp2)

GPIO.add_event_detect(alert1, GPIO.FALLING, callback = callBack1)
GPIO.add_event_detect(alert2, GPIO.FALLING, callback = callBack1)
while 1:
    t1 = bus.read_byte_data(address1,0)
    t2 = bus.read_byte_data(address2,0)
    print(str(t1)+ " " + str(t2))
    time.sleep(5)
GPIO.cleanup
