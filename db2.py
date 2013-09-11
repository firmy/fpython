#!/usr/bin/python
# -*- coding: utf-8 -*-
import _mysql as mdb
import sys
con = None 
con = mdb.connect('localhost', 'root', 'firmy', 'web_daydayup_1')    
cur.query("SELECT VERSION()")
result = cur.fetchall()
for row in result:
    print row
