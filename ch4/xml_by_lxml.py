#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 09:03:41 2018

@author: jayhan
"""

from lxml import etree

xml_doc = open("movies.xml",'r').read()
xml_node = etree.XML(xml_doc)
print(etree.tostring(xml_node,pretty_print=True))

for mov in xml_node:
    print(mov.tag,mov.text)
    print(mov.items())
    for attr in mov:
        print(attr.tag,attr.text)
        print(attr.items())
        
