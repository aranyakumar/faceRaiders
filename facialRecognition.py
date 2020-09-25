import cv2 as cv
import numpy as np
a = cv.imread("mother.jpg")
image = cv.cvtColor(a, cv.COLOR_BGR2HSV)
cv.imshow('window!', a)
cv.waitKey(0)
cv.imwrite("doesthiswork.jpg",a)

