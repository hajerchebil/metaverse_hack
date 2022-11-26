import cv2
import numpy as np
import random
import time
initialState = None  
cap = cv2.VideoCapture('./videos/1.mp4')
ret, frame1 = cap.read()
ret, frame2 = cap.read()
# Loop until the end of the video
counter = 0
rand_intensity = "intensity: " + str(random.randint(0, 9))
rand_velocity = "velocity: " + str(random.randint(30, 50))

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter('filename.avi',cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

current_time = time.time()
while (cap.isOpened()):
    #current_frame = cap.get(cv2.CV_CAP_PROP_POS_FRAMES)
    difference = cv2.absdiff(frame1,frame2)
    gray_image = cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_image,(25,25),0)
    ret,thresh = cv2.threshold(blur,18,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,iterations=3)
    contours,_ =cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if ((time.time()-current_time<80) or (time.time()-current_time>=104)):
        cv2.circle(frame1, (150, 315), 30, (255, 0, 0), 2) # radius is 5,  blue color RGB is 255, 0, 0)
        color = (0, 0, 255)
        # Line thickness of 2 px
        thickness = 2
        font = cv2.FONT_HERSHEY_SIMPLEX
        org = (00, 185)
        if counter%5 == 0:
            rand_intensity = "intensity: " + str(random.randint(5, 9))
            rand_velocity = "velocity: " + str(random.randint(30, 50))
        cv2.putText(frame1, rand_intensity, org, font, 1,
                    color, thickness, cv2.LINE_AA, False)
        cv2.putText(frame1, rand_velocity, (00, 250), font, 1,
                    color, thickness, cv2.LINE_AA, False)
    result.write(frame1)
    cv2.imshow("Detect",frame1)
    frame1=frame2
    ret,frame2 = cap.read()

    if cv2.waitKey(30) == 27:
        break
    counter += 1
result.release() 