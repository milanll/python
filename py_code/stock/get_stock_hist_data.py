
from _comm_stock import *
from _date import *
from _file import *
import json
import sys
import time
import os

#pd.set_option('display.width', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
#pd.set_option('max_colwidth',100)

x_trade_days = 125
start_date, end_date = get_x_trade_days(x_trade_days)

#0    ts_code       symbol      name        area        industry    market  list_date
#0      000001.SZ       1       平安银行     深圳       银行        主板      19910403
#1      000002.SZ       2       万科A         深圳      全国地产    主板      19910129
stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

import sys,time
def progress_bar(i, base):
        p = (i / base) * 100
        str = '.' * (int(p) + 1)
        #sys.stdout.write('\r[%.2f%s]%s ' % ((p), '%', str))
        sys.stdout.write('\r[ %.2f%s ]' % ((p), '%'))
        sys.stdout.flush()
        #time.sleep(0.1)

def del_hist_data():
    print('rm -rf ./data/hist_data_*')
    os.system('rm -rf ./data/hist_data_*')    
    
#[return]   file(str)  E:\\git\\python\\py_code\\stock\\data\\hist_data_2019-05-22.json 
def save_hist_data():

    dir = 'E:\\git\\python\\py_code\\stock\\data\\'
    files = file_name(dir)
    
    file_json = f'hist_data_{end_date}.json'
    file_json_dir = f'./data/{file_json}'
    
    if file_json not in files:
    
        del_hist_data()
        
        hist_data_dict = get_stock_hist_data()
        
        with open(file_json_dir, 'w') as f:
            data_dict = json.dumps(hist_data_dict)
            json.dump(data_dict, f)
            f.close()
        print('Save \'%s\' successfully!!!' % file_json)
    else:
        print('\'%s\' exsit!!!' % file_json)
    
    return  file_json_dir      

#[input]    file(str)           E:\\git\\python\\py_code\\stock\\data\\hist_data_2019-05-22.json  
#[return]   data_dict(dict)
def read_hist_data(file):
    #file_json = f'hist_data_{end_date}.json'
    #file_json_dir = f'./data/{file_json}'
    
    with open(file, 'r') as f:
        data = json.load(f)
        data_dict = json.loads(data)
        f.close()

    #print(data_dict)
    return data_dict
 
def get_stock_hist_data():
  
    print('\nget_stock_hist_data():')
    time_start = time.time()
    #print (time.asctime( time.localtime(time.time()) ))
    
    hist_data_dict = {}
    base = stock_basic_info.shape[0]

    i = 0
    j = 0
    E = 100000000
    for index, row in stock_basic_info.iterrows():
        i += 1
        code = str(row.symbol).zfill(6)
        data = ts.get_hist_data(code, start = start_date, end = end_date)
        
        #the data is wrong, discard
        if check_stock_data(data, x_trade_days, code) != True:
            continue
            
        #最近一日成交额 < 1 亿，不要
        avg_price = (data.iloc[0].high + data.iloc[0].low + data.iloc[0].open + data.iloc[0].close) / 4
        volume = data.iloc[0].volume * 100
        if (avg_price * volume) < (1.0 * E):
            continue
            
        #hist_data[code] = data
        data = data.to_dict()
        hist_data_dict[code] = data
        progress_bar(i, base)
        
        j += 1
        
        #i += 1
        #if i > 5:
            #break
            
    print("\nGet stock history data finish!!!")
    time_end = time.time()
    #print (time.asctime(time.localtime(time.time())))
    print('Cost %d S.\n' % int(time_end - time_start))
    print('Total: %d' % j)
       
    return hist_data_dict

#[input]    key_list(list)
#[output]   stock_info(DataFrame)
def get_stock_info_by_key(key_list):
    print('\n\nget_stock_info_by_key():')
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_info = pd.DataFrame(columns=col_name)
    
    base = len(key_list)
    
    i = 0
    for k in key_list:
        i += 1
        for index, row in stock_basic_info.iterrows():
            if int(k) == int(row.symbol):
                # translate from series to dataframe
                df_row = pd.DataFrame([row], columns=col_name)
                #print(row.values)
                # append datafarme
                stock_info = stock_info.append(df_row)
                break
                
        progress_bar(i, base)
    
    print('\n')
    print(stock_info)
    print (stock_info.shape[0])
    return stock_info


def get_hist_data_():
    file = save_hist_data()
    stock_data = read_hist_data(file)
    
    return stock_data
    
if __name__ == '__main__':
    stock_data = get_hist_data_()
    #print(start_date, end_date)

