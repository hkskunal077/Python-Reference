import cv2
from matplotlib import pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)
img = cv2.imread('C:\AcademicProjects\OpenCV\mess.jpg', cv2.IMREAD_COLOR)

while True:
    ret, frame = cap.read()
    cv2.imshow('FRAME',frame)
    
    key = cv2.waitKey(30) & 0xFF
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
