
from _comm_stock import *
from _date import *
start_date, end_date = get_period_x_days(5)

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

def get_stock_by_3_rasing_limit(code):
    data = ts.get_hist_data(code, start = start_date, end = end_date)
    if data is None:
        return None

    i = 0
    for index, r in data.iterrows():
        if r.p_change > 9.7:
            i += 1

        if i == 3:
            break

    if i == 3:
        return True
    else:
        return False

def get_stock():
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)

    for index, row in stock_basic_info.iterrows():
        code = str(row.symbol).zfill(6)
        ret = get_stock_by_3_rasing_limit(code)

        if ret:
            # translate from series to dataframe
            df_row = pd.DataFrame([row], columns=col_name)
            print(row.values)
            # append datafarme
            stock_ma = stock_ma.append(df_row)

    save_stock(stock_ma, '3_10')
    return stock_ma

if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    get_stock()
    stock = read_stock('3_10')
    print (stock)
    print (stock.shape[0])

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))