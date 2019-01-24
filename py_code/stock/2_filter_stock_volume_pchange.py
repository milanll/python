
from _comm_stock import *
from _date import *
start_date, end_date = get_period_3days()

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

def get_stock_by_pchange(code):
    data = ts.get_hist_data(code, start = start_date, end = end_date)
    if data is None:
        return None

    #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
    #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
    i = 0
    for index, r in data.iterrows():
        i += 1
        if i == 1:
            if r.volume > r.v_ma10 * 3:
                if (r.p_change > 4):
                    return True
                else:
                    return False

            else:
                return False
        elif i == 2:
            pass

def get_stock():
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', '_name', 'area', 'industry', 'market', 'list_date')
    stock_p_change = pd.DataFrame(columns=col_name)

    for index, row in stock_basic_info.iterrows():
        code = str(row.symbol).zfill(6)
        ret = get_stock_by_pchange(code)

        if ret:
            # translate from series to dataframe
            row = row.drop('Unnamed: 0')
            df_row = pd.DataFrame([row], columns=col_name)
            print(row.values)
            # append datafarme
            stock_p_change = stock_p_change.append(df_row)

    save_stock(stock_p_change, 'p-change')
    return stock_p_change

if __name__ == '__main__':

    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    get_stock()
    stock = read_stock('p-change')
    print (stock.shape[0])

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))
