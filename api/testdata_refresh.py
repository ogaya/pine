# -*- coding: utf-8 -*-
import unittest
import statistics as st
import simple_sql as ss
import datetime
import random

storage_table_name = "storage"

db=ss.Db()

# storage初期化
db.table_delete(storage_table_name)
start_time = datetime.datetime(2014, 1, 1)

for val in range(0, 1000):
    ran = random.randint(1,100)
    ran2 = random.randint(100,200)
    ran3 = random.randint(1,100)
    print ran
    print ran2
    record = {}
    record["tag"] = "2AI001"
    record_time = start_time + datetime.timedelta(minutes=10*val)
    record["timestamp"] = record_time
    record["value"] = val
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI002"
    record["timestamp"] = record_time
    record["value"] = ran
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI003"
    record["timestamp"] = record_time
    record["value"] = 3
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI004"
    record["timestamp"] = record_time
    record["value"] = ran * 3 + val*2 -12 
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI005"
    record["timestamp"] = record_time
    record["value"] = val - ran - ran3
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI006"
    record["timestamp"] = record_time
    record["value"] = val*4*ran3
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI007"
    record["timestamp"] = record_time
    record["value"] = ran * 2 
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI008"
    record["timestamp"] = record_time
    record["value"] = ran2 * 4 - ran3
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI009"
    record["timestamp"] = record_time
    record["value"] = ran2 - 5 
    db.write(record, storage_table_name, ["tag","timestamp"])

    record["tag"] = "2AI010"
    record["timestamp"] = record_time
    record["value"] = ran2 + ran 
    db.write(record, storage_table_name, ["tag","timestamp"])


# target初期化
db.table_delete("target")

for val in range(1, 10):
    target_record = {}
    target_record["tag"] = "2AI" + "%03d"%(val)
    target_record["pattern_id"] = [0]
    db.write(target_record, "target", ["tag"])

# statistics_result初期化
db.table_delete("statistics_result")
#
#for val in range(0, 10):
#    result_record = {}
#    result_record["objective"] = "2AI001"
#    record_time = start_time + datetime.timedelta(minutes=10*val)
#    result_record["obj_time"] = record_time
#    result_record["explanatory"] = ["3AI001"]
#    result_record["exp_time"] = [start_time]
#    result_record["span"] = 240
#    result_record["f"] = 0.01 * val
#    result_record["t"] = [val,1]
#    result_record["coefficient"] = [21,20-val]
#    result_record["detail"] = ""
#    print db.convert_psql_value(result_record["objective"])
#    print db.convert_psql_value(result_record["explanatory"])
#    db.write(result_record, "statistics_result", ["objective","obj_time","explanatory","exp_time"])

# タグリスト初期化
db.table_delete("tags")
for val in range(1, 10):
    tags_record = {}
    tags_record["tag"] = "2AI" + "%03d"%(val)
    db.write(tags_record, "tags", ["tag"])




