#!/bin/bash
#THis is to read the temperature of the sensor through i2c. 
config-pin P9_19 i2c
config-pin P9_20 i2c

cd /sys/class/i2c-adapter/i2c-2
echo 0x48 > delete_device
echo tmp101 0x48 > new_device
cd 1-0048/hwmon/hwmon0
cat temp1_input
