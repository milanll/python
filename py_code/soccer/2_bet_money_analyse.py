
'''
import csv
from matplotlib import pyplot as plt
from datetime import datetime
#读取CSV文件数据
filename='sitka_weather_2014.csv'
with open(filename) as f: #打开这个文件，并将结果文件对象存储在f中
    reader=csv.reader(f)  #创建一个阅读器reader
    header_row=next(reader) #返回文件中的下一行
    dates,highs,lows=[],[],[]      #声明存储日期，最值的列表
    for row in reader:
        current_date=datetime.strptime(row[0],'%Y-%m-%d')  #将日期数据转换为datetime对象
        dates.append(current_date)    #存储日期
        high=int(row[1])    #将字符串转换为数字
        highs.append(high)   #存储温度最大值
        low=int(row[3])
        lows.append(low)    #存储温度最小值
 
#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)#实参alpha指定颜色的透明度，0表示完全透明，1（默认值）完全不透明
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) #给图表区域填充颜色
plt.title('Daily high and low temperature-2004',fontsize=24)
plt.xlabel('',fontsize=16)
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
fig.autofmt_xdate()  #绘制斜的日期标签
plt.show()


(1)figure语法说明

figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)

num:图像编号或名称，数字为编号 ，字符串为名称
figsize:指定figure的宽和高，单位为英寸；
dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
facecolor:背景颜色
edgecolor:边框颜色
frameon:是否显示边框

(2) 绘制曲线
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
 
T = np.array([6, 7, 8, 9, 10, 11, 12])
power = np.array([1.53E+03, 5.92E+02, 2.04E+02, 7.24E+01, 2.72E+01, 1.10E+01, 4.70E+00])
xnew = np.linspace(T.min(),T.max(),300) #300 represents number of points to make between T.min and T.max
 
power_smooth = spline(T,power,xnew)
 
plt.plot(xnew,power_smooth)
plt.show()

(3)设置坐标轴刻度

my_x_ticks = np.arange(-5, 5, 0.5)      #显示范围为-5至5，每0.5显示一刻度
my_y_ticks = np.arange(-2, 2, 0.2)      #显示范围为-2至2，每0.2显示一刻度
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)

(4)设置网格
matplotlin.pyplot.grid(b, which, axis, color, linestyle, linewidth， **kwargs)

grid()参数有很多，这里只列举了我此次工作中用到的几个：

    b : 布尔值。就是是否显示网格线的意思。官网说如果b设置为None， 且kwargs长度为0，则切换网格状态。但是没弄明白什            么意思。如果b设置为None，但是又给了其它参数，则默认None值失效。

    which : 取值为'major', 'minor'， 'both'。 默认为'major'。看别人说是显示的我的是Windows7下，用Sublime跑的，minor                 只是一个白画板，没有网格，major和both也没看出什么效果，不知道为什么。

    axis : 取值为‘both’， ‘x’，‘y’。就是想绘制哪个方向的网格线。不过我在输入参数的时候发现如果输入x或y的时候，             输入的是哪条轴，则会隐藏哪条轴

    color : 这就不用多说了，就是设置网格线的颜色。或者直接用c来代替color也可以。

    linestyle :也可以用ls来代替linestyle， 设置网格线的风格，是连续实线，虚线或者其它不同的线条。 | '-' | '--'                        | '-.' | ':' | 'None' | ' ' | '']

    linewidth : 设置网格线的宽度

'''
import csv
import copy
from datetime import datetime

'''
import sys;
sys.path.append("../time_chenll")
from time_manage import get_month_from_date
'''

#read data from bet_record.csv, return dates list and balance list
def read_record():
	#filename = 'E:/git/python/py_code/soccer/bet_record/bet_record_18-19.csv'
	filename = 'E:/git/python/py_code/soccer/bet_record/bet_record_week_18-19.csv'
	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader) #返回文件中的下一行
		#dates, balance, costs = [], [], []
		
		#row = [Date,Balance,Cost,Mark]
		#计算成本总额
		cost = 0
		bet_data = {}
		for row in reader:
			#date = datetime.strptime(row[0],'%Y-%m-%d')
			date = row[0]
			#dates.append(date)

			#成本
			cost += int(row[2])
			
			count = int(row[1]) - cost
			#balance.append(count)
			
			bet_data[date] = count
		
	return bet_data

	
#draw chart according to dates list and balance list
#param [in]:	list data
def draw_chart(data):
	import matplotlib.pyplot as plt #importing matplot lib library
	import numpy as np
	from scipy.interpolate import spline
	
	figsize_x = len(data) * 0.4;
	fig=plt.figure(dpi=80,figsize=(figsize_x,6))
	x = data.keys()
	#x_new = np.linspace(dates, dates[0], dates[len(dates) - 1])
	#print x, print and check what is x
	y = data.values()

	# 实现插值的模块
	from scipy import interpolate
	#y_new = spline(x,y,x_new)
	#print y
	print(len(x))
	plt.plot(x,y) #plotting x and y
	fig.autofmt_xdate()  #绘制斜的日期标签

	#设置网格
	plt.grid(axis = 'y')
	plt.show()

if __name__ == '__main__':
	data = read_record()
	draw_chart(data)

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	