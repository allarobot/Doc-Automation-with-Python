#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 00:40:54 2018

@author: jayhan
"""
fo = open("test_read.txt",'r')
print("文件名为: %s"%fo.name)

for line in fo.readlines():
    line = line.strip()
    print("读取的数据为: %s"%line)
    
fo.close()
