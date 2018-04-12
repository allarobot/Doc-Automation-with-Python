#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 09:08:24 2018

@author: jayhan
"""

from lxml import etree

##etree.Element, SubElement,tostring,tag, iterator

root_node = etree.Element("root")
print(root_node.tag)

child1_node = etree.SubElement(root_node,"child1")
child2_node = etree.SubElement(root_node,"child2")
child3_node = etree.SubElement(root_node,"child3")


# 添加属性
child3_node.text ="this is child3"
child3_node.set("id","id_child3")
print(child3_node.get("id"))

print(etree.tostring(root_node))
print(etree.tostring(child1_node))

print(root_node.tag)

for child in root_node:
    print(child.tag,child.text,etree.tostring(child))

##append, insert
#元素都是通过列表组织起来的
print("lists??")
print(etree.tostring(root_node[0]))
print(etree.tostring(root_node[1]))

grandson1_node = etree.SubElement(child1_node,"grandson1")
grandson2_node = etree.SubElement(child1_node,"grandson2")
grandson3_node = etree.SubElement(child3_node,"grandson3")
for child in root_node:
    print(etree.tostring(child))

print(etree.tostring(root_node[0][0]))
    
    
##iter("") filter with tag names
print("filtering by iter()")
for node in root_node.iter("child1","grandson1"):
    print(etree.tostring(node))