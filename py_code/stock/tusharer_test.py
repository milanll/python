
'''
在新版0.5.6中，已经新增了一个接口：get_k_data，具体使用方法请参考tushare公众号文章《全新的免费行情数据接口》 ，建议使用全新接口。
获取个股历史交易数据（包括均线数据），可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据。本接口只能获取近3年的日线数据，适合搭配均线数据进行选股和分析，如果需要全部历史数据，请调用下一个接口get_h_data()。

参数说明：

code：股票代码，即6位数字代码，或者指数代码（sh=上证指数 sz=深圳成指 hs300=沪深300指数 sz50=上证50 zxb=中小板 cyb=创业板）
start：开始日期，格式YYYY-MM-DD
end：结束日期，格式YYYY-MM-DD
ktype：数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
retry_count：当网络异常后重试次数，默认为3
pause:重试时停顿秒数，默认为0

返回值说明：

date：日期
open：开盘价
high：最高价
close：收盘价
low：最低价
volume：成交量
price_change：价格变动
p_change：涨跌幅
ma5：5日均价
ma10：10日均价
ma20:20日均价
v_ma5:5日均量
v_ma10:10日均量
v_ma20:20日均量
turnover:换手率[注：指数无此项]
'''

import tushare as ts
import datetime

stock_code = input('Please input stocke code:')

date = datetime.date.today()

# 获取某只股票数据
#print(ts.get_hist_data('600487', start='2018-01-05',end='2018-04-18'))

# 基金持股情况
# print(ts.fund_holdings(2017, 3))

# 新股发行情况
# print(ts.new_stocks())

# 实时指数行情
#print(ts.get_index())
#print(ts.get_index())
#print(ts.realtime_boxoffice())
#print(ts.get_deposit_rate().rate)

#大单交易数据
dd = ts.get_sina_dd(stock_code, date= date, vol=100)
#type = ts.get_sina_dd(stock_code, date= date, vol=100).type
print(ts.get_sina_dd(stock_code, date= date, vol=100)) #默认400手

buy_vol = 0
sell_vol = 0
print(type(dd))

for d in dd:
	print(type(d))
	if '买盘' in d:
		buy_vol += d.volume
	else:
		sell_vol += d.volume

print('buy:%d,sell:%d' % (buy_vol,sell_vol))
#print(ts.get_notices('300395'))











