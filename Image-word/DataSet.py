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
import sys
import random
import pickle


data = pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\ML\Handwriting Project\A_Z\A_Z Handwritten Data.csv").astype('float32')

#reshaping the data in csv file so that it can be seen as image

train_x = data.drop('0',axis = 1)
train_x = np.reshape(train_x.values, (train_x.shape[0],28,28))
train_y = data['0']


## Word to number mapping

###Data reshaping
train_X = train_x.reshape(train_x.shape[0],train_x.shape[1],train_x.shape[2],1)
###image reshaping
train_yOHE = to_categorical(train_y, num_classes = 26, dtype='int')
## put in in a list with [image,map]
#shuffle data


###test run
##for sample in training_data:
##    print(sample[1])

X = train_X
y = train_yOHE
fin = []
for i in range(len(X)):
    fin.append([X[i],y[i]])
random.shuffle(fin)

X_ = []
y_ = []
for i,j in fin:
    X_.append(i)
    y_.append(j)

X = np.array(X_).reshape(-1,28,28,1)
y = np.array(y_).reshape(-1,26)

    

    
#Save data
pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()


