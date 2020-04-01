from _comm_stock import *
from _date import *
from get_stock_hist_data import *

#pd.set_option('display.width', 1000)
#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
#pd.set_option('max_colwidth',100)

x_trade_days = 300
start_date, end_date = get_x_trade_days(x_trade_days)

#stock list
codes = ['300474','603986','000938','002049','300750','603259','600276','300454','000063','603019','002439','000977','002396','300760']

#每天所有股票价格之和
#price = {'2019-05-01:3000', ......}
price = {}

for code in codes:
	
	data = ts.get_hist_data(code, start = start_date, end = end_date)

	#按index升序排列
	data = data.sort_index()
	
	for k, v in data.iterrows():

		if k in price.keys():
			price[k] += round(v.close,2)
		else:
			price[k] = round(v.close,2)
			
for k, v in price.items():
	price[k] = round((v / 14), 2)


import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
 
x = price.keys()
y = price.values()
 
plt.plot(x,y,c='blue')

#把x轴的刻度间隔设置为1，并存在变量里
x_major_locator=MultipleLocator(30)
#ax为两条坐标轴的实例
ax=plt.gca()
#把x轴的主刻度设置为1的倍数
ax.xaxis.set_major_locator(x_major_locator)

#设置x轴标签及其字号
#plt.xlabel('Data',fontsize=16)

#设置刻度的字号
plt.tick_params(axis='x',which='major',labelsize=6)

plt.show()
