#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 23:39:21 2018

@author: jayhan
"""

import bs4


html_doc = open("countries.xml").read()
soup = bs4.BeautifulSoup(html_doc,"lxml")
print(soup.prettify())

a_tags = soup.select("country")
print("a_tags:\n",a_tags)


    
