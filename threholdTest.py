import cv2
from windowCreator import *
from threshold_intersection import *

imgBase = cv2.imread('images/transition2.png')
grayImage = cv2.cvtColor(imgBase, cv2.COLOR_BGR2GRAY)
#describing the up and low limit for the threshold function
lowerVal = 0
upperVal = 100
#this func creating a function according to out parameters
# Check the windowCreator.py and  threshold_Intersection.pyfile for more details 
WindowCeator( lowerVal, upperVal, thresholdIntersection(imgBase, grayImage, lowerVal, upperVal))
# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
 
# closing all open windows
cv2.destroyAllWindows()
