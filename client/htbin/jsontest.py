#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import cgi
import cgitb; cgitb.enable()
import json

print "Content-type: text/javascript; charset=utf-8"
print

form = cgi.FieldStorage()

foo = form.getfirst("foo", "")
bar = form.getfirst("bar", "")
baz = form.getfirst("baz", "")

print json.dumps([{'key':'foo','value':foo},
    {'key':'bar','value':bar},
    {'key':'baz','value':baz}])
