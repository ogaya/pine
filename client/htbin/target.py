#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import cgi

mydir = os.path.dirname( os.path.abspath( __file__ ) )
apidir = os.path.realpath(os.path.join(mydir, u"../../api"))
sys.path.append(apidir)
import simple_sql as ss

db = ss.Db()

#print "Content-type: text/javascript; charset=utf-8"
print "Content-type: application/json; charset=utf-8"
print

print db.select_json(None,"target")
