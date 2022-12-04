import cv2 
#Abdullah Erzin
#this is a void func which is creating a display with a name with the upper and lower threshold limits
def WindowCeator(lowerLimit, upperLimit, img):
    windowName =f'threshold between {lowerLimit} and {upperLimit}'
    cv2.namedWindow(windowName)    
    cv2.imshow(windowName, img)