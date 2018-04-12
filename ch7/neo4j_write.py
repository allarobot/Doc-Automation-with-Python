#!/Users/jayhan/VirtualEnvs/flask_py3/bin python
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:40:53 2017
@author: jayHan

Modified 2018.1.4,15:44pm
function demonstration

"""
from py2neo import Graph

        
conn = Graph('bolt://127.0.0.1:7687',user="neo4j",password='comac.123')
query = '''create (n1:ACTOR{name:'tom',earning:1000})
        return n1
        '''
data =conn.run(query).data()
print(data)