#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:21:23 2018

@author: jayhan
"""

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

## Never do this -- insecure!
#symbol = 'RHAT'
#c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
print("查询一个结果:")
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

print("查询所有结果:")
for row in c.execute('SELECT * FROM stocks'):
    print(row)

print("查询所有结果，并排序输出:")
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
conn.close()