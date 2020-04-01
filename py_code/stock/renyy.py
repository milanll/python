
from _comm_stock import *
from _date import *
from get_stock_hist_data import *

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

def renyy_0(stock_data):
    print('\nrenyy_0():')
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
        #data.iloc[-1]      #选取DataFrame最后一行，返回的是Series
        #data.iloc[-1:]     #选取DataFrame最后一行，返回的是DataFrame
        if(len(df) >= 14):
            df = df[-14:]
        else:
            print('len(df) is too short!!!\n')
            return
        
        atr = get_atr(df)
        
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        i = 0
        ma = 0
        first_close = 0
        last_close = 0
        high = 0
        low = 1000
        for index, r in df.iterrows():
            if first_close == 0:
                first_close = r.close
                
            last_close = r.close
            
            if r.close > high:
                high = r.close
                
            if r.close < low:
                low = r.close
            
            if abs(r.price_change) < (atr * 0.9):
                i += 1
				
            if r.close > r.ma5:
                ma += 1
            
        if i == 14 and ma > 7 and last_close > (first_close * 1.10) and (high - low) < 2.8 * atr:
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)
    print('''\n======================= 需求renyy =============================
		a. 当日涨幅 p_change > 5 and p_change < 9
		b. 当日成交量 volume > (v_ma10 * 1.75)
		c. 成交额 > 3亿
        ''')        
    stock_p_change = get_stock_info_by_key(stock_key)
    #save_stock(stock_p_change, 'renyy_0') 

    return
    
if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    renyy_0(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))