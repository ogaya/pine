#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import os

def find_query(key, index=0):

    # Get and parse a query string
    query_string_key = 'QUERY_STRING'
    if query_string_key in os.environ:
        query = cgi.parse_qs(os.environ[query_string_key])
    else:
        query = {}
    
    if key in query:
        return cgi.escape(query[key][index])
    else:
        return None

