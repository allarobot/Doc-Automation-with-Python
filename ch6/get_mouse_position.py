#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:25:16 2018

@author: jayhan
"""
import pyautogui as ag
try:
    while(True):
        xy = ag.position()
        info = "X: {},Y:{}".format(*xy)
        print(info,end='')
        print('\b'*(len(info)),end='',flush=True)
except KeyboardInterrupt:
    print('\nDone')