#!/usr/bin/env python3
#Show the current temperature on the display
import blynklib
import blynktimer
import os, sys
import Adafruit_BBIO.GPIO as GPIO
import smbus
import time 

bus = smbus.SMBus(2)
address1 = 0x48
tmp = bus.read_byte_data(address1,0)

button = 'P9_11'
GPIO.setup(button, GPIO.IN)

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH', default="")
if(BLYNK_AUTH == ""):
    print("BLYNK_AUTH is not set")
    sys.exit()

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

#Read the temperature every one second and send it to display
def pushed():
    tmp = bus.read_byte_data(address1,0)
    print(tmp)
    # blynk.virtual_write(10, 255)
    blynk.virtual_write(5, tmp)  # Virtual LED: 255 max brightness
    time.sleep(1)
# GPIO.add_event_detect(button, GPIO.BOTH, callback=pushed) 

while (1):
    blynk.run()
    pushed()
    
GPIO.cleanup