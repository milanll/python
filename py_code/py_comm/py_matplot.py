'''

from matplotlib import pyplot as plt
from datetime import datetime

 
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
#draw chart according to dict
#param [in]: data(dict)
def draw_line_chart(data):
	import matplotlib.pyplot as plt #importing matplot lib library
	import numpy as np
	from scipy.interpolate import spline

	fig = plt.figure(dpi=80,figsize=(10,6))
	x = tuple(data.keys())
	y = tuple(data.values())
	
	#设置标签
	#for a,b in zip(x, y):
		#plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)

	print(len(x))
	plt.plot(x,y) #plotting x and y
	fig.autofmt_xdate()  #绘制斜的日期标签

	#设置网格
	plt.grid(axis = 'y')
	plt.title("投注盈亏图")
	plt.show()

	
'''
柱状图
绘制柱状图，我们主要用到bar()函数。只要将该函数理解透彻，我们就能绘制各种类型的柱状图。

我们先看下bar()的构造函数：bar(x，height， width，*，align='center'，**kwargs)

x
包含所有柱子的下标的列表

height
包含所有柱子的高度值的列表

width
每个柱子的宽度。可以指定一个固定值，那么所有的柱子都是一样的宽。或者设置一个列表，这样可以分别对每个柱子设定不同的宽度。

align
柱子对齐方式，有两个可选值：center和edge。center表示每根柱子是根据下标来对齐, edge则表示每根柱子全部以下标为起点，然后显示到下标的右边。如果不指定该参数，默认值是center。

其他可选参数有：

color
每根柱子呈现的颜色。同样可指定一个颜色值，让所有柱子呈现同样颜色；或者指定带有不同颜色的列表，让不同柱子显示不同颜色。

edgecolor
每根柱子边框的颜色。同样可指定一个颜色值，让所有柱子边框呈现同样颜色；或者指定带有不同颜色的列表，让不同柱子的边框显示不同颜色。

linewidth
每根柱子的边框宽度。如果没有设置该参数，将使用默认宽度，默认是没有边框。

tick_label
每根柱子上显示的标签，默认是没有内容。

xerr
每根柱子顶部在横轴方向的线段。如果指定一个固定值，所有柱子的线段将一直长；如果指定一个带有不同长度值的列表，那么柱子顶部的线段将呈现不同长度。

yerr
每根柱子顶端在纵轴方向的线段。如果指定一个固定值，所有柱子的线段将一直长；如果指定一个带有不同长度值的列表，那么柱子顶部的线段将呈现不同长度。

ecolor
设置 xerr 和 yerr 的线段的颜色。同样可以指定一个固定值或者一个列表。

capsize
这个参数很有趣, 对xerr或者yerr的补充说明。一般为其设置一个整数，例如 10。如果你已经设置了
yerr 参数，那么设置 capsize 参数，会在每跟柱子顶部线段上面的首尾部分增加两条垂直原来线段的线段。对 xerr 参数也是同样道理。可能看说明会觉得绕，如果你看下图就一目了然了。


	import matplotlib.pyplot as plt
	import numpy as np

	# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
	plt.figure(figsize=(8, 6), dpi=80)

	# 再创建一个规格为 1 x 1 的子图
	plt.subplot(1, 1, 1)

	# 柱子总数
	N = 6
	# 包含每个柱子对应值的序列
	values = (25, 32, 34, 20, 41, 50)

	# 包含每个柱子下标的序列
	index = np.arange(N)

	# 柱子的宽度
	width = 0.35

	# 绘制柱状图, 每根柱子的颜色为紫罗兰色
	p2 = plt.bar(index, values, width, label="rainfall", color="#87CEFA")

	# 设置横轴标签
	plt.xlabel('Months')
	# 设置纵轴标签
	plt.ylabel('rainfall (mm)')

	# 添加标题
	plt.title('Monthly average rainfall')

	# 添加纵横轴的刻度
	plt.xticks(index, ('Jan', 'Fub', 'Mar', 'Apr', 'May', 'Jun'))
	plt.yticks(np.arange(0, 81, 10))

	# 添加图例
	plt.legend(loc="upper right")
'''
#[input]:	data(dict)	{month:profit}
def draw_bar_graph(data):
	import matplotlib.pyplot as plt
	import numpy as np
	
	# 柱子总数
	N = len(data.keys())
	
	# 创建一个点数为 8 x 6 的窗口, 并设置分辨率为 80像素/每英寸
	plt.figure(figsize=(N, 6), dpi=80)

	# 再创建一个规格为 1 x 1 的子图
	plt.subplot(1, 1, 1)

	# 包含每个柱子对应值的序列
	y = values = tuple(data.values())

	# 包含每个柱子下标的序列
	x = index = tuple(data.keys())

	# 柱子的宽度
	width = 0.25
	
	#设置柱子标签
	for a,b in zip(x, y):
		plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)

	# 绘制柱状图, 每根柱子的颜色为紫罗兰色
	p2 = plt.bar(x, y, width, label="rainfall", color="#3299CC")

	# 设置横轴标签
	plt.xlabel('Months')
	# 设置纵轴标签
	plt.ylabel('rainfall (mm)')

	# 添加标题
	plt.title('Monthly average rainfall')

	# 添加纵横轴的刻度
	plt.xticks(x, ('Aug', 'Seb', 'Oct'))
	plt.yticks(np.arange(min(y), max(y), 100))

	# 添加图例
	#plt.legend(loc="upper right")

	plt.show()




if __name__ == '__main__':
	
	draw_bar_graph()
	
	