#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 13:16:50 2018

@author: jayhan
"""
import PyPDF2

pdfWriter = PyPDF2.PdfFileWriter()
pdfFileObj = open('Neo4j_graph_platform.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
page1 = pdfReader.getPage(1)
page0 = pdfReader.getPage(0)
pdfWriter.addPage(page1)
pdfWriter.addPage(page0)
pdfOutputFile = open('hello.pdf', 'wb') 
pdfWriter.write(pdfOutputFile) 
pdfOutputFile.close()
