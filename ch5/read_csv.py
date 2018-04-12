#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:37:55 2018

@author: jayhan
"""

import csv


train=[]
with open("names.csv",'r',newline='') as f:
    lines = csv.reader(f,delimiter=',')
    for line in lines:
        print(line)
      

