import cv2
from threshold_intersection import *

imgBase = cv2.imread('images/transition2.png')
grayImage = cv2.cvtColor(imgBase, cv2.COLOR_BGR2GRAY)
# describing the up and low limit for the threshold function
lowerLimit = -1
upperLimit = 100
windowName =f'threshold between {lowerLimit} and {upperLimit}'

#this func creating a function according to out parameters
nestedImage , contours = thresholdIntersection(imgBase, grayImage, lowerLimit, upperLimit)

# Draw the contours on the original image
cv2.drawContours(nestedImage, contours, -1, (0, 0, 255), 2)

cv2.namedWindow(windowName)    
cv2.imshow(windowName, nestedImage)
cv2.waitKey(0) 
cv2.destroyAllWindows()
