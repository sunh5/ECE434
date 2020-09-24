#!/usr/bin/env python3
#This is a python file to real temperatures for the two sensors. 
import time
import smbus

bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x4a
#Keep reading the temperatures and pint them out
while 1:
    tmp1 = bus.read_byte_data(address1, 0)
    tmp2 = bus.read_byte_data(address2, 0)
    print(tmp1, ' ', tmp2, end="\r")
    time.sleep(0.1)