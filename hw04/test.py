#!/usr/bin/env python3
#This is to toggle LED with button using mmap
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
button1 = 1 << 12
button2 = 1 << 15

with open("/dev/mem", "r+b" ) as f:
  mem = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
  
packed_reg = mem[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]

# reg_status &= ~(USR3)
reg_status &= ~(pin1)
reg_status &= ~(pin2)

mem[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

# try:
while(True):
    button_packed = mem[GPIO_DATAIN:GPIO_DATAIN+4] 
    button_status = struct.unpack("<L", button_packed)[0] 
    
    if (button_status & button1 ) == button1:
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", pin1)
    else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", pin1)
    
    if (button_status & button2 ) == button2:
        mem[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", pin2)
    else:
        mem[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", pin2)
    
    
    # time.sleep(0.5)