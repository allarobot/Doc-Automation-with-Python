#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 00:27:52 2018

@author: jayhan
"""
# 打开文件
fo = open("test_read.txt", "r+")
print("文件名为: ", fo.name)

line = fo.read(10)
print("读取的字符串: \n%s" % (line))

# 关闭文件
fo.close()
