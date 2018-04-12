#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 17:55:00 2018

@author: jayhan
"""
import  bs4, requests
url = "http://www.w3school.com.cn/index.html"

##get html file from website
pHtml = requests.get(url)
print(pHtml.raise_for_status,pHtml.encoding)
encoding_temp = pHtml.encoding
pHtml.encoding = pHtml.apparent_encoding
pHtmlText = pHtml.text

soup = bs4.BeautifulSoup(pHtmlText,'lxml')
print(soup.prettify)

fp =open("download.html",'w',encoding=pHtml.encoding)
fp.write(pHtmlText)
fp.close()