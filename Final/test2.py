import numpy as np
import cv2
import pdb
import time
import Adafruit_BBIO.PWM as PWM

def moveServo(angle):
    duty = 100-((angle/180)*duty_span+duty_min)
    PWM.set_duty_cycle(servo_pin,duty)

servo_pin = "P8_13"
duty_min = 2.5
duty_max = 12.5 

duty_span =duty_max -duty_min
PWM.start(servo_pin,(100-duty_min),50.0,1)
moveServo(90)
time.sleep(0.1)


# def erode(image):
#     kernel = np.ones((6, 6), np.uint8)
#     return cv2.erode(image, kernel, iterations=1)
def erodeblue(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)   
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print ("camera is working")
else:
    print ("camera not working")
    

i = 0
def cameraRec():
    cap.open(0)
    #time.sleep(1)
    cap.set(3,600)
    cap.set(4,500)
    cap.set(cv2.CAP_PROP_FPS, 1)
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# define range of blue color in HSV
    lower_red = np.array([0,50,50]) #red value
    upper_red = np.array([10,255,255]) #red value
# Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

# Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
# cv2.imwrite("res.png", res)
    blur = cv2.GaussianBlur(res,(5,5),0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
# erode = erode(gray)
    erode = erodeblue(gray)
# cv2.imwrite("erode.png", erode)
# rat,thresh = cv2.threshold(erode,60,255,cv2.THRESH_BINARY) #Green
    rat,thresh = cv2.threshold(erode,50,255,cv2.THRESH_BINARY) #BLue
# thresh = cv2.adaptiveThreshold(erode,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
# circles = cv2.HoughCircles(thresh,cv2.HOUGH_GRADIENT,0.25,5)
# pdb.set_trace()
    yaxis = np.array([])
    for i in range (len(thresh)):
        for j in range (len(thresh[0])):
            if (thresh[i][j] > 0):
                # print(str(i)+ "  " + str(j))
                yaxis = np.append(yaxis,j)
                break
    yaxis.sort()
# print(yaxis)
    if yaxis.size == 0:
        center = 1000
    else:
        center = yaxis[int(yaxis.size/2)]
    print(center)
    cv2.imwrite("frame.png", thresh)
    cap.release()
    return center

resolution = 10
step = (110-70)/resolution
history = np.array([])
for i in range(resolution):
    moveServo(70+(i*step))
    time.sleep(0.08)
    result = cameraRec()
    history = np.append(history, result)

bestIndex = 0
smallestDiff = 1000
print(history)

for i in range (resolution):
    diff = abs(160-history[i])
    if(diff<=smallestDiff):
        bestIndex = i
        smallestDiff = diff
    
moveServo(70+(bestIndex*step))


#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cap.release()
cv2.destroyAllWindows()