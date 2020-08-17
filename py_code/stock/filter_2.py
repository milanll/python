
from _comm_stock import *
from _date import *
from get_stock_hist_data import *

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

def print_filter_2_condition():
    print('''\n======================= 需求2 =============================
            a. 连续3天，累计涨幅超15%。
            b. 每天涨幅大于1%。 
            \n''')    
    return
    
#[breif]    append one record to count_grow_2_days.csv  
#[input]    date(str)       2019-05-15
#           count(int)      50
def save_count_grow_2_days(date, count):
    file = './data/count_grow_2_days.csv'
    f = pd.read_csv(file)
    if f is None:
        print('Read count_grow_2_days.csv fail!!!')
    
    df = pd.DataFrame({'Date':date, 'Count':count}, index = [len(f) + 1])
    df.to_csv(file, mode='a', header=False)
    
def filter_2(stock_data):
    
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
        df = df.sort_values(by = "trade_date")
        
        #get the last 3 rows.
        df = df[-3:]
        
        #       ts_code  trade_date   open   high    low    close     pre_close  change(额度)   pct_chg(幅度)   vol         amount         ma5       ma_v_5        ma10      ma_v_10       ma20       ma_v_20
        #0   000001.SZ   20181011     10.05  10.16   9.70   9.86      10.45       -0.59         -5.6459         1995143.83  1994186.611    10.474    1570205.872   10.527    1344378.759   10.2365    1.068715e+06
		
        p = 0
        i = 0
        for index, r in df.iterrows(): 
            if r.pct_chg > 1:
                i += 1
            p += r.pct_chg
                
        if p > 15 and i == 3:
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)

        #if j > 250:
            #break
    
    print_filter_2_condition()
    stock_p_change = get_stock_info_by_key(stock_key)
    #save_stock(stock_p_change, '2_filter') 
    
    count = len(stock_p_change)
    #save_count_grow_2_days(end_date, count)

    return stock_key
    
if __name__ == '__main__':

    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_2(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))
