# -*- coding: utf-8 -*-
"""number detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17SuTyVrPWTCVZ4ZabDjMZp4kftehVeL3
"""

from google.colab import drive
drive.mount('/content/drive')

# Create model to Digit recogmization from 0-9 and test pridiction:

# import the depedency packages or models to run the further code

import tensorflow as tf # tensorflow for dataset, tranining and pridiction
import numpy as np      # numarical tool for python
import matplotlib.pyplot as plt  # for graph

mnist = tf.keras.datasets.mnist # from where dataset to be load

(x_train,y_train), (x_test,y_test) = mnist.load_data() # load data from mnist dataset

x_train = tf.keras.utils.normalize(x_train, axis=1) # normalize train images such that all value in array shouldn't exceed 1
x_test = tf.keras.utils.normalize(x_test, axis=1)   # normalize test images such that all value in array shouldn't exceed 1


plt.imshow(x_test[3])  # test whethere the data is loaded or not
print(x_test[3].shape) # check the shape of img_data

# make 3 layer
# 2 layer with 128 neurons using relu function
# 1 layer with 12 neurons using softmax function

model= tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())

model.add(tf.keras.layers.Dense(128,activation= tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation= tf.nn.relu))

model.add(tf.keras.layers.Dense(12,activation= tf.nn.softmax))

#compile Model using adam optimizer:
model.compile(optimizer= 'adam', loss= 'sparse_categorical_crossentropy', metrics=['accuracy'])

# fit model to the ANN to give ready model to predict
model.fit(x_train , y_train , epochs = 6)

# inatall pydrive to get athuntication from drive and save model in drive
# !pip install -U -q PyDrive

# from pydrive.auth import GoogleAuth  
# from pydrive.drive import GoogleDrive 
# from google.colab import auth 
# from oauth2client.client import GoogleCredentials

# auth.authenticate_user()
# gauth = GoogleAuth()
# gauth.credentials = GoogleCredentials.get_application_default()
# drive = GoogleDrive(gauth)

# model.save('model.h5')
# model_file = drive.CreateFile({'title' : 'model.h5'})
# model_file.SetContentFile('model.h5')
# model_file.Upload()

# # mount drive to load and upload data from drive
# from google.colab import drive
# drive.mount('/mntDrive')

# new_model = tf.keras.models.load_model('/mntDrive/My Drive/Colab Notebooks/number_detect_keras/model.h5')

# import openCV
import cv2

test_dir = '/content/drive/My Drive/1-9/1.jpg'
test_img = cv2.imread(test_dir, cv2.IMREAD_GRAYSCALE) # read and convert image to gray scale
plt.imshow(test_img, cmap ='gray')

# image preparation:
test_img = cv2.resize(test_img,(28,28))


test_img = 255 - test_img # invert the image, always accept the inverted image


test_img = test_img.reshape(1, 28, 28, 1)  # after this image ready to predict by model

# check the image how looks like
plt.imshow(test_img.reshape(28, 28))

pridiction = model.predict(test_img)
print(pridiction)



np.argmax(pridiction[0])

