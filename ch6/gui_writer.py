#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:17:55 2018

@author: jayhan
"""

import pyautogui
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=0.5)   # move down
    pyautogui.dragRel(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=0.5)  # move up