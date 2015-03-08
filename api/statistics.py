# -*- coding: utf-8 -*-
import numpy as np
import statsmodels.api as sm
import simple_sql as ss
import datetime as dt

class Ols():
    __storage_table_name = "storage"
    __result_table_name = "statistics_result"
    __result_table_key = ["objective", "obj_time", "explanatory", "exp_time", "span"]
    __storage_field_value = "value"

    __corr_table_name = "correlation"
    __corr_table_key = ["x","x_time","y","y_time"]
    # 目的変数
    __objective = ""
    # 目的変数の時間帯 
    __obj_time = dt.datetime.now()
    # 説明変数
    __explanatory = []
    # 説明変数のデータ時間
    __exp_time = []
    # 時間幅
    __span = 60*60*24
    # 演算結果
    __result = None
    # 相関係数
    __corr = None

    __obj_record = None
    __exp_record = None

    # コンストラクタ
    def __init__(self, objective="", obj_time=None, explanatory=[]):
        self.__objective = objective
        self.__obj_time = obj_time
        self.__explanatory = explanatory

        exp_len = len(self.__explanatory)

        if exp_len == 0:
            return

        exp_time_len = len(self.__exp_time)
        if exp_time_len < exp_len:
            for val in range(exp_time_len, exp_len):
                self.__exp_time.append(self.__obj_time)

        self.__get_dbrecord()
        self.__solve_coff()


    def __get_dbrecord(self):
        db = ss.Db()
        obj_condition = "tag=" + db.convert_psql_value(self.__objective)
        self.__obj_record = db.select_field(self.__storage_field_value, self.__storage_table_name, obj_condition, "timestamp")
        exp_record = None
        for i in range(0, len(self.__explanatory)):
            exp_condition = "tag=" + db.convert_psql_value(self.__explanatory[i])

            tmp = db.select_field(self.__storage_field_value, self.__storage_table_name, exp_condition,"timestamp")
            self.__exp_record = tmp if self.__exp_record is None else np.c_[self.__exp_record, tmp]

    def fit(self):
        exp_record_add_constant = sm.add_constant(self.__exp_record)
        model = sm.OLS(self.__obj_record, exp_record_add_constant)
        self.__result = model.fit()

    def __solve_coff(self):
        self.__corr = np.corrcoef(self.__exp_record.T)
        print self.__corr
        self.__put_db_corr();

    # fit可能か
    def can_fit(self):
        # 相関係数が算出不能（NAN）の場合、最小二乗法不可能
        if np.isnan(self.__corr).any():
            return False

        if self.__corr.size == 1:
            return True

        size = self.__corr[self.__corr > 0.95].size
        column  = self.__corr.shape[0]
        if size > column:
            return False

        return True

    # 結果取得
    def result(self):
        return self.__result

    def corr(self):
        return self.__corr

    # データベースへ出力
    def put_db(self):
        self.__put_db_result();

    def __put_db_result(self):
        record = {}
        record["objective"] = self.__objective
        record["obj_time"] = self.__obj_time
        record["explanatory"] = self.__explanatory
        record["exp_time"] = self.__exp_time
        record["span"] = self.__span

        record["r_squared"] = self.__result.rsquared
        record["t"] = self.__result.tvalues
        record["coefficient"] = self.__result.params
        record["detail"] = ""
        
        db = ss.Db()
        db.write(record, self.__result_table_name, self.__result_table_key) 

    def __put_db_corr(self):
        
        if self.__corr.size == 1:
            return

        if np.isnan(self.__corr).any():
            return

        record = {}
        record["x"] = self.__explanatory[0]
        record["x_time"] = self.__exp_time[0]
        record["y"] = self.__explanatory[1]
        record["y_time"] = self.__exp_time[1]
        record["val"] = self.__corr[0][1]
        
        db = ss.Db()
        db.write(record, self.__corr_table_name, self.__corr_table_key) 


