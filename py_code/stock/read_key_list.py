
from get_stock_hist_data import *
import pandas as pd
from _date import *

def get_key_list_file_name():
    start_date, end_date = get_x_trade_days(x_trade_days)
    print('\nstart_date: %s\nend_date: %s\n' % (start_date, end_date))
    
    file_json = f'key_list_{end_date}.json'
    file_name = f'./sync_data/{file_json}'
    
    import platform 
    sys = platform.system()
    if sys == "Windows":
        file_name = f'./sync_data/{file_json}'
    elif sys == "Linux":
        file_name = f'./sync_data/{file_json}'
    else:
        print('unknwn OS!!\n')
        
    return file_name    

#[breif]    print condition by key
#[input]    key(str)    'filter_1'
def print_condition(key):
    
    if 'filter_1' == key:
        print('''
1.根据成交价和成交量选股

    需求：a. 当日涨幅 p_change > 5
          b. 当日成交量 volume > (v_ma10 * 3)
''')
    elif 'filter_2' == key: 
        print('''
2.根据日涨幅和日成交量选股

    需求：a. 连续3天，累计涨幅超20%。
''')
    elif 'filter_3' == key: 
        print('''
3.根据涨幅选股

    需求：  a. 三天涨幅超过10%
            b. 收盘价 > 开盘价
            c. 每天ma5 > ma10 > ma20
        ''')
    elif 'filter_4' == key:  
        print('''
4.横向比较选股

    需求:   
            a. 连续5天，ma5 > ma10 > ma20
            b. 每天成交额大于1亿
        ''')
    elif 'filter_5' == key:   
        print('''
5.过去5个交易日中，有三个涨停板。

    需求：a.过去5个交易日中，有三个涨停板
''')
    elif 'filter_6' == key:
        print('''
6.日均线反转。
    
    py文件：6_filter.py
    需求：a.当日ma5 > ma10 and ma5 > ma20
          b.前一日ma5 < ma10 < ma20
          c.成交额大于2亿
      ''')
    elif 'filter_7' == key:    
        print('''
7.连续3天涨幅大于2%。
    
    需求：a.连续3天涨幅大于2%
    ''')
    elif 'filter_8' == key:
        print('''
8.持仓股票
    py文件：8_filter.py
    需求：a. 计算止损点
          b. 计算止盈点
          ''')
    elif 'filter_9' == key:  
        print('''
9.连续20个交易日，收盘价在ma20以上  

    需求：连续20个交易日，收盘价在ma20以上
    ''')
    else:
        print('filter wrong!!!\n')
        
    return    

if __name__ == '__main__':
    file_name = get_key_list_file_name()
    print(file_name)

    key_list_dict = read_hist_data(file_name)

    for k, v in key_list_dict.items():
        print_condition(k)
        get_stock_info_by_key(v)

