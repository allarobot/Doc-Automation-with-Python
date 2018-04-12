#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:17:04 2018

@author: jayhan
"""

import docx 
doc = docx.Document('helloworld.docx') 
for paragram in doc.paragraphs:
    print(paragram.text)
