# -*- coding: UTF-8 -*- 
import tushare as ts
from _comm_stock import *
from _date import *
import sys

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

g_stock_str = '600536 中国软件 400 400 72.983 71.550 28620.000 -573.040 -1.964 上海A股 '

g_stock_buy = {'中兴通讯':['000063', 33.515], '士兰微':['600460', 15.492], '市北高新':['600604', 12.499]}

#[breif]    返回持仓股票的代码列表，原始表格手动更改
#[input]    void
#[return]   stock_code(list)    ['000001.SZ', '600666.SH']
def get_stock_code():
    code = ['300399','000063']
    stock_code = []
    '''
    深市A股票代码以000大头
    中小板股票代码以002打头
    创业板股票代码以300打头

    沪市A股票买卖的代码是以600、601或603打头
    
    跨市场股票ETF业务分配515000-515999代码段
    '''
    for c in code:
        assert(len(c) == 6)
        
        if c[0:3] == '000' or c[0:3] == '002' or c[0:3] == '300':
            stock_code.append(c + '.SZ')
        elif c[0:3] == '600' or c[0:3] == '601' or c[0:3] == '603':
            stock_code.append(c + '.SH')
        else:
            print('stock code error!')
            
    #print(stock_code)
    return stock_code

#[breif]    对字符串股票信息进行解析，将不同参数解析出来，并装入相应格式中。
#[input]    stock_str(str)      '600536 中国软件 400 400 72.983 71.550 28620.000 -573.040 -1.964 上海A股 '
#[return]   stock_info(list)    ['600536', '中国软件', '400', '400', '72.983', '71.550', '28620.000', '-573.040', '-1.964', '上海A股', '']
def format_stock_info(stock_str):
    stock_info = []
    if len(stock_str) < 50:
        print("The stock infomation you input is wrong!!!\n")
        sys.exit()
        
    stock_info = stock_str.split(' ')
  
    return stock_info    

#[breif]    将控制台输入的参数，整理并装入相应格式中。
#[input]    stock_str(str)      600536 中国软件 400 400 72.983 71.550 28620.000 -573.040 -1.964 上海A股 
#[return]   stock_info(list)    ['600536', '中国软件', '400', '400', '72.983', '71.550', '28620.000', '-573.040', '-1.964', '上海A股', '']
def get_input_param():
    stock_info = []
    
    if len(sys.argv) < 6:
        print("\n[Error]:Please input correct stock infomation as follow:")
        print('py 8_filter.py 600536 中国软件 400 400 72.983 71.550 28620.000 -573.040 -1.964 上海A股\n')
        sys.exit()
    
    for v in sys.argv:
        if sys.argv.index(v) == 0:
            continue
            
        stock_info.append(v)
    
    return stock_info

#[breif]    计算该股票一段时间内的ATR    
#[input]    stock(list)             ['600536', '中国软件', '400', '400', '72.983', '71.550', '28620.000', '-573.040', '-1.964', '上海A股', '']
#[return]   atr(int)
def get_atr_by_code(stock):
    exchange_data = {}
    start_date, end_date = get_x_trade_days(20)
    
    exchange_data = ts.get_hist_data(stock[0], start = start_date, end = end_date)
    
    atr = get_atr(exchange_data)
    
    return atr

#[input]    atr(int)
#           stock_info(list)    ['600536', '中国软件', '400', '400', '72.983', '71.550', '28620.000', '-573.040', '-1.964', '上海A股', '']
def calc_stock_operate_point(stock_info, atr):
    cost = float(stock_info[4])

    print('\n%-6s   atr: %.2f     止损点: %.2f     止盈点: %.2f' % (stock_info[1], atr, (cost - atr * 0.5), (cost + atr * 1.5)))

if __name__ == '__main__':
    #stock_info = format_stock_info(str)
    stock_info = get_input_param()
    atr = get_atr_by_code(stock_info)
    calc_stock_operate_point(stock_info, atr)
    
    
    

