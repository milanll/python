from _comm_stock import *
from _date import *
start_date, end_date = get_x_trade_days(30)

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
data = ts.get_hist_data('sh', start = start_date, end = end_date)

i = 0
for index, r in data.iterrows():
    if r.volume > 1500000:
        i += 1
    else:
        break

print ('日成交量大于1.5亿手的连续天数：%d' % (i))
