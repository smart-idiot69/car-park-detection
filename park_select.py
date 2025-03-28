
import numpy as np
import cv2 as cv
import pickle

video = cv.VideoCapture(r'C:\Users\352\Desktop\car_park_detection\data\carPark.mp4')

ret , frame = video.read()
width = 90
height = 40

rectangle_list = []
def draw_rectangle(event, x, y, flage, param):
    if event == cv.EVENT_LBUTTONDOWN:
        x2 = x+width
        y2 = y+height
        cv.rectangle(frame, (x, y), (x2, y2), (0,0,255), 2)

        rectangle_list.append([x, y, x2, y2])




cv.namedWindow('frame')
cv.setMouseCallback('frame', draw_rectangle)

while True:
    cv.imshow('frame', frame)
    if cv.waitKey(5) & 0xFF == 27:
        break

cv.destroyAllWindows()

rectangle_list = np.array(rectangle_list)
with open(r'C:\Users\352\Desktop\car_park_detection\data\rectangles', 'wb') as f:
    pickle.dump(rectangle_list, f)
