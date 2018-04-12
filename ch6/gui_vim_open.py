#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:37:19 2018

@author: jayhan
"""
import pyautogui as ag
import time
ag.PAUSE = 0.5
ag.moveTo(1346,9)
ag.click()
ag.typewrite('terminal')
ag.typewrite(['enter'])
ag.typewrite('vim newfile')
ag.typewrite(['enter'])
ag.moveTo(1346,9)
ag.click()
ag.typewrite('pages')
ag.typewrite(['enter'])
ag.moveTo(340,544)
ag.click()
ag.moveTo(1168,761)
ag.click()
time.sleep(2)
width,height = ag.size()
for i in range(3):
    ag.click(5,46)
    ag.moveTo(width/2,height/4)
    ag.dragRel(0,height/4)
    ag.keyDown('command')
    ag.keyDown('c')
    ag.keyUp('command')
    ag.keyUp('c')
    ag.typewrite(['down']*10)
#    ag.scroll(0,-height/4)

    
    ag.moveTo(1346,9)
    ag.click()
    ag.typewrite('pages')
    ag.typewrite(['enter'])    
    ag.click(width/2,height/2)
    ag.keyDown('command')
    ag.keyDown('v')
    ag.keyUp('command')
    ag.keyUp('v')
    ag.scroll(-height/4)
    
