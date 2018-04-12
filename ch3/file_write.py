#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 00:24:26 2018

@author: jayhan
"""

# 打开文件
fo = open("test_write.txt", "w")
print("文件名为: ",fo.name)
text = "记录 1\n记录 2"
fo.write(text )

# 关闭文件
fo.close()