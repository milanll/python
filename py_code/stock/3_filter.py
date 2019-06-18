
from _comm_stock import *
from _date import *
start_date, end_date = get_x_trade_days(4)

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

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
        i = 0
        j = 0
        pre_close = 0
        for index, r in df.iterrows():
            p_change += r.p_change
            
            if r.close > min(r.open, pre_close):
                i += 1
            else:
                break
                
            if r.ma5 > r.ma10 and r.ma10 > r.ma20:
                j += 1
            else:
                break
                
            pre_close = r.close
            
        if p_change > 8 and i == 3 and j > 1:
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