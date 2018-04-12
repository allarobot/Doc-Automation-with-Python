#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:47:19 2018

@author: jayhan
"""
import os

path = input("please input the path of files:")
for path in os.walk(path):
    print(path)
