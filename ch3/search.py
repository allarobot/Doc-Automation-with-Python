#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 00:24:04 2018

@author: jayhan
"""

import os
import sys
cmd_set = ('all','file','text','folder')
if len(sys.argv)==4:
    path = sys.argv[1]
    cmd = sys.argv[2]
    param2 = sys.argv[3]
    if cmd not in cmd_set:
        print("wrong command!")
else:
    print("command length not right!")

files = os.listdir(path)
index =1
for file in files:
    if os.path.isfile(file):
        if (cmd=='file') or (cmd=='all'):
            if os.path.basename(file).find(param2)!=-1:
                info = "{} file:{}".format(index,file)
                index +=1
                print(info)
                
        if (cmd=='text') or (cmd=='all'):           
           with open(file,'r') as f:
               try:
                   lines = f.readlines()
                   for line in lines:
                       if param2 in line:
                           info= "{} text:{} @ file:{}".format(index,line.rstrip(),file)
                           index+=1
                           print(info)
                           
               except:
                   pass
            
    else:    
        if cmd=='folder' or cmd=='all':
            if os.path.isdir(file) and os.path.dirname.find(param2)!=-1:
                info="{} folder:{}".format(index,file)
                index+=1
                print(info)
                
    
            
        
            
            
    
