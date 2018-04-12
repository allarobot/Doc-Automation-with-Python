#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:30:26 2018

@author: jayhan
"""

#见面礼：）
print("hello world!")

#怎么称呼呢？
strName = input("先生，请问您贵姓？")
print("很高兴见到您,",strName,"先生!")

#有空格不美观
strName = input("先生，请问您怎么称呼？")
print("很高兴见到您,",strName,"先生!",sep='') #end

#格式化字符串
strName = '%s%s'%(strName,"先生")
print("很高兴见到您,",strName,sep='') 
#字符串类型
type(strName)
#字符串的长度
num=len(strName)


#多大了
age = input("请输入您的年龄:")
type(age)
# float(), int(), str()
age = int(age) + 1

#
print(age+1)