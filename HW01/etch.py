#   Written by Haoxuan Sun 9/9/2020
#   Homework 01
#   This code is to implement the function of Etch-a-sketch
import numpy

width  = 8
length = 8

curX = 1
curY = 1
clearFlag = 0

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
        
            

def printGrid():
    for i in range (width+1):
        result = ""
        if i == 0:
            result += " "
        for j in range(length+1):
            result = result + grid[i][j] + "  "
        
        print(result)
grid[curX][curY] = "+"
printGrid()
print("Instruction: w to move up; s to move down; a to move left; d to move right; c to clear")
def drawGrid():
    value = input("Direction=\n")
    global curX
    global curY
    global clearFlag
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
    else:
        print("Say what? I might have heard")

    grid[curX][curY] = "+"
    if value == "c":
        clearFlag = 1
    printGrid()


while (1):
    drawGrid()





