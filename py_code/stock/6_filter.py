from _comm_stock import *
from _date import *


'''
ts.get_hist_data('600848') #一次性获取全部日k线数据
3.ts.get_hist_data('600848',start='2015-05-01',end='2015-06-18') #指定时间区间
4.ts.get_hist_data('600848'，ktype='W') #获取周k线数据
5.ts.get_hist_data('600848'，ktype='M') #获取月k线数据
6.ts.get_hist_data('600848'，ktype='5') #获取5分钟k线数据
7.ts.get_hist_data('600848'，ktype='15') #获取15分钟k线数据
8.ts.get_hist_data('600848'，ktype='30') #获取30分钟k线数据
9.ts.get_hist_data('600848'，ktype='60') #获取60分钟k线数据
10.ts.get_hist_data('sh'）#获取上证指数k线数据，其它参数与个股一致，下同
11.ts.get_hist_data('sz'）#获取深圳成指k线数据
12.ts.get_hist_data('hs300'）#获取沪深300指数k线数据
13.ts.get_hist_data('sz50'）#获取上证50指数k线数据
14.ts.get_hist_data('zxb'）#获取中小板指数k线数据
15.ts.get_hist_data('cyb'）#获取创业板指数k线数据
'''

E = 100000000

from get_stock_hist_data import *
def filter_6(stock_data):
    print('\nfilter_6():')
    # create a initial dataframe
    col_name = ('ts_code', 'symbol', 'name', 'area', 'industry', 'market', 'list_date')
    stock_ma = pd.DataFrame(columns=col_name)
    
    stock_key = []
    #base = stock_basic_info.shape[0]
    base = len(stock_data)
    
    
    j = 0
    for k, v in stock_data.items():
        j += 1
        df = pd.DataFrame(v)
        #data.iloc[-1]   #选取DataFrame最后一行，返回的是Series
        #data.iloc[-1:]   #选取DataFrame最后一行，返回的是DataFrame
        df = df[-3:]
        
        #open   high    close   low     volume      price_change    p_change    ma5     ma10    ma20    v_ma5       v_ma10      v_ma20
        #10.40  10.55   10.52   10.37   679240.88   0.17            1.64        10.384  10.320  9.941   607936.01   663916.01   713548.05
        if (((df.iloc[-1].ma5 > df.iloc[-1].ma10) and (df.iloc[-1].ma20 > df.iloc[-1].ma5))
            and ((df.iloc[-2].ma5 < df.iloc[-2].ma10) and (df.iloc[-2].ma10 < df.iloc[-2].ma20))
            and ((df.iloc[-1].close * df.iloc[-1].volume * 100) > 2 * E)):
            
            stock_key.append(k)
            #print(k)
            progress_bar(j, base)

            
    stock_p_change = get_stock_info_by_key(stock_key)
    #save_stock(stock_p_change, '6_filter') 

    return
    
if __name__ == '__main__':

    time_start = time.time()
    print (time.asctime( time.localtime(time.time()) ))

    stock_data = get_hist_data_()
    filter_6(stock_data)

    time_end = time.time()
    print (time.asctime(time.localtime(time.time())))
    print(int(time_end - time_start))
