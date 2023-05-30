import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm
import tensorflow as tf
import sys
import pickle
import matplotlib.pyplot as plt
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.callbacks import ReduceLROnPlateau, EarlyStopping
from tensorflow.keras.utils import to_categorical
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle


pickle_in = open("X.pickle","rb")
test_X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
test_yOHE = pickle.load(pickle_in)


DATADIR = r'C:\Users\Asus\OneDrive\Desktop\ML\Handwriting Project\Test'
word_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',
             15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z'}

model = tf.keras.models.load_model(hand2.h5)

##for img in os.listdir(DATADIR):
##    img_array = cv2.imread(os.path.join(DATADIR,img),cv2.IMREAD_GRAYSCALE)
##    new_array = cv2.resize(img_array, (28,28))
##    img_final =np.reshape(new_array, (1,28,28,1))
##    img_pred = word_dict[np.argmax(model.predict(img_final))]
##    print(img_pred)

fig, axes = plt.subplots(3,3, figsize=(8,9))
axes = axes.flatten()
for i,ax in enumerate(axes):
    img = np.reshape(test_X[i], (28,28))
    ax.imshow(img, cmap="Greys")
    
    pred = word_dict[np.argmax(model.predict(test_yOHE[i]))]
    ax.set_title("Prediction: "+pred)
    ax.grid()
    
