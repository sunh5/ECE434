#!/bin/bash
#This is a python file to real temperatures for the two sensors. 
while [ "1" = "1" ]; do   
#Read the temperatures from two addresses
    tmp1=`i2cget -y 2 0x48`
    tmp2=`i2cget -y 2 0x4a`
#Convert the number to fahrenhite 
    tmp1F=$(($tmp1*9))
    tmp2F=$(($tmp2*9))
    tmp1F=$(($tmp1F / 5))
    tmp2F=$(($tmp2F / 5))
    tmp1F=$(($tmp1F + 32))
    tmp2F=$(($tmp2F + 32))
#Show the numbers and unit
    echo tmpSensor 1 is $tmp1F F
    echo tmpSensor 2 is $tmp2F F
    
    sleep 1
done
    
    
    
    
    
    