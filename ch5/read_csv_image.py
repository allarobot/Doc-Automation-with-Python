#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:37:55 2018

@author: jayhan
"""

import csv


train=[]
with open("data.csv",'r',newline='') as f:
    f.readline()  
    lines = csv.reader(f,delimiter=',')
    for line in lines:
        train.append(line)
      
import numpy as np
import matplotlib.pyplot as plt
data = np.array(train,dtype='int8')
print(data.shape)
label = data[:,0] 
data = data[:,1:]
img = data.reshape(data.shape[0],28,28) 
print(label.shape)
print(img.shape)

index = 3
plt.figure("image_{}".format(label[index]))
plt.imshow(img[index],cmap='gray')
plt.show()
