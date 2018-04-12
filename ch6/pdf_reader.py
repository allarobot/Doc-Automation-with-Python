#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:16:29 2018

@author: jayhan
"""

import PyPDF2 
pdfFileObj = open('Neo4j_graph_platform.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0) 
txt = pageObj.extractText()
print(txt)
