
from _comm_stock import *
from _date import *
#start_date, end_date = get_x_trade_days(4)

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

E = 100000000
W = 10000

from get_stock_hist_data import *
def filter_3(stock_data):
    
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
        
        atr = get_atr(df)
        
        #data.iloc[-1]   #选取DataFrame最后一行，返回的是Series
        #data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame
        d = df[-3:]
        
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        p_change = 0
        i = 0
        ma = 0
        pre_close = df.iloc[-4].close
        for index, r in d.iterrows():
            
            #波动幅度不能太大
            if (r.high - r.close) > atr:
                break
            
            #涨幅不能太小
            if r.p_change < 0.6:
                break
                
            #累计涨幅
            p_change += r.p_change
            
            #大于开盘价，或者大于前一日收盘价
            if r.close > min(r.open, pre_close):
                i += 1
            else:
                break
                
            if r.ma5 > r.ma10 and r.ma10 > r.ma20:
                ma += 1
            else:
                break

            pre_close = r.close
                
        if (p_change > 6 
            and i == 3 
            #成交额大于2亿
            and ((d.iloc[-1].close * d.iloc[-1].volume * 100) > 2 * E)):
            
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)

    print('''\n======================= 需求3 =============================  
            a. 三天涨幅超过10%
            b. 收盘价 > 开盘价
            c. 每天ma5 > ma10 > ma20\n''')        
    stock_p_change = get_stock_info_by_key(stock_key)
    #save_stock(stock_p_change, '3_filter') 

    return stock_key

if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_3(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))