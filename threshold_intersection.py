import cv2
import numpy as np

#Abdullah Erzin

#this is a helper function to cv2.threshold which is finding the value in between up and low limit
# I assigng the pixel value to 255 under the lowerLimit(every value under the lowerLimit is going to be an white)
# and i am making the opposite of it that means i assigng 255 every pixel value bigger than upperLimit 
# (every value bigger the upperLimit is going to be an white)
def thresholdIntersection(image, grayImage, lowerLimit, upperLimit):
    _,  thresholdLower = cv2.threshold(grayImage, lowerLimit, 255, cv2.THRESH_BINARY_INV)
    _, thresholdUpper = cv2.threshold( grayImage, upperLimit, 255, cv2.THRESH_BINARY)


    # And by summing these threshold values, I change every pixel value to 255, except for 
    # the lower and upper limit range, so that the intermediate region remains.    
    nestedImage = np.add(thresholdLower, thresholdUpper)    
    _,threshold_Nested = cv2.threshold(nestedImage, 0, 255, cv2.THRESH_BINARY_INV)
    nestedContours, _ = cv2.findContours(threshold_Nested, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, nestedContours, -1, (0, 0, 255), 2)
    return image