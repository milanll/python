
from _comm_stock import *
from _date import *
#import get_stock_hist_data
from get_stock_hist_data import *

count_days = 30
start_date, end_date = get_x_trade_days(count_days)

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

def print_filter_9_condition():
    print('''\n======================= 需求9 =============================
            需求：连续4个交易日，收盘涨幅2%以上
          ''')    
    return
    
#[input]     stock_data(dict)   
def filter_9(stock_data):
    print('\nfilter_9():')
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
        df = df[-4:]
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        i = 0
        for index, r in df.iterrows():           
            if r.p_change > 2:
                i += 1
                continue
            
        if i == 4:
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)
    
        #if j > 250:
            #break
    print_filter_9_condition() 
    stock_ma = get_stock_info_by_key(stock_key)
    #save_stock(stock_ma, '9_ma20') 

    return stock_key

if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_9(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))