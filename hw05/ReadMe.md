# hw05 grading

| Points      | Description |
| ----------- | ----------- |
|  2 | Project - *Intresting project ideas. Do you know of a Siri API?*
|  2 | Makefile
|  4 | Kernel Source
|  2 | Cross-Compiling
|  8 | Kernel Modules: hello, ebbchar, gpio_test, led
|  0 | Extras
| 18 | **Total**

*My comments are in italics. --may*

# Homework 05
-------
# MakeFile 
The Makefile is in fold Makefile, in that folder and type "make" to compile the app.c. Then you can run app.arm to get HelloWorld print out.

# Installing the Kernel Source
Follow the instruction to install the certain version of kernel on host and bone.

# Cross-Compiling
The screenshots are named CrossCompileBone.png and CrossCompileHost.png show the program from both host and bone.
Follow the instruction to compile file on host for the file in bone. 

# Kernel Modules
In the folder gpio_test and type make to compile the c file. Install the kernel module by typing "sudo immod gpio_test.ko".
Then two buttons will toggle the LEDs on both rising and falling edges. 
In the folder led, and type make to compile the c file. Then use command "sudo immod" to install the kernel module. 
Two leds will blink in different rates. 
To remove the kernel module, type "sudo rmmod"