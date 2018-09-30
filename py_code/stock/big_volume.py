
'''
大单交易数据¶
获取大单交易数据，默认为大于等于400手，数据来源于新浪财经。

参数说明：

code：股票代码，即6位数字代码
date:日期，格式YYYY-MM-DD
vol:手数，默认为400手，输入数值型参数
retry_count : int, 默认3,如遇网络等问题重复执行的次数
pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
返回值说明：

code：代码
name：名称
time：时间
price：当前价格
volume：成交手
preprice ：上一笔价格
type：买卖类型【买盘、卖盘、中性盘】
'''

import tushare as ts
import datetime

stock_code = input('Please input stocke code:')

date = datetime.date.today()

#大单交易数据

#默认400手
dd = ts.get_sina_dd(stock_code, date= date, vol=100)
print(dd) 

buy_vol = 0
sell_vol = 0

for i in range(len(dd)):
	if '卖盘' in dd['type'][i]:		
		sell_vol += dd['volume'][i]
		
	elif '买盘' in dd['type'][i]:
		buy_vol += dd['volume'][i]
		
	else:
		#print('中性盘')
		pass

print('\nbuy:%d,sell:%d' % (buy_vol,sell_vol))
print('buy volume:', buy_vol - sell_vol)
#print(ts.get_notices('300395'))











