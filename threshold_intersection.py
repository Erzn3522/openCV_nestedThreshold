import cv2
import numpy as np

'''
# This is a helper function to cv2.threshold which is finding the value in between 
# up and low limit I assigng the pixel value to 255 under the lowerLimit(every value 
# under the lowerLimit is going to be an white) and i am making the opposite of it 
# that means i assigng 255 every pixel value bigger than upperLimit (every value 
# bigger the upperLimit is going to be an white)

    Args:
        image (numpy.ndarray): The original image.
        grayImage (numpy.ndarray): The grayscale version of the original image.
        lowerLimit (int): The lower limit for thresholding. If you want to get 0 value, use -1
        upperLimit (int): The upper limit for thresholding.

    Returns:
        numpy.ndarray: The modified image with contours drawn.


'''

def thresholdIntersection(image, grayImage, lowerLimit, upperLimit):
    thresholdLower = cv2.threshold(grayImage, lowerLimit, 255, cv2.THRESH_BINARY_INV)[1]
    thresholdUpper = cv2.threshold(grayImage, upperLimit, 255, cv2.THRESH_BINARY)[1]

    nestedImage = cv2.add(thresholdLower, thresholdUpper)
    thresholdNested = cv2.threshold(nestedImage, 0, 255, cv2.THRESH_BINARY_INV)[1]
    nestedContours, _ = cv2.findContours(thresholdNested, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return image, nestedContours
