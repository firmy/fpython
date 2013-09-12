#!/usr/bin/env python
#coding=utf-8
#!/usr/bin/python

# -*- coding: utf-8 -*-
import MySQLdb as mdb
import sys
con = None 
try: 
    con = mdb.connect('localhost', 'root', 'firmy', '56demo');
    cur = con.cursor()
    cur.execute("SELECT id,num from tmp order by id desc limit 4")
    data = cur.fetchall()
    desc = cur.description
    print "%s %s" % (desc[0][0],desc[1][0])
    for row in data:
       print "%s %s" % row
except mdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
finally:    
        if con:    
           con.close()
