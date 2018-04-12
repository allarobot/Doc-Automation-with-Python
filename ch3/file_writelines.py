#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 00:16:26 2018

@author: jayhan
"""
# 打开文件
fo = open("test_writelines.txt", "w")
print("文件名为: ", fo.name)
seq = ["记录 1 \n", "记录 2"]
fo.writelines( seq )

# 关闭文件
fo.close()
