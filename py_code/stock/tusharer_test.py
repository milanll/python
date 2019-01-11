import tushare as ts
import datetime
import pandas as pd
import numpy as np

from _date import get_period

start_date, end_date, num_week = get_period()

pro = ts.pro_api()

#    ts_code    trade_date  open   high    low      close   pre_close  change      pct_chg      vol         amount
#    000001.SZ   20190110   9.87   10.20   9.86     10.10     9.94      0.16        1.6097      1071817.66  1079711.035
#stock_info_daily = pro.daily(ts_code = '000001.SZ', start_date = start_date, end_date = end_date)
stock_info_week = pro.weekly(ts_code = '000001.SZ', start_date = start_date, end_date = end_date,
               fields='ts_code,trade_date,open,high,low,close,vol,amount')

amount_avr_1 = 0
amount_avr_2 = 2
amount_1 = []
amount_2 = []
len_amount = 0

# len of rows
len_amount = stock_info_week.shape(0)
print(len_amount)
print(stock_info_week.values)
for index, row in stock_info_week.iterrows():
	if index < len_amount * 1/3:
		amount_1.append(row.amount)
	else:
		amount_2.append(row.amount)

amount_avr_1 = np.mean(tuple(amount_1))
amount_avr_2 = np.mean(tuple(amount_2))

print(len(amount_1), amount_avr_1, len(amount_2), amount_avr_2)










