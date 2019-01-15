import tushare as ts
#from pandas import dataframe
import pandas as pd

from _date import get_period, get_date

pro = ts.pro_api()

#[Return]   stock_info(DataFrame)
def store_stock_basic_info():
    #查询当前所有正常上市交易的股票列表
    stock_info = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    stock_info.to_csv("./data/stock_basic_info.csv" , encoding = "utf-8")

    return stock_info

#[Input]   stock_final(DataFrame)
def save_stock_final(stock_final):
    date = get_date()
    dir = f'./stock_date_final/{date}.csv'
    stock_final.to_csv(dir, encoding = "utf-8")

if __name__ == "__main__":
    #stock_info = store_stock_basic_info()
    #stock_info = stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")
    #print(stock_info)
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
    #print(stock_info.index)
    #save_stock_final(stock_info)