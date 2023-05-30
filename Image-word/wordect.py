import cv2
import numpy as np
from tester import convert
from PIL import Image

image = cv2.imread("sen.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
_,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV) 
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 1) 
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
word = ""
i = 10
for contour in contours:

    [x,y,w,h] = cv2.boundingRect(contour)

    crop = image[y:y+h,x:x+w]
    size = crop.shape[:2]
    max_dim = max(size)
    delta_w = max_dim - size[1] + 10
    delta_h = max_dim - size[0] + 10
    top, bottom = delta_h, delta_h
    left, right = delta_w, delta_w
    crop = cv2.copyMakeBorder(crop, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255,255,255])
    cv2.imwrite(str(i)+".png",crop)
    word += convert(crop)
    i += 1
    
new = word[::-1]   

    

    
