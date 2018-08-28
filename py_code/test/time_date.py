# Filename : test.py
# author by : www.runoob.com
 
# 引入 datetime 模块
import datetime
def getYesterday(): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=2) 
    yesterday=today-oneday  
    return yesterday
 
# 输出
print(getYesterday())
print(datetime.timedelta(days=2))
print(datetime.date.today())