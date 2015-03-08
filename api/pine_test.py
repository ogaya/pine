# -*- coding: utf-8 -*-
import unittest
import statistics as st
import simple_sql as ss
import datetime

class TestStatistics(unittest.TestCase):

    __storage_table_name = "storage"

    def test_where(self):
        db=ss.Db()
        db.table_delete(self.__storage_table_name)

        start_time = datetime.datetime(2014, 1, 1)

        for val in range(0, 10):
            record = {}
            record["tag"] = "2AI001"
            record_time = start_time + datetime.timedelta(minutes=10*val)
            record["timestamp"] = record_time
            record["value"] = val
            db.write(record,self.__storage_table_name,["tag","timestamp"])

        row = db.select_field("value",self.__storage_table_name)
        self.assertEqual(len(row) , 10)
        where_str = "timestamp=" + db.convert_psql_value(datetime.datetime(2014,1,1)) 
        
        row_where = db.select_field("value", self.__storage_table_name, where_str)
        self.assertEqual(len(row_where), 1)

    def test_write(self):
        db = ss.Db()
        db.table_delete(self.__storage_table_name)
        record = {}
        record["tag"] = "2AI001"
        record["timestamp"] =  datetime.datetime(2014, 1, 1)
        
        record["value"] = 1
        db.write(record,self.__storage_table_name,["tag","timestamp"])
        row = db.select_field("value",self.__storage_table_name)
        self.assertEqual(row[0] , 1)
        
        record["value"] = 2
        db.write(record,self.__storage_table_name,["tag","timestamp"])
        row = db.select_field("value",self.__storage_table_name)
        self.assertEqual(row[0] , 2)
        
        record["value"] = 3
        db.write(record,self.__storage_table_name,["tag","timestamp"])
        row = db.select_field("value",self.__storage_table_name)
        self.assertEqual(row[0] , 3)


    def test_ols(self):

        db=ss.Db()
        db.table_delete(self.__storage_table_name)
        start_time = datetime.datetime(2014,1,1)
        for val in range(0, 10):
            record = {}
            record["tag"] = "2AI001"
            record_time = start_time + datetime.timedelta(minutes=10*val)
            record["timestamp"] = record_time
            record["value"] = val
            db.write(record,self.__storage_table_name,["tag","timestamp"])

        for val in range(0, 10):
            record = {}
            record["tag"] = "2AI002"
            record_time = start_time + datetime.timedelta(minutes=10*val)
            record["timestamp"] = record_time
            record["value"] = val*2
            db.write(record,self.__storage_table_name,["tag","timestamp"])

        ols = st.Ols("2AI001", start_time, ["2AI002"])

        ols.fit()

        self.assertGreaterEqual(0,ols.result().params[0])



if __name__ == '__main__':
    unittest.main()

