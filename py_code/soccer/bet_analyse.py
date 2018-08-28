
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

'''
import csv
from datetime import datetime

filename = 'E:/7_python/code/soccer/bet_record/bet_record_18-19.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row=next(reader) #返回文件中的下一行
	dates, counts = [], []
	
	#row = [Date,Balance,Cost]
	#计算成本总额

	for row in reader:
		#date = datetime.strptime(row[0],'%Y-%m-%d')
		date = row[0]
		dates.append(date)
		
		count = int(row[1])
		counts.append(count)
#

import matplotlib.pyplot as plt #importing matplot lib library
import numpy as np
from scipy.interpolate import spline

fig=plt.figure(dpi=80,figsize=(10,6))
x = dates 
#x_new = np.linspace(dates, dates[0], dates[len(dates) - 1])
#print x, print and check what is x
y = counts
#y_new = spline(x,y,x_new)
#print y
plt.plot(x,y) #plotting x and y
fig.autofmt_xdate()  #绘制斜的日期标签
plt.show()

