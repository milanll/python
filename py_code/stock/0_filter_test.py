
from _comm_stock import *
from _date import *
from _file import *
import json

x_trade_days = 20
start_date, end_date = get_x_trade_days(x_trade_days)

#0    ts_code       symbol      name        area        industry    market  list_date
#0      000001.SZ       1       平安银行     深圳       银行        主板      19910403
#1      000002.SZ       2       万科A         深圳      全国地产    主板      19910129
stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)


hist_data = {}
hist_data_dict = {}

#
def save_hist_data():
    date_str = end_date
    dir = 'E:\\git\\python\\py_code\\stock\\data\\'
    files = file_name(dir)
    
    file_json = f'hist_data_{date_str}.json'
    file_json_dir = f'./data/{file_json}'
    
    if file_json not in files:
    
        get_stock_hist_data()
        
        with open(file_json_dir, 'w') as f:
            data_dict = json.dumps(hist_data_dict)
            json.dump(data_dict, f)
            f.close()
        print('Save \'%s\' successfully!!!' % file_json)
    else:
        print('\'%s\' exsit!!!' % file_json)
    
    return        
 
#[return]   data_dict(dict)
def read_hist_data():
    file_json = f'hist_data_{end_date}.json'
    file_json_dir = f'./data/{file_json}'
    
    with open(file_json_dir, 'r') as f:
        data = json.load(f)
        data_dict = json.loads(data)
        f.close()

    #print(data_dict)
    return data_dict
 
def get_stock_hist_data():
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_p_change = pd.DataFrame(columns=col_name)
    
    print('\nget_stock_hist_data():')
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))
    
    i = 0
    for index, row in stock_basic_info.iterrows():
        code = str(row.symbol).zfill(6)
        data = ts.get_hist_data(code, start = start_date, end = end_date)
        if check_stock_data(data, x_trade_days, code) != True:
            continue
        
        hist_data[code] = data
        data = data.to_dict()
        hist_data_dict[code] = data
        
        #i += 1
        #if i > 50:
        #    break
            
    print("Get stock history data finish!!!\n")
    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))
       
    return

#[input]    key_list(list)
#[output]   stock_info(DataFrame)
def get_stock_info_by_key(key_list):
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_info = pd.DataFrame(columns=col_name)
    
    for k in key_list:
        for index, row in stock_basic_info.iterrows():
            if int(k) == int(row.symbol):
                # translate from series to dataframe
                df_row = pd.DataFrame([row], columns=col_name)
                #print(row.values)
                # append datafarme
                stock_info = stock_info.append(df_row)
                break
    
    print(stock_info)
    print (stock_info.shape[0])
    return stock_info
    
def filter_9():
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)
    
    stock_key = []
    
    print('\nfilter_9():')
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))
    
    stock_data = read_hist_data()
    
    for k, v in stock_data.items():
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        i = 0
        for index, r in v.items():
            print(r)
            i += 1
            '''
            if r.close > r.ma20 * 0.9:
                i += 1
                continue
            else:
                break
            

        if i > (len(v) * 0.9):
            stock_key.append(k)
        break
        '''
            if i > 50:
                break
    
    stock_ma = get_stock_info_by_key(stock_key)
    save_stock(stock_ma, '9_ma20')   
    
    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))

    return

if __name__ == '__main__':

    save_hist_data()
    filter_9()

