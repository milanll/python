import tushare as ts
import datetime
import pandas as pd
import numpy as np

start_date = end_date = str(datetime.date.today())

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")
#print(type(stock_basic_info['industry']))

stock_industry = pd.Series(stock_basic_info['industry'].tolist(), index = stock_basic_info['ts_code'])

#print(stock_industry)

stock_industry_df = pd.DataFrame(columns = ['industry'])

i = 0
for index, row in stock_basic_info.iterrows():
    code = str(row.symbol).zfill(6)
    data = ts.get_hist_data(code, start=start_date, end=end_date)
    i += 1
    print(i)

    if len(data['p_change']) > 0:
        if data['p_change'][0] > 5:
            #df_row = pd.DataFrame(stock_industry[row.symbol], columns = ['industry'])
            stock_industry_df = stock_industry_df.append({'industry' : stock_industry[row.symbol]}, ignore_index=True)
    else:
        pass

print(stock_industry_df)

print(stock_industry_df.duplicated())















