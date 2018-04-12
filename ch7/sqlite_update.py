#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:21:23 2018

@author: jayhan
"""

import sqlite3
conn = sqlite3.connect('example.db')

#生成操作光标
c = conn.cursor()

##向数据库加入数据
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
##别忘了commit，将操作结果真正刷入数据库
conn.commit()

conn.close()