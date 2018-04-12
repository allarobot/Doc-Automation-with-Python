#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 15:47:19 2018

@author: jayhan
"""
import os

path = '/Users/jayhan/Documents/DocumentAutomationWithPython'
for info in os.walk(path):
    print(info)
    
