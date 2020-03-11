
from _comm_stock import *
from _date import *
from get_stock_hist_data import *

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

#获取成交额
#[input]	df (dataframe)	当日成交数据
#[return]	amount(int)		当日成交额
def get_amount(df):
	#open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
    #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
	avg_price = (df.open + df.high + df.close + df.low) / 4
	return df.volume * 100 * avg_price
	
def filter_1(stock_data):
    print('\nfilter_1():')
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
        #data.iloc[-1]      #选取DataFrame最后一行，返回的是Series
        #data.iloc[-1:]     #选取DataFrame最后一行，返回的是DataFrame
        df = df.iloc[-1]
        
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
		
        if ((df.p_change > 5) and (df.p_change < 9)) and (df.volume > (df.v_ma10 * 1.5)) and (get_amount(df) > 3 * E ):
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)

        #if j > 250:
            #break
			
    print('''\n======================= 需求1 =============================
		a. 当日涨幅 p_change > 5 and p_change < 9
		b. 当日成交量 volume > (v_ma10 * 1.5)
		c. 成交额 > 3亿
        ''')
    stock_p_change = get_stock_info_by_key(stock_key)
    #save_stock(stock_p_change, '1_filter') 

    return
    
if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_1(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))