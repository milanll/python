
from _comm_stock import *
from _date import *
from get_stock_hist_data import *

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

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
        #get the last 3 rows.
        df = df[-3:]
        
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        p = 0
        i = 0
        for index, r in df.iterrows(): 
            if r.p_change > 1:
                i += 1
            p += r.p_change
                
        if p > 10 and i == 3:
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)

        #if j > 250:
            #break
    
    print('''\n======================= 需求2 =============================
            a. 连续3天，累计涨幅超10%。\n''')
    stock_p_change = get_stock_info_by_key(stock_key)
    #save_stock(stock_p_change, '2_filter') 
    
    count = len(stock_p_change)
    #save_count_grow_2_days(end_date, count)

    return
    
if __name__ == '__main__':

    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_2(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))
