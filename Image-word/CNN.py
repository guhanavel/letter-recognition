import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPool2D
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import sys

import pickle


pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

#split data
train_x, test_x, train_y, test_y = train_test_split(X, y, test_size = 0.1)

#running data set into CNN

#Part1: creating a CNN
model = Sequential()

# Convolutional layer. Learn 32 filters using a 3x3 kernel
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))

# Max-pooling layer, using 2x2 pool size
model.add(MaxPool2D(pool_size=(2, 2)))

##Convolutional layer. Learn 64 filters using a 3x3 kernel
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu', padding = 'same'))

##Max-pooling layer, using 2x2 pool size
model.add(MaxPool2D(pool_size=(2, 2)))

## Convolutional layer. Learn 128 filters using a 3x3 kernel
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu', padding = 'same'))

## Max-pooling layer, using 2x2 pool size
model.add(MaxPool2D(pool_size=(2, 2), strides=2))

##Flatten units
model.add(Flatten())

 # Add a hidden layer with dropout'
model.add(Dense(64,activation = "relu"))
model.add(Dense(128,activation ="relu"))
Dropout(0.5)


#Add output layers for all 26 letters
model.add(Dense(26,activation ="softmax"))

# Train neural network
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(train_x,train_y,epochs=15)



### Evaluate neural network performance
model.evaluate(test_x,test_y, verbose=2)

# Save model to file
if len(sys.argv) == 2:
   filename = sys.argv[1]
   model.save(filename)
   print(f"Model saved to {filename}.")

