from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

def arrise(img):
    image = cv2.imread(img)
    array = image.tolist()
    return array

def find_pix(array):
    count = []
    for arra in array:
        for arr in arra:
            if 255 not in arr:
                if array.index(arra) not in count:
                    count.append(array.index(arra))
    if len(array) not in count:
        count.append(len(array))
    return count

def intervals(count,x):
    inter = []
    inter.append((0,count[0]))
    count.sort()
    counter = count[0]
    for i in range(len(count)-1):
        if count[i+1] - count[i] > x:
            inter.append((counter,count[i]))
            counter = count[i]
    return inter
    
def pieced(array,count):
    slicer = []
    for i in count:
        slicer.append(array[i[0]:i[1]])
    return slicer

def shown(slicer):
    store = []
    for i in slicer:
        ary = np.array(i,dtype=np.uint8)
        new_image = Image.fromarray(ary)
        store.append(ary)
    return store

def sentence_finder(image,x):
    sen = []
    array = arrise(image)
    con = find_pix(array)
    inte = intervals(con,x)
    to = pieced(array,inte)
    return shown(to)

