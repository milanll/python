
from _comm_stock import *
from _date import *
#import get_stock_hist_data
from get_stock_hist_data import *

count_days = 30
start_date, end_date = get_x_trade_days(count_days)

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

def get_stock_by_ma20(code):
    # open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
    # 10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
    data = ts.get_hist_data(code, start = start_date, end = end_date)
    
    if check_stock_data(data, count_days, code) != True:
        return False

    for index, r in data.iterrows():
        if r.close > r.ma20 * 0.99:
            continue
        else:
            return False

    return True

def get_stock():
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)

    for index, row in stock_basic_info.iterrows():
        code = str(row.symbol).zfill(6)
        ret = get_stock_by_ma20(code)

        if ret:
            # translate from series to dataframe
            df_row = pd.DataFrame([row], columns=col_name)
            print(row.values)
            # append datafarme
            stock_ma = stock_ma.append(df_row)

    save_stock(stock_ma, '9_ma20')
    return stock_ma
    
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
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        i = 0
        for index, r in df.iterrows():           
            if r.close > (r.ma20 * 0.99):
                i += 1
                continue
            
        if i > (len(df) * 0.9):
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)
    
        #if j > 250:
            #break
    #print('\n')
    stock_ma = get_stock_info_by_key(stock_key)
    save_stock(stock_ma, '9_ma20') 

    return

if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_9(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))