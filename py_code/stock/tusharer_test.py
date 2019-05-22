import tushare as ts
import datetime
import pandas as pd
import numpy as np
import json

from _comm_stock import *
from _date import *

#from _date import get_period

#start_date, end_date, num_week = get_period()

#ts.set_token('1b75b5ac5f9dd3aaaa43264942284efff50d34f0f87b720d4504a35e')

#pro = ts.pro_api()

#    ts_code    trade_date  open   high    low      close   pre_close  change      pct_chg      vol         amount
#    000001.SZ   20190110   9.87   10.20   9.86     10.10     9.94      0.16        1.6097      1071817.66  1079711.035
#stock_info_daily = pro.daily_basic(ts_code = '300220.SZ', start_date = '20190101', end_date = '20190515')
#stock_info_week = pro.weekly(ts_code = '000001.SZ', start_date = start_date, end_date = end_date,
#               fields='ts_code,trade_date,open,high,low,close,vol,amount')
#print(stock_info_daily)

'''
get_hist_data()

参数说明：

code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
start：开始日期，格式YYYY-MM-DD
end：结束日期，格式YYYY-MM-DD
ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
retry_count：当网络异常后重试次数，默认为3
pause:重试时停顿秒数，默认为0

返回值说明：

date：日期
open：开盘价
high：最高价
close：收盘价
low：最低价
volume：成交量
price_change：价格变动
p_change：涨跌幅
ma5：5日均价
ma10：10日均价
ma20:20日均价
v_ma5:5日均量
v_ma10:10日均量
v_ma20:20日均量
turnover:换手率[注：指数无此项]
'''

x_trade_days = 2
start_date, end_date = get_x_trade_days(x_trade_days)

hist_data = {}

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")
'''
for index, row in stock_basic_info.iterrows():
    if '种业' in row['name'] or '农' in row['name']:
        print(row.values)
'''
print(stock_basic_info.shape[0])




