#   Written by Haoxuan Sun 9/9/2020
#   Homework 01
#   This code is to implement the function of Etch-a-sketch
import numpy
import Adafruit_BBIO.GPIO as GPIO
import time
#Set gpios to push button
pushButton1 = "P8_7"
pushButton2 = "P8_8"
pushButton3 = "P8_9"
pushButton4 = "P8_10"
pushButton5 = "P8_11"

width  = 8
length = 8

curX = 1
curY = 1
clearFlag = 0
quitFLag = 0
global value 

foo = " "
grid = [[foo for i in range(width+1)] for j in range(length+1)]

GPIO.setup(pushButton1, GPIO.IN)
GPIO.setup(pushButton2, GPIO.IN)
GPIO.setup(pushButton3, GPIO.IN)
GPIO.setup(pushButton4, GPIO.IN)   
GPIO.setup(pushButton5, GPIO.IN) 
#Set flags to interrupt

interflag1 = 0;
interflag2 = 0;
interflag4 = 0;
interflag3 = 0;

for i in range (width+1):
    for j in range (length+1):
        grid[i][j] = " "
        if (i == 0) & (j > 0):
            grid[i][j] =str(j-1)
            # print(grid[i][j])
        if (j == 0) & (i > 0):
            grid[i][j] = str(i-1)+":"
        
            

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
print("Instruction: w to move up; s to move down; a to move left; d to move right; c to clear")
def drawGrid():
    # value = callback1(a) #input("Direction=\n")
    global curX
    global curY
    global clearFlag
    global quitFlag
    global grid2
    global value
    if value == "w":
        grid[curX][curY] = "*"
        if clearFlag == 1:
            grid[curX][curY] = " "
            clearFlag = 0
        if curX == 1:
            curX = width
        else:
            curX -= 1
    elif value == "s":
        grid[curX][curY] = "*"
        if clearFlag == 1:
            grid[curX][curY] = " "
            clearFlag = 0
        if curX == width:
            curX = 1
        else:
            curX += 1
    elif value == "a":
        grid[curX][curY] = "*"
        if clearFlag == 1:
            grid[curX][curY] = " "
            clearFlag = 0
        if curY == 1:
            curY = length
        else:
            curY -= 1
    elif value == "d":
        grid[curX][curY] = "*"
        if clearFlag == 1:
            grid[curX][curY] = " "
            clearFlag = 0
        if curY == length:
            curY = 1
        else:
            curY += 1
    elif value == "p":
        for i in range (width+1):
            for j in range (length+1):
                grid[i][j] = " "
                if (i == 0) & (j > 0):
                    grid[i][j] =str(j-1)
                    # print(grid[i][j])
                if (j == 0) & (i > 0):
                    grid[i][j] = str(i-1)+":"
    elif value == "q":
        quitFlag = 1
    else:
        print("Say what? I might have heard")

    grid[curX][curY] = "+"
    if value == "c":
        clearFlag = 1
    printGrid()

def callback1(a):
    global interflag1;
    global interflag2;
    global interflag3;
    global interflag4;
    global value
    if(a==pushButton1):
        # return "w"
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
    

#GPIO.remove_event_detect(BT1)
GPIO.add_event_detect(pushButton1, GPIO.RISING, callback=callback1) 
GPIO.add_event_detect(pushButton2, GPIO.RISING, callback=callback1) 
GPIO.add_event_detect(pushButton3, GPIO.RISING, callback=callback1) 
GPIO.add_event_detect(pushButton4, GPIO.RISING, callback=callback1) 
GPIO.add_event_detect(pushButton5, GPIO.RISING, callback=callback1) 


while (1):
    global quitFlag
    # drawGrid()
 





