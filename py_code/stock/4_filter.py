
from _comm_stock import *
from _date import *
from get_stock_hist_data import *

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

#[input]     stock_data(dict)   
def filter_4(stock_data):
    print('\nfilter_4():')
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)
    
    stock_key = []
    #base = stock_basic_info.shape[0]
    base = len(stock_data)
    
    #stock_data = get_hist_data_()
    vol = 150000
    j = 0
    for k, v in stock_data.items():
        j += 1
        df = pd.DataFrame(v)
        #get the last 4 rows.
        df = df[-4:]
        
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05  
        if df['ma5'][0] < df['ma5'][1] and df['ma5'][1] < df['ma5'][2] and df['ma5'][2] < df['ma5'][3]:
            if df['ma5'][2] > df['ma10'][2] > df['ma20'][2]:
                if df['volume'][0] > vol and df['volume'][1] > vol and df['volume'][2] > vol and df['volume'][3] > vol:
                    stock_key.append(k)
                    progress_bar(j, base)
                    
    stock_ma = get_stock_info_by_key(stock_key)
    #save_stock(stock_ma, '4_filter') 

if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_4(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))