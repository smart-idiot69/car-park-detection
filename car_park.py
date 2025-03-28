
import numpy as np
import cv2 as cv
import pickle


video = cv.VideoCapture(r'C:\Users\352\Desktop\car_park_detection\data\carPark.mp4')
with open(r'C:\Users\352\Desktop\car_park_detection\data\rectangles', 'rb') as f:
    rec_loc = pickle.load(f)

cpn = len(rec_loc)
#car_park_number
cars = cpn
while True:
    ret , frame = video.read()
    if not ret:
        break

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_GB = cv.GaussianBlur(frame_gray, (9,9), 10)
    frame_thresh = cv.adaptiveThreshold(frame_GB, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, 7)
    
    for loc in rec_loc:
        new_frame = frame_thresh[loc[1]:loc[1] + (loc[3] - loc[1]), loc[0]:loc[0] + (loc[2] - loc[0])]
        if new_frame.sum() < 700000:
            cv.rectangle(frame, (loc[0], loc[1]), (loc[2], loc[3]), (0,0,255), 2)
            if cars < cpn:
                cars += 1
        else:
            cv.rectangle(frame, (loc[0], loc[1]), (loc[2], loc[3]), (0,255,0), 2)
            if cars > 0:
                cars -= 1
        


    
    cv.imshow('frame_gray', frame_thresh)
    cv.imshow('frame', frame)
    if cv.waitKey(5) & 0xFF == 27:
        break
    


cv.destroyAllWindows()
video.release()



















