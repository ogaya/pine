# -*- coding: utf-8 -*-
import numpy as np
import psycopg2 as pg2
from psycopg2.extras import RealDictCursor
import datetime
import json

# JSON変換に対応していない型を変換する
def support_datetime_default(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()
    raise TypeError(repr(o) + " is not JSON serializable")

class Db():
    __dbname=""
    __host=""
    __user=""
    __table_name="product"

    def __init__(self, dbname="sample", host="localhost", user="postgres"):

        self.__dbname = dbname
        self.__host = host
        self.__user = user

    # アクセスパスを生成
    def __connect_path(self):
        return "dbname="+self.__dbname+" host="+self.__host+" user="+self.__user

    # pythonのデータをSQLに格納可能な形に変更
    def convert_psql_value(self, value, ea = "'"):
        if type(value) is datetime.datetime:
            return ea + value.strftime("%Y/%m/%d %H:%M") + ea
        
        if type(value) is int:
            return str(value)
        if type(value) is float:
            return str(value)

        if type(value) is str:
            return ea + value + ea 

        if type(value) is list or type(value) is np.ndarray:
            listval = ""
            for val in value:
                v = self.convert_psql_value(val,"\"")
                listval = v if listval == '' else listval + "," + v
            listval = "'{" + listval + "}'"
            return listval

        txt = str(value)
        
        return ea + txt + ea

    # select文を生成
    def get_select_sql(self, field, table, condition=None, order=None, limit=1000, direction="ASC"):
        field = "*" if field is None else field 
        table_name = self.__table_name if table is None else table
    
        # 条件
        where_str = "" if condition is None else " Where " + condition + " " 
   
        # 順序
        order_str = "" if order is None else " order by " + order + " " + direction + " "

        # 検索上限
        limit_str = "" if limit is None else " limit " + str(limit) + " "

        # select文
        return "SELECT " + field + " FROM " + table_name + where_str + order_str + limit_str + ";"

    # JSON形式でデータ取得
    def select_json(self, field, table, condition=None, order=None, limit=100, direction="ASC"):
        
        # データベース接続
        conn = pg2.connect(self.__connect_path())
        #cur = conn.cursor()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        select_sql = self.get_select_sql(field, table, condition, order, limit, direction) 

        cur.execute(select_sql)
        value = json.dumps(cur.fetchall(), indent=2, default=support_datetime_default)
       
        cur.close()
        conn.close()

        return value

    def select_field(self, field, table, condition=None, order=None, limit=1000, direction="ASC"):
    
        row_data = np.array([])
        
        # データベース接続
        conn = pg2.connect(self.__connect_path())
        cur = conn.cursor()

        select_sql = self.get_select_sql(field, table, condition, order, limit, direction) 
        cur.execute(select_sql)
    
        for row in cur:
            row_data = np.append(row_data, row)
       
        cur.close()
        conn.close()
    
        return row_data
  
    # データ書き込み(insert and update)
    def write(self, vals, table, key):

        conn = pg2.connect(self.__connect_path())
        cur = conn.cursor()

        self.__insert(cur, vals, table, key)
        self.__update(cur, vals, table, key)

        conn.commit()
        cur.close()
        conn.close()

    # データ追加
    def __insert(self, cur, vals, table, key):
        table_field =""
        select_field = ""

        for k,v in vals.items():
            val = self.convert_psql_value(v)
            table_field = k if table_field == '' else table_field + "," + k
            select_field = val if select_field == '' else select_field + "," + val 

        key_field=""
        for k in key:
            val = self.convert_psql_value(vals[k])
            key_field = k + "=" + val \
                    if key_field == '' else key_field + " and " + k + "=" + val 

        cur.execute("INSERT INTO " + table + " (" + table_field + ") "+
                "SELECT " + select_field + " WHERE NOT EXISTS ( SELECT 1 FROM " +
                table + " WHERE " + key_field + " )")

    # データ更新
    def __update(self, cur, vals, table, key):
 
        update_field = ""
        for k,v in vals.items():
            val = self.convert_psql_value(vals[k])
            update_field = k + "=" +  val if update_field == '' else update_field + "," + k + "=" + val

        key_field=""
        for k in key:
            val = self.convert_psql_value(vals[k])
            key_field = k + "=" + val if key_field == '' else key_field + " and " + k + "=" + val 

        cur.execute("UPDATE " + table + " set " + update_field + " WHERE " + key_field)

    # テーブルの情報削除（dropではない）   
    def table_delete(self,table):
   
        table_name = self.__table_name if table is None else table
        conn = pg2.connect(self.__connect_path())
        cur = conn.cursor()

        cur.execute("DELETE FROM " + table_name + ";")

        conn.commit()
        cur.close()
        conn.close()

    # テーブル作成
    def create_table(self, table):
 
        table_name = self.__table_name if table is None else table
        conn = pg2.connect(self.__connect_path())
        cur = conn.cursor()

        cur.execute("DELETE FROM " + table_name + ";")

        conn.commit()
        cur.close()
        conn.close()

