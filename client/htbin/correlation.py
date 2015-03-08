#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import cgi

mydir = os.path.dirname( os.path.abspath( __file__ ) )
apidir = os.path.realpath(os.path.join(mydir, u"../../api"))
sys.path.append(apidir)
import simple_sql as ss
import simple_query as sq

condition = None
query = sq.find_query("x")
if query is not None:
    condition = "x='" + query +"'"

print "Content-type: text/javascript; charset=utf-8"
print

db = ss.Db()
print db.select_json(None,"correlation", condition, order="val", direction="DESC")
