
from _comm_stock import *
from _date import *
start_date, end_date = get_x_trade_days(4)

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

def get_stock_by_strategy(code):
    # open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
    # 10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
    data = ts.get_hist_data(code, start = start_date, end = end_date)
    if data is None:
        return None

    i = 0
    for index, r in data.iterrows():
        #type(r.p_change) is numpy.float64
        i += r.p_change

    if i < -15:
        return True

    return False

from get_stock_hist_data import *
def filter_3(stock_data):
    print('\nfilter_3():')
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)
    
    stock_key = []
    #base = stock_basic_info.shape[0]
    base = len(stock_data)
      
    j = 0
    for k, v in stock_data.items():
        j += 1
        df = pd.DataFrame(v)
        #data.iloc[-1]   #选取DataFrame最后一行，返回的是Series
        #data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame
        df = df[-3:]
        
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        p_change = 0
        for index, r in df.iterrows():
            p_change += r.p_change
            
        if p_change > 15:
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)

            
    stock_p_change = get_stock_info_by_key(stock_key)
    #save_stock(stock_p_change, '3_filter') 

    return

if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_3(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))