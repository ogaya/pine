# -*- coding: utf-8 -*-
import time
import random
import datetime

import simple_sql as ssql
import statistics as st

db = ssql.Db()

# 無限ループ
while True:
    # 目的変数を一つランダムに選択
    objective_tag = db.select_field("tag", "target", None, "RANDOM()", 1)

    # 説明変数の数を決める
    exp_num = random.randint(1,10)
    # 説明変数を選択
    explanatory_tags = db.select_field("tag", "tags", "Not tag='" + objective_tag[0] + "'", "RANDOM()", exp_num)

    start_time = datetime.datetime(2014, 1, 1)
   
    # 解析を行う（最小二乗法）
    print objective_tag[0]
    print explanatory_tags
    ols = st.Ols(objective_tag[0], start_time, explanatory_tags)

    if ols.can_fit() == False:
        print "解析不可能"
        continue

    ols.fit()

    # データベースに展開する
    ols.put_db()

    # 次の処理まで待ち
    time.sleep(2)
