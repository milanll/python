
from _comm_stock import *
from _date import *
from get_stock_hist_data import *

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

#获取成交额
#[input]	df (dataframe)	当日成交数据
#[return]	amount(int)		当日成交额
def get_amount(df):
	#open   high    close   low     vol      price_change    change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
    #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
	avg_price = (df.open + df.high + df.close + df.low) / 4
	return df.vol * 100 * avg_price

def print_filter_1_condition():
    print('''\n======================= 需求1 =============================
		a. 连续三天成交额上涨
		b. 连续三天成交量上涨
		c. 当天成交额 1 亿
        ''')    
    return
    
#[input]    stock_data(dict)
def filter_1(stock_data):
    print('\nfilter_1():%d' % len(stock_data))
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)
    
    stock_key = []
    #base = stock_basic_info.shape[0]
    base = len(stock_data)
    
    #stock_data = get_hist_data_()
    
    j = 0
    for k, v in stock_data.items():
        j += 1
        df = pd.DataFrame(v)
        #df = df.sort_index(by = "trade_date")
        df = df.sort_values(by = "trade_date")
        
        #data.iloc[-1]      #选取DataFrame最后一行，返回的是Series
        #data.iloc[-1:]     #选取DataFrame最后一行，返回的是DataFrame
        df = df.iloc[-8:]
        
        atr = get_atr(df)
        
        #       ts_code  trade_date   open   high    low    close     pre_close  change  pct_chg         vol         amount         ma5       ma_v_5        ma10      ma_v_10       ma20       ma_v_20
        #0   000001.SZ   20181011     10.05  10.16   9.70   9.86      10.45       -0.59  -5.6459         1995143.83  1994186.611    10.474    1570205.872   10.527    1344378.759   10.2365    1.068715e+06
		
        '''
        if (((df.iloc[-3].change > (-2)) and (df.iloc[-2].change > 0 and df.iloc[-2].change > df.iloc[-3].change) and (df.iloc[-1].change > df.iloc[-2].change and df.iloc[-1].change > 2))      #a. 连续三天 change > 0
            and ((df.iloc[-2].vol > df.iloc[-3].vol) and (df.iloc[-1].vol > df.iloc[-2].vol) and (df.iloc[-1].vol > df.iloc[-1].ma_v_10))   #b. 连续三天成交量上涨
            and (get_amount(df.iloc[-1]) > 1 * E )):  #c. 当天成交额 1 亿  
        '''
        if((df.iloc[-7].ma5 > df.iloc[-8].ma5)
            and (df.iloc[-6].ma5 > df.iloc[-7].ma5)
            and (df.iloc[-5].ma5 > df.iloc[-6].ma5)
            and (df.iloc[-4].ma5 > df.iloc[-5].ma5)
            and (df.iloc[-3].ma5 > df.iloc[-4].ma5)
            and (df.iloc[-2].ma5 > df.iloc[-3].ma5)
            and (df.iloc[-1].ma5 > df.iloc[-2].ma5)
            and (atr/df.iloc[-1].ma10) < 0.037):
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)

        #if j > 250:
            #break
	
    print_filter_1_condition()    
    stock_p_change = get_stock_info_by_key(stock_key)
    #save_stock(stock_p_change, '1_filter') 

    return stock_key
    
if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_1(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))