#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:47:19 2018

@author: jayhan
"""
import os

path = input("please input the path of files:")
print(path)
for root,dirs,filename in os.walk(path):
    for file in filename:
        filepath = os.path.join(root,file)
        folder = root.split(os.sep)[-1]
        print(root,folder,filepath)
