import pandas as pd
from _comm_stock import *

pd.set_option('display.max_rows',None)
pd.set_option('display.width',None)

stock_amount = read_stock_amount()
stock_trade = read_stock_trade()

def analyse_trade_detail(code):
    col_name_1 = ('ts_code', 'trade_date', 'close', 'open', 'high', 'low', 'vol', 'amount')
    df_trade_detail = pd.DataFrame(columns=col_name_1)

    for i, r in stock_trade.iterrows():
        if r.ts_code == code:
            df_trade_detail = df_trade_detail.append(r, ignore_index=True)

    #print (df_trade_detail.loc[0].close, df_trade_detail.loc[1].close, df_trade_detail.loc[2].close)
    if (df_trade_detail.loc[0].close > df_trade_detail.loc[1].close) and (df_trade_detail.loc[1].close < df_trade_detail.loc[2].close):
        return True
    else:
        return False

def stock_sel():
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'list_date')
    stock = pd.DataFrame(columns=col_name)

    for i, r in stock_amount.iterrows():
        if analyse_trade_detail(r.ts_code):
            df_row = pd.DataFrame([r], columns=col_name)
            stock = stock.append(df_row)

    print(stock)


if __name__ == '__main__':
    stock_sel()


