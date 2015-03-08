#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os
import cgi

mydir = os.path.dirname( os.path.abspath( __file__ ) )
apidir = os.path.realpath(os.path.join(mydir, u"../../api"))
sys.path.append(apidir)
import simple_query as sq


## Get and parse a query string
#query_string_key = 'QUERY_STRING'
#if query_string_key in os.environ:
#    query = cgi.parse_qs(os.environ[query_string_key])
#else:
#    query = {}
#
#message_key = 'message'
#if message_key in query:
#    message = cgi.escape(query[message_key][0])
#else:
#    message = "ECHO WORLD"
#

message = sq.find_query("message") 

print "Content-type: text/html"
print
print "<html>"
print "<center>hogehoge</center>"
print message
print "</html>"

