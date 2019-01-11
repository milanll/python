
import tushare as ts
import datetime
import pandas as pd
import numpy as np

from _date import get_period

# ts.set_token('1b75b5ac5f9dd3aaaa43264942284efff50d34f0f87b720d4504a35e')
pro = ts.pro_api()

start_date, end_date, num_week = get_period()

global g_num
g_num = 0

def get_final_stock():
    stock_final = {}
    stock_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

    #      Unnamed: 0   ts_code     symbol  name        area    industry  list_date
    #              0    000001.SZ      1    平安银行     深圳       银行    19910403

    for index, row in stock_info.iterrows():
        if analyse_stock_by_week(row.ts_code):
            stock_final.update({row.ts_code:row})




#[Return]   True    wanted
#           False   not wanted
def analyse_stock_by_day(ts_code):
    amount_avr_1 = 0
    amount_avr_2 = 0
    amount_1 = []
    amount_2 = []
    len_amount = 0

    g_num += 1

    #    ts_code    trade_date  open   high    low      close   pre_close  change      pct_chg      vol         amount
    #    000001.SZ   20190110   9.87   10.20   9.86     10.10     9.94      0.16        1.6097      1071817.66  1079711.035
    stock_info_daily = pro.daily(ts_code = ts_code, start_date = start_date, end_date = end_date)

    #len of rows
    len_amount = stock_info_daily.shape[0]
    if num_week < len_amount:
        for index, row in stock_info_daily.iterrows():
            if index < len_amount * 1/3:
                amount_1.append(row.amount)
            else:
                amount_2.append(row.amount)

        amount_avr_1 = np.mean(tuple(amount_1))
        amount_avr_2 = np.mean(tuple(amount_2))

    if  amount_avr_1 > (amount_avr_2 * 1.5):
        return True
    else:
        return False

#[Return]   True    wanted
#           False   not wanted
def analyse_stock_by_week(ts_code):
    amount_avr_1 = 0
    amount_avr_2 = 0
    amount_1 = []
    amount_2 = []
    len_amount = 0
    global g_num
    g_num += 1

    stock_info_week = pro.weekly(ts_code = ts_code, start_date = start_date, end_date = end_date,
               fields='ts_code,trade_date,open,high,low,close,vol,amount')

    #len of rows
    len_amount = stock_info_week.shape[0]
    for index, row in stock_info_week.iterrows():
        if index < 3:
            amount_1.append(row.amount)
        else:
            amount_2.append(row.amount)

    amount_avr_1 = np.mean(tuple(amount_1))
    amount_avr_2 = np.mean(tuple(amount_2))

    print(g_num, ts_code, len(amount_1), amount_avr_1, len(amount_2), amount_avr_2)

    if  amount_avr_1 > (amount_avr_2 * 1.5):
        return True
    else:
        return False

if __name__ == "__main__":
    get_final_stock()
    
    print(stock_final.keys())
    print(len(stock_final))