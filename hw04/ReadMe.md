# hw04 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Memory map 
|  4 | mmap()
|  4 | i2c via Kernel
|  4 | Etch-a-Sketch via flask
|  4 | LCD display
|  1 | Extras
| 19 | **Total**

*My comments are in italics. --may*

# Homework 04
-------
# Memory Map
    |         |Start Address|End Address|
    | EMIF0   |0x4C00_0000 | 0x4CFF_FFFF |
    | SDRAM   |0x420F_0400 | 0x402F_FFFF |
    | GPIO1   |0x44E0_7000 | 0x44E0_7FFF |
    | GPIO2   |0x4804_C000 | 0x481A_CFFF |
    | GPIO3   |0x481A_C000 | 0x481A_CFFF |
    | GPIO4   |0x481A_E000 | 0x481A_EFFF |
    
# GPIO via mmap
The file test.py is the python code to use buttons to control the LED using register
The fast.py is used to test the shortest period of toggle time. 
The period measured on scope is 11.16us. The shortest period I got previously is 4.44us. The periods are pretty close. 

# i2c via the Kernel Driver
This program is to read temperature through i2c communication via kernal driver. 
Run the temperature.sh file, the temperature will be shown on screen. 

# Control the LED matrix from a browser
This is to control the LED matrix from browser. Run the etchWithWeb.py, and open the website on localserver. 
Use the four buttons to control the move of LED spot. 

# 2.4” TFT LCD Display
In the folder Pictures, there are three pictures for boris, rotated boris, and picture with texts.
Run on.sh first, the use other command for playing pictures and movies. Text.sh is to put text on a picture. 
To rotate the picture, change the 90 to 180 degrees in on.sh.
sudo fbi -noverbose -T 1 -a boris.png
mplayer -vf-add rotate=4 -framedrop hst_1.mpg
# Extra
Pygame is working, the picture is in folder Pictures called "pygame.jpg".

