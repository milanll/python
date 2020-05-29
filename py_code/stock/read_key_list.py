
from get_stock_hist_data import *
import pandas as pd
from _date import *
from filter_1 import *
from filter_2 import *
from filter_3 import *
from filter_4 import *
from filter_5 import *
from filter_6 import *
from filter_7 import *
from filter_9 import *

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
        print_filter_1_condition()
    elif 'filter_2' == key: 
        print_filter_2_condition()
    elif 'filter_3' == key: 
        print_filter_2_condition()
    elif 'filter_4' == key:  
        print_filter_3_condition()
    elif 'filter_5' == key:   
        print_filter_5_condition()
    elif 'filter_6' == key:
        print_filter_6_condition()
    elif 'filter_7' == key:    
        print_filter_7_condition()
    elif 'filter_8' == key:
        print_filter_8_condition()
    elif 'filter_9' == key:  
        print_filter_9_condition()
    else:
        print('filter wrong!!!\n')
        
    return   

def read_key_list(file_name):
    key_list_dict = read_hist_data(file_name)

    for k, v in key_list_dict.items():
        print_condition(k)
        get_stock_info_by_key(v)

if __name__ == '__main__':
    file_name = get_key_list_file_name()
    read_key_list(file_name)
    

