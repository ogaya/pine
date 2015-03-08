# -*- coding: utf-8 -*-
import unittest
import statistics as st
import simple_sql as ss
import datetime
import random

storage_table_name = "storage"

db=ss.Db()

db.table_delete("statistics_result")


