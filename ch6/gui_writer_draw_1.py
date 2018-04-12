#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:17:55 2018

@author: jayhan
"""
import pyautogui as ag
screenWidth, screenHeight = ag.size()
ag.moveTo(screenWidth/2, screenHeight/2)
ag.click()
ag.mouseDown(button='left')
distance = 200
while distance > 0:
    ag.dragRel(distance, 0, duration=0.5,button='left')   # move right
    distance -= 5
    ag.dragRel(0, distance, duration=0.5,button='left')   # move down
    ag.dragRel(-distance, 0, duration=0.5,button='left')  # move left
    distance -= 5
    ag.dragRel(0, -distance, duration=0.5,button='left')  # move up 
ag.click()