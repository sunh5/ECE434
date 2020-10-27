# hw03 grading

| Points      | Description |
| ----------- | ----------- |
|  5 | TMP101 
|  3 |   | setup.sh
|  2 |   | Documentation
|  5 | Etch-a-Sketch
|  3 |   | setup.sh
|  2 |   | Documentation
| 20 | **Total**

*My comments are in italics. --may*

# TMP101
There four code files in this folder. First is TMP.sh, this is a shell script to read the temperatures from 
two sensors. Run the code, and the temperatures will be printed out. 
Second is readTMP.py, this is a python file to read the temperatures. It runs the same as the shell script. 
Third is a i2cset command file to define the high and low limit for temperatures. Run the shell and it can be checked
in the next python file.
The last one is alarm.py, this file is to use interrupt to auto detect the temperature high and low limit.
The interrupt successfully triigered when the temperature above the limit, a warning be printed out in callback. 

# Etch-a-sketch with LED matrix
The file name is etchWithMatrix.py. Instead of drawing on screen, this file will draw on the 8x8 LED matrix. All the other 
command are the same as before, use five buttons to move up, down, left, right, and clear. 
# Etch-a-sketch with Encoder
The file name is etchWithEncoder.py. Before running this file, run setup.sh first to set the pinmode to eqep.
Then, run the file and rotate the encoders, red spot will be drawn on LED matrix. The direction 
depends on which encoder rotated, and whether clockwise or counterclockwise is selected. 

All the assignments are finished as expected. Pretty useful skill. 

