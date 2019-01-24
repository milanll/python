
from _comm_stock import *
from _date import *
start_date, end_date = get_period_3days()

stock_basic_info = pd.read_csv("./data/stock_basic_info.csv", encoding="utf-8")

pd.set_option('display.width', 1000)

def get_stock_by_ma(code):
    data = ts.get_hist_data(code, start = start_date, end = end_date)
    if data is None:
        return None

    i = 0
    for index, r in data.iterrows():
        if r.volume > r.v_ma10 * 1.5:
            if (r.ma5 > r.ma10) and (r.ma10 > r.ma20):
                i += 1
            else:
                return False

            if i == 2:
                return True
        else:
            return False

def get_stock():
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)

    for index, row in stock_basic_info.iterrows():
        code = str(row.symbol).zfill(6)
        ret = get_stock_by_ma(code)

        if ret:
            # translate from series to dataframe
            df_row = pd.DataFrame([row], columns=col_name)
            print(row.values)
            # append datafarme
            stock_ma = stock_ma.append(df_row)

    save_stock(stock_ma, 'ma')
    return stock_ma

if __name__ == '__main__':
    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    get_stock()
    stock = read_stock('ma')
    print (stock)
    print (stock.shape[0])

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))