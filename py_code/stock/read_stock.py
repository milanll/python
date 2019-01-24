import pandas as pd
from _comm_stock import *

pd.set_option('display.max_rows',None)
pd.set_option('display.width',None)

#stock = read_stock('p-change')
stock_basic = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

#result = pd.merge(stock_final, stock_basic, how = 'inner', on = ['Unnamed: 0','ts_code', 'symbol', 'name', 'area', 'industry', 'list_date'])

if stock_basic is None:
    print ('stock is null')
else:
    pass

col_name = ('ts_code', 'symbol', 'name', 'area', 'industry',  'list_date')
stock_final = pd.DataFrame(columns = col_name)

for i, row in stock_basic.iterrows():
    row = row.drop('Unnamed: 0')
    print (row)
    df_row = pd.DataFrame([row], columns=col_name)
    print (df_row)
    break


