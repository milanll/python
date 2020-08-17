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

    #x_trade_days = 2
    #start_date, end_date = get_x_trade_days(x_trade_days)

    #d = ts.get_hist_data('600438', start = '2020-03-24' , end = '2020-03-31')
    d = ts.get_hist_data('300194', start = '2020-03-30' , end = '2020-04-03')
    d = d.sort_index()

    print(get_atr(d))
    print(get_average_close(d))
    print(get_atr(d) / get_average_close(d))


    


def art_():
    d = ts.get_hist_data('300454', start = '2020-07-01' , end = '2020-07-10')
    print(d)
    atr = get_atr(d)
    print(atr, atr/d.iloc[0].close)

#统计5天ATR分布    
def atr_statistics(stock_data):
    print('\nrenyy_0():')
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)
    
    stock_key = []
    #base = stock_basic_info.shape[0]
    base = len(stock_data)
    
    j = 0
    atr_01 = 0
    atr_02 = 0
    atr_03 = 0
    atr_04 = 0
    atr_05 = 0
    atr_06 = 0
    atr_07 = 0
    atr_08 = 0
    atr_09 = 0
    atr_10 = 0
    atr_11 = 0
    atr_12 = 0
    atr_13 = 0
    atr_14 = 0
    
    for k, v in stock_data.items():
        j += 1
        df = pd.DataFrame(v)
        #data.iloc[-1]      #选取DataFrame最后一行，返回的是Series
        #data.iloc[-1:]     #选取DataFrame最后一行，返回的是DataFrame
        
        if(len(df) >= 5):
            df = df[-5:]
        else:
            print('len(df) is too short!!!\n')
            return
        
        atr = get_atr(df)
        
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        i = 0
        ma = 0
        first_close = 0
        last_close = 0
        high = 0
        low = 1000
        sum_close = 0
        avg_close = 0
        atr_rate = 0

        for index, r in df.iterrows():
            i += 1
            sum_close += r.close
        
        avg_close = sum_close/i
        atr_rate = atr/avg_close
        
        if atr_rate < 0.01:
            atr_01 += 1
        elif atr_rate < 0.02:
            atr_02 += 1
        elif atr_rate < 0.03:
            atr_03 += 1
        elif atr_rate < 0.04:
            atr_04 += 1
        elif atr_rate < 0.05:
            atr_05 += 1
        elif atr_rate < 0.06:
            atr_06 += 1
        elif atr_rate < 0.07:
            atr_07 += 1
        elif atr_rate < 0.08:
            atr_08 += 1
        elif atr_rate < 0.09:
            atr_09 += 1
        elif atr_rate < 0.1:
            atr_10 += 1
        elif atr_rate < 0.11:
            atr_11 += 1    
        elif atr_rate < 0.12:
            atr_12 += 1
        elif atr_rate < 0.13:
            atr_13 += 1 
        else:
            atr_14 += 1
        
        stock_key.append(k)
        #print(k)
        progress_bar(j, base)
    print('''\n======================= 需求renyy =============================
		a. 5日内价格中枢整体抬升。最后一天价格中枢大于第一天。
        b. 偏离平均价格中枢的最大值，小于一定比例，待定。

        ''') 
        
    print(atr_01)
    print(atr_02)
    print(atr_03)
    print(atr_04)
    print(atr_05)
    print(atr_06)
    print(atr_07)
    print(atr_08)
    print(atr_09)
    print(atr_10)
    print(atr_11)
    print(atr_12)
    print(atr_13)
    print(atr_14)
    return    

def test():
    #    ts_code     trade_date  open  high     low  close      pre_close  change  pct_chg      vol         amount      ma5     ma_v_5      ma10        ma_v_10     ma20      ma_v_20
    #1   600157.SH   20200811    1.39  1.43     1.38   1.38       1.39      -0.01  -0.7194      2159391.85  303472.626  1.382   1739221.142  1.371      1555656.944  1.3540  1413549.894
    #0   600157.SH   20200812    1.37  1.42     1.36   1.41       1.38      0.03   2.1739       1881561.60  259874.204  1.390   1888087.140  1.379      1653376.382  1.3560  1418746.485
    df = ts.pro_bar(ts_code='600157.SH', adj='qfq', start_date='20200713', end_date='20200812', ma = [5,10,20])
    df = df.sort_values(by = "trade_date")
    #print(df)
    
    atr = get_atr(df)
    print((atr/df.iloc[-1].ma10).round(3))
    
if __name__ == '__main__':
    #stock_data = get_hist_data_()
    test()
    


