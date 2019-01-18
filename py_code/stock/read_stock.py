import pandas as pd
from _comm_stock import *

pd.set_option('display.max_rows',None)
pd.set_option('display.width',None)

stock_amount = read_stock_amount()
#stock_basic = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

print (stock_amount[['ts_code', 'name']])
#result = pd.merge(stock_final, stock_basic, how = 'inner', on = ['Unnamed: 0','ts_code', 'symbol', 'name', 'area', 'industry', 'list_date'])
