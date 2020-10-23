#!/usr/bin/env python3
#This is to test how fast the LED can toggle using mmap.
from mmap import mmap
import time, struct 


GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_DATAIN = 0x138
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
pin1 = 1<<16
pin2 = 1<<13


with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
  
packed_reg = mem[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]

# reg_status &= ~(USR3)
reg_status &= ~(pin1)
reg_status &= ~(pin2)

mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)


while(True):
    mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", pin1)
    mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", pin1)
    
    # time.sleep(0.5)