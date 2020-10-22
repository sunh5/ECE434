#!/usr/bin/env python3
#   Written by Haoxuan Sun 10/21/2020
#   Homework 07
#   This code is to implement the function of Etch-a-sketch with blynk
import numpy
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import time
import pdb; 
import blynklib
import os, sys

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH', default="")
if(BLYNK_AUTH == ""):
    print("BLYNK_AUTH is not set")
    sys.exit()

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70
delay = 1; # Delay between images in s
#Define the pattern of the matrix
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)
r1 = 0; r2 = 0; r3 = 0; r4 = 0; r5 = 0; r6 = 0; r7 = 0; r8 = 0
g1 = 0; g2 = 0; g3 = 0; g4 = 0; g5 = 0; g6 = 0; g7 = 0; g8 = 0
pattern = [g1, r1, g2, r2, g3, r3, g4, r4,
           g5, r5, g6, r6, g7, r7, g8, r8
]
reverse = [128,64,32,16,8,4,2,1]    #Used to define the position of light spot

#Set gpios to push button
pushButton1 = "P8_7"
pushButton2 = "P8_8"
pushButton3 = "P8_9"
pushButton4 = "P8_10"
pushButton5 = "P8_11"

#Parameters used to etch-a-sketch
width  = 8
length = 8
curX = 1
curY = 1
clearFlag = 0
quitFLag = 0
global value 


foo = " "
redLabel = [[foo for i in range(width)] for j in range(length)]

#Define the input for all gpio pins
GPIO.setup(pushButton1, GPIO.IN)
GPIO.setup(pushButton2, GPIO.IN)
GPIO.setup(pushButton3, GPIO.IN)
GPIO.setup(pushButton4, GPIO.IN)   
GPIO.setup(pushButton5, GPIO.IN) 


foo = " "
grid = [[foo for i in range(width+1)] for j in range(length+1)]
for i in range (width+1):
    for j in range (length+1):
        grid[i][j] = " "
        if (i == 0) & (j > 0):
            grid[i][j] =str(j-1)
            # print(grid[i][j])
        if (j == 0) & (i > 0):
            grid[i][j] = str(i-1)+":"
        
            
#Print out the grid
def printGrid():
    for i in range (width+1):
        result = ""
        if i == 0:
            result += " "
        for j in range(length+1):
            result = result + grid[i][j] + "  "
        print(result)

grid[curX][curY] = "+"
grid2 = grid
printGrid()
pattern[0] = 128
bus.write_i2c_block_data(matrix, 0, pattern)

reverseRed = [0,0,0,0,0,0,0,0]
print("Instruction: w to move up; s to move down; a to move left; d to move right; c to clear")
#Draw the grid according to button pressed
def drawGrid():
    # value = callback1(a) #input("Direction=\n")
    global curX; global curY; global clearFlag; global quitFlag
    global grid2; global value
    global pattern; global reverse; 
    global clearGreen
    global clearRed
    global reverseRed
    global redLabel
    if value == "w":
        grid[curX][curY] = "*"
        if redLabel[curX-1][curY-1] != 1:           #Check is the position been occupied
            reverseRed[curY-1] += reverse[curX-1]   #convert position to position on matrix
        if (reverseRed[curY-1] > 255): reverseRed[curY-1] = 255
        pattern[curY*2-1] = reverseRed[curY-1]
        redLabel[curX-1][curY-1] = 1
        
        if clearFlag == 1:
            grid[curX][curY] = " "
            clearFlag = 0
        if curX == 1:
            curX = width
        else:
            curX -= 1
        clearGreen()
        pattern[curY*2-2] = reverse[curX-1]
        
    elif value == "s":
        grid[curX][curY] = "*"
        if redLabel[curX-1][curY-1] != 1:
            reverseRed[curY-1] += reverse[curX-1]
        if (reverseRed[curY-1] > 255): reverseRed[curY-1] = 255
        pattern[curY*2-1] = reverseRed[curY-1]
        redLabel[curX-1][curY-1] = 1
        if clearFlag == 1:
            grid[curX][curY] = " "
            clearFlag = 0
        if curX == width:
            curX = 1
        else:
            curX += 1
        clearGreen()
        pattern[curY*2-2] = reverse[curX-1]
    elif value == "a":
        grid[curX][curY] = "*"
        if redLabel[curX-1][curY-1] != 1:
            reverseRed[curY-1] += reverse[curX-1]
        if (reverseRed[curY-1] > 255): reverseRed[curY-1] = 255
        print(reverseRed)
        pattern[curY*2-1] = reverseRed[curY-1]
        redLabel[curX-1][curY-1] = 1
        # temp = curX; tempReverse[curY-1] = reverseRed[curY-1]
        if clearFlag == 1:
            grid[curX][curY] = " "
            clearFlag = 0
        if curY == 1:
            curY = length
        else:
            curY -= 1
        clearGreen()
        pattern[curY*2-2] = reverse[curX-1]
        
    elif value == "d":
        grid[curX][curY] = "*"
        if redLabel[curX-1][curY-1] != 1:
            reverseRed[curY-1] += reverse[curX-1]
        if (reverseRed[curY-1] > 255): reverseRed[curY-1] = 255
        pattern[curY*2-1] = reverseRed[curY-1]
        redLabel[curX-1][curY-1] = 1
        if clearFlag == 1:
            grid[curX][curY] = " "
            clearFlag = 0
        if curY == length:
            curY = 1
        else:
            curY += 1
        clearGreen()
        pattern[curY*2-2] = reverse[curX-1]
    elif value == "p":
        for i in range (width+1):
            for j in range (length+1):
                grid[i][j] = " "
                if (i == 0) & (j > 0):
                    grid[i][j] =str(j-1)
                    # print(grid[i][j])
                if (j == 0) & (i > 0):
                    grid[i][j] = str(i-1)+":"
        clearGreen()
        clearRed()
        reverseRed = [0,0,0,0,0,0,0,0]
        fo = " "; redLabel = [[fo for i in range(width+1)] for j in range(length+1)]
        pattern[curY*2-2] = reverse[curX-1]
    elif value == "q":
        quitFlag = 1
    else:
        print("Say what? I might have heard")

    grid[curX][curY] = "+"
    if value == "c":
        clearFlag = 1
    bus.write_i2c_block_data(matrix, 0, pattern)
    printGrid()

#Define the callback function for each button pressed
def callback1(a):
    global value
    if(a==pushButton1):
        value = "w"
        drawGrid()
    if(a==pushButton2):
        value = "a"
        drawGrid()
    if(a==pushButton3):
        value = "s"
        drawGrid()
    if(a==pushButton4):
        value = "d"
        drawGrid()
    if(a==pushButton5):
        value = "p"
        drawGrid()
        
def clearGreen():
    global pattern
    for i in range (8):
        pattern[i * 2] = 0
def clearRed():
    global pattern
    for i in range (8):
        pattern[i * 2+1] = 0

#GPIO.remove_event_detect(BT1)
GPIO.add_event_detect(pushButton1, GPIO.RISING, callback=callback1) 
GPIO.add_event_detect(pushButton2, GPIO.RISING, callback=callback1) 
GPIO.add_event_detect(pushButton3, GPIO.RISING, callback=callback1) 
GPIO.add_event_detect(pushButton4, GPIO.RISING, callback=callback1) 
GPIO.add_event_detect(pushButton5, GPIO.RISING, callback=callback1) 

# bus.write_i2c_block_data(matrix, 0, pattern)

#Assign value according to which button pressed in blynk
@blynk.handle_event('write V*')
def my_write_handler(pin, valu):
    global value
    print('Current V{} value: {}'.format(pin, valu))
    if (pin == 0):
        print(value)
        value = "w"
        drawGrid()
    if (pin == 1):
        value = "a"
        drawGrid()
    if (pin == 2):
        value = "s"
        drawGrid()
    if (pin == 3):
        value = "d"
        drawGrid()
    if (pin == 4):
        value = "p"
        drawGrid()

while (1):
    blynk.run()
    global quitFlag
    # drawGrid()
 





