#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:49:16 2018

@author: jayhan
"""

# A minimal SQLite shell for experiments

import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

buffer = ""

print("Enter your SQL commands(end with ;) to execute in sqlite3.")
print("Enter a blank line to exit.")

while True:
    line = input()
    if line == "":
        break
    buffer += line
    if sqlite3.complete_statement(buffer):
        try:
            buffer = buffer.strip()
            cur.execute(buffer)
            #con.commit()

            if buffer.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())
        except sqlite3.Error as e:
            print("An error occurred:", e.args[0])
        buffer = ""

con.close()

##example commands as following
#create table test1 (name text,weight real) ;

#insert into test1 values ('jay','65.1') ;

#insert into test1 values ('jay',65.2) ;

#select * from test1 ;
#>>[('jay', 65.1), ('jay', 65.2)]

#insert into test1 values ('mary',50.2) ;

#insert into test1 values ('lily',50.2) ;

#select * from test1 where name='lily' ;
#>>[('lily', 50.2)]

#select * from test1 where weight='50.2' ;
#>>[('mary', 50.2), ('lily', 50.2)]