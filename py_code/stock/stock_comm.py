import tushare as ts
#from pandas import dataframe

pro = ts.pro_api()

def store_stock_basic_info():
    #查询当前所有正常上市交易的股票列表
    stock_info = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    stock_info.to_csv("./data/stock_basic_info.csv" , encoding = "utf-8")

    return stock_info

if __name__ == "__main__":
    stock_info = store_stock_basic_info()
    print(stock_info)