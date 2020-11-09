import numpy as np
import cv2
import pdb
import time

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print ("camera is working")
else:
    print ("camera not working")
    
cap.open(0)
time.sleep(1)
cap.set(3,600)
cap.set(4,500)
cap.set(cv2.CAP_PROP_FPS, 1)
ret, frame = cap.read()

# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
lower_blue = np.array([0,50,50])
upper_blue = np.array([50,255,255])

    # Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
res = cv2.bitwise_and(frame,frame, mask= mask)
cv2.imwrite("frame.png", res)

# path = '/~/image.jpg'
# img = cv2.imread(path)
# print(img)

# cv2.imwrite("frame.png", frame)
# while(True):

#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

cap.release()
cv2.destroyAllWindows()