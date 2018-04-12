#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 00:36:29 2018

@author: jayhan
"""

# 打开文件
fo = open("test_read.txt", "r")
print("文件名为: ", fo.name)

line = fo.readline()
print("读取第一行 \n%s" % (line))
line = fo.readline()
print("读取第二行 \n%s" % (line))
line = fo.readline(4)
print("读取的字符串为: \n%s" % (line))

# 关闭文件
fo.close()