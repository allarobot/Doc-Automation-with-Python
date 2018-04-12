#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:02:16 2018

@author: jayhan
"""
info = input("请输入等腰三角形的高度,宽度,表示符号:").split(",")
height,width,symbolic = int(info[0]),int(info[1]),info[2]
dt = (width-1)/(height-1)
for i in range(0,height):
    blank_n =int(dt/2*i)
    line = " "*blank_n+symbolic*int(width-blank_n*2)+" "*blank_n
    print(line)

