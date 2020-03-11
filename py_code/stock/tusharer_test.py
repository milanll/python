import tushare as ts
import datetime
import pandas as pd
import numpy as np
import json

from _comm_stock import *
from _date import *
from get_stock_hist_data import *

#ts.set_token('1b75b5ac5f9dd3aaaa43264942284efff50d34f0f87b720d4504a35e')

#pd.set_option('display.width', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
#pd.set_option('max_colwidth',100)
#不换行
pd.set_option('display.width',1000)

'''
深市A股票代码以000大头
中小板股票代码以002打头
创业板股票代码以300打头
'''
'''
沪市A股票买卖的代码是以600、601或603打头
'''
def basic_info():
    pro = ts.pro_api()
    
    '''
    名称	        类型	    描述
    ts_code	        str	        TS股票代码
    trade_date	    str	        交易日期
    close	        float	    当日收盘价
    turnover_rate	float	    换手率
    turnover_rate_f	float	    换手率（自由流通股）
    volume_ratio	float	    量比
    pe	            float	    市盈率（总市值/净利润）
    pe_ttm	        float	    市盈率（TTM）
    pb	            float	    市净率（总市值/净资产）
    ps	            float	    市销率
    ps_ttm	        float	    市销率（TTM）
    total_share	    float	    总股本 （万）
    float_share	    float	    流通股本 （万）
    free_share	    float	    自由流通股本 （万）
    total_mv	    float	    总市值 （万元）
    circ_mv	        float	    流通市值（万元）
    '''
    stock_info_daily = pro.daily_basic(ts_code = '000063.SZ', start_date = '20190101', end_date = '20190515')
    #print(stock_info_daily.head(5))
    
    
    #    ts_code    trade_date  open   high    low      close   pre_close  change      pct_chg      vol         amount
    #    000001.SZ   20190110   9.87   10.20   9.86     10.10     9.94      0.16        1.6097      1071817.66  1079711.035
    stock_daily = pro.daily(ts_code = '000063.SZ', start_date = '20190501', end_date = '20190617')
    print(stock_daily.head(5))
    print(get_atr(stock_daily))
    
    #stock_info_week = pro.weekly(ts_code = '000001.SZ', start_date = start_date, end_date = end_date,
    #               fields='ts_code,trade_date,open,high,low,close,vol,amount')
    #print(stock_info_daily)

def test_hist_data():
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

    d = ts.get_hist_data('000001', start = '2020-01-03' , end = '2020-03-04')
    d = d.sort_index()

    print(d)

def test(stock_data):
    print('\ntest():')
    
    stock_key = []
    #base = stock_basic_info.shape[0]
    base = len(stock_data)
      
    j = 0
    for k, v in stock_data.items():
        j += 1
        df = pd.DataFrame(v)
        
        if df.iloc[0].close < df.iloc[-1].close:
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)
            
    stock_p_change = get_stock_info_by_key(stock_key) 

    return

if __name__ == '__main__':
    #stock_data = get_hist_data_()
    #test(stock_data)
	test_hist_data()



