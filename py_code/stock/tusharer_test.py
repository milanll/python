import tushare as ts
import datetime
import pandas as pd
import numpy as np

#from _date import get_period

#start_date, end_date, num_week = get_period()

#ts.set_token('1b75b5ac5f9dd3aaaa43264942284efff50d34f0f87b720d4504a35e')

#pro = ts.pro_api()

#    ts_code    trade_date  open   high    low      close   pre_close  change      pct_chg      vol         amount
#    000001.SZ   20190110   9.87   10.20   9.86     10.10     9.94      0.16        1.6097      1071817.66  1079711.035
#stock_info_daily = pro.daily(ts_code = '000001.SZ', start_date = start_date, end_date = end_date)
#stock_info_week = pro.weekly(ts_code = '000001.SZ', start_date = start_date, end_date = end_date,
#               fields='ts_code,trade_date,open,high,low,close,vol,amount')

data = ts.get_hist_data('000029', start = '2019-01-01', end = '2019-03-21')
print(type(data))
print(data)











