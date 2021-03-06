import tushare as ts
import datetime
import pandas as pd
import numpy as np
import time

from _date import get_period, get_trade_date

pro = ts.pro_api()

E = 100000000

#[Return]   stock_info(DataFrame)
def store_stock_basic_info():
    print('\nstore_stock_basic_info():')
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))
    
    #查询当前所有正常上市交易的股票列表
    stock_info = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,market,list_date')
    stock_info.to_csv("./data/stock_basic_info.csv" , encoding = "utf-8")
    
    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))

    return stock_info

#[Input]   stock_final(DataFrame)
def save_stock_amount(stock_final):
    date = get_trade_date()
    dir = f'./stock_date_final/amount-{date}.csv'
    stock_final.to_csv(dir, encoding = "utf-8")

def save_stock_trade(trade_detail):
    date = get_trade_date()
    dir = f'./stock_date_final/trade-{date}.csv'
    trade_detail.to_csv(dir, encoding="utf-8")

#[Return]   stock_final(DataFrame)
def read_stock_amount():
    date = get_trade_date()
    dir = f'./stock_date_final/amount-{date}.csv'
    stock_final = pd.read_csv(dir, encoding = "utf-8")

    return stock_final

#[Return]   trade_detail(DataFrame)
def read_stock_trade():
    date = get_trade_date()
    dir = f'./stock_date_final/trade-{date}.csv'
    trade_detail = pd.read_csv(dir, encoding = "utf-8")

    return trade_detail

#[Input]   stock_info(DataFrame)
#          sub_name(str)             ma/amount/trade
def save_stock(stock_info, sub_name):
    date = get_trade_date()
    dir = f'./stock_date_final/{sub_name}-{date}.csv'
    stock_info.to_csv(dir, encoding="utf-8")

#[Input]    sub_name(str)             ma/amount/trade
#[Return]   trade_detail(DataFrame)
def read_stock(sub_name):
    date = get_trade_date()
    dir = f'./stock_date_final/{sub_name}-{date}.csv'
    print(dir)
    stock_info = pd.read_csv(dir, encoding = "utf-8")

    return stock_info

#[input]    data(DataFrame)
#           x_trade_days(int)
def check_stock_data(data, x_trade_days, code):
    if data is None:
        #print('%s is None!' % code)
        return False

    if data.empty or len(data) < (x_trade_days * 0.8):
        #print('%s exchange is stopped!' % (code))
        return False

    return True

#[input]    stock_info(DataFrame)
#[return]   atr(int)
def get_atr(stock_info):
    atr = 0
    n_atr = 0
    #assert(len(stock_info) == 14)
    if len(stock_info) > 14:
        stock_info = stock_info[0:14]
    
    '''
    ATR定义：
    1.TR=∣最高价-最低价∣ 和 ∣最高价-昨收∣ 和 ∣昨收-最低价∣ 的最大值
        =max(∣H-L∣,∣H-PC∣,∣PC-L∣)
    2.真实波幅（ATR）= TR的N日简单移动平均
    3.参数N设置为14日
    '''
    pre_close = 0
    
    #    ts_code     trade_date  open  high     low  close      pre_close  change  pct_chg      vol         amount      ma5     ma_v_5      ma10        ma_v_10     ma20      ma_v_20
    #1   600157.SH   20200811    1.39  1.43     1.38   1.38       1.39      -0.01  -0.7194      2159391.85  303472.626  1.382   1739221.142  1.371      1555656.944  1.3540  1413549.894
    #0   600157.SH   20200812    1.37  1.42     1.36   1.41       1.38      0.03   2.1739       1881561.60  259874.204  1.390   1888087.140  1.379      1653376.382  1.3560  1418746.485
    for index, v in stock_info.iterrows():
        if pre_close == 0:
            pre_close = v.close
            continue
             
        m = max(abs(v.high - v.low), abs(v.high - pre_close), abs(pre_close - v.low))
        #print(index, m)
        atr += m
        n_atr += 1
        
        pre_close = v.close
    
    atr = atr / n_atr
    #print(atr)
    
    return round(atr, 2)
 
#[input]    stock_info(DataFrame)
#[return]   average_close(int)
def get_average_close(stock_info):
    sum_close = 0

    for index, v in stock_info.iterrows():
        sum_close += v.close
    
    average_close = sum_close / len(stock_info)
    return round(average_close, 2)
    
if __name__ == "__main__":
    '''
    #    A  B  C
    # x  1  2  3
    # y  4  5  6
    # z  7  8  9
    
    # 选取index='x', column='A'的值为1的元素，
    df.iloc[0][0]
    df.loc['x']['A']
    df.at['x','A']
    df.iat[0,0]
    df.get_value('x', 'A')
    '''
    #save_count_grow_2_days('2019-05-13', 20)
    store_stock_basic_info()
    