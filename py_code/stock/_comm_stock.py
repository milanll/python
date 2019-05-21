import tushare as ts
import datetime
import pandas as pd
import numpy as np
import time

from _date import get_period, get_date

pro = ts.pro_api()

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
    date = get_date()
    dir = f'./stock_date_final/amount-{date}.csv'
    stock_final.to_csv(dir, encoding = "utf-8")

def save_stock_trade(trade_detail):
    date = get_date()
    dir = f'./stock_date_final/trade-{date}.csv'
    trade_detail.to_csv(dir, encoding="utf-8")

#[Return]   stock_final(DataFrame)
def read_stock_amount():
    date = get_date()
    dir = f'./stock_date_final/amount-{date}.csv'
    stock_final = pd.read_csv(dir, encoding = "utf-8")

    return stock_final

#[Return]   trade_detail(DataFrame)
def read_stock_trade():
    date = get_date()
    dir = f'./stock_date_final/trade-{date}.csv'
    trade_detail = pd.read_csv(dir, encoding = "utf-8")

    return trade_detail

#[Input]   stock_ma(DataFrame)
#          filter(str)             ma/amount/trade
def save_stock(stock_ma, filter):
    date = get_date()
    dir = f'./stock_date_final/{filter}-{date}.csv'
    stock_ma.to_csv(dir, encoding="utf-8")

#[Input]    filter(str)             ma/amount/trade
#[Return]   trade_detail(DataFrame)
def read_stock(filter):
    date = get_date()
    dir = f'./stock_date_final/{filter}-{date}.csv'
    print(dir)
    stock_ma = pd.read_csv(dir, encoding = "utf-8")

    return stock_ma

#[input]    data(DataFrame)
#           x_trade_days(int)
def check_stock_data(data, x_trade_days, code):
    if data is None:
        print('%s is None!' % code)
        return False

    if data.empty or len(data) < (x_trade_days * 0.8):
        print('%s exchange is stopped!' % (code))
        return False

    return True

#[breif]    append one record to count_grow_2_days.csv  
#[input]    date(str)       2019-05-15
#           count(int)      50
def save_count_grow_2_days(date, count):
    file = './data/count_grow_2_days.csv'
    f = pd.read_csv(file)
    if f is None:
        print('Read count_grow_2_days.csv fail!!!')
    
    df = pd.DataFrame({'Date':date, 'Count':count}, index = [len(f) + 1])
    df.to_csv(file, mode='a', header=False)
    
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
    