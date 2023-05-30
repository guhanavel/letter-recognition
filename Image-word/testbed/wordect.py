import cv2
import numpy as np
from tester import convert
from arr import sentence_finder
from PIL import Image

sentences = sentence_finder("apple.png",1)

def sort_contours(contours):
    # construct the list of bounding boxes and sort them from top to bottom
    boundingBoxes = [cv2.boundingRect(c) for c in contours]
    (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes)
           , key=lambda b: b[1][0], reverse=False))
    # return the list of sorted contours
    return contours

def word(sen):
    words = []
    for i in sen:
        gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY) 
        _,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV) 
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(10,5))
        dilated = cv2.dilate(thresh,kernel,iterations = 1)
        eroded = cv2.erode(dilated,kernel,iterations = 0)
        contours, hierarchy = cv2.findContours(eroded,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    new_con = sort_contours(contours)


    for contour in new_con:

        [x,y,w,h] = cv2.boundingRect(contour)

        crop = i[y:y+h,x:x+w]
        size = crop.shape[:2]
        max_dim = max(size)
        delta_w = max_dim - size[1] + 10
        delta_h = max_dim - size[0] + 10
        top, bottom = delta_h, delta_h
        left, right = delta_w, delta_w
        crop = cv2.copyMakeBorder(crop, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255,255,255])
        words.append(crop)
    return words

def guess(word):
        final = []
        add = " "
        i = 0
        for wo in word:
            myy = ""
            gray = cv2.cvtColor(wo,cv2.COLOR_BGR2GRAY) 
            _,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV) 
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
            dilated = cv2.dilate(thresh,kernel,iterations = 1)
            eroded = cv2.erode(dilated,kernel,iterations = 1)
            contours, hierarchy = cv2.findContours(eroded,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


            new_con = sort_contours(contours)

            for contour in new_con:

                [x,y,w,h] = cv2.boundingRect(contour)

                crop = wo[y:y+h,x:x+w]
                size = crop.shape[:2]
                max_dim = max(size)
                delta_w = max_dim - size[1] + 10
                delta_h = max_dim - size[0] + 10
                top, bottom = delta_h, delta_h
                left, right = delta_w, delta_w
                crop = cv2.copyMakeBorder(crop, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[255,255,255])
                myy += convert(crop)
            final.append(myy)
        return final    

te = word(sentences)
fi = guess(te)
