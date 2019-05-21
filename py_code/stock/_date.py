import datetime
import tushare as ts
#import time
#from _comm_stock import *

DAYS = 60

#[breif]    if      input 2019-01-01,  output  20190101
#           elif    input 20190101,    o  2019-01-01
#[input]    date        2019-01-01  or  20190101
#[output]   str_date    20190101    or  2019-01-01
def transfer_date_format(date):
    if '-' in str(date):
        return str(date)[0:4] + str(date)[5:7] + str(date)[8:]
    else:
        return str(date)[0:4] + '-' + str(date)[4:6] + '-' + str(date)[6:]

#[Return]   True    After 16:00
#           False   Before 16:00
def time_compare_pm4():

    str_Time_16 = datetime.datetime.now().strftime('%Y-%m-%d') + ' ' + '16:00:00'
    str_Time_now = (datetime.datetime.now()+datetime.timedelta(hours=7)).strftime('%Y-%m-%d %H:%M:%S')
    
    if (str_Time_now > str_Time_16):
        return True
    else:
        return False


#[Return]   str_start_date(str)  20180101
#           str_end_date(str)    20181211
def get_period():
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    days_x = datetime.timedelta(days = DAYS)

    if time_compare_pm4():
        end_date = today
    else:
        end_date = today - oneday

    start_date = end_date - days_x

    str_start_date = str(start_date)[0:4] + str(start_date)[5:7] + str(start_date)[8:]
    str_end_date = str(end_date)[0:4] + str(end_date)[5:7] + str(end_date)[8:]

    return str_start_date, str_end_date, DAYS/10

#[Input]    x_days(int)          5
#[Return]   str_start_date(str)  2018-01-01
#           str_end_date(str)    2018-12-11
def get_period_x_days(x_days):
    today = datetime.date.today()
    oneday = datetime.timedelta(days = 1)
    days_x = datetime.timedelta(days = int(x_days))

    if time_compare_pm4():
        end_date = today
    else:
        end_date = today - oneday

    start_date = end_date - days_x
    print(start_date)

    start_date = start_date.strftime("%Y-%m-%d")
    end_date = end_date.strftime("%Y-%m-%d")

    return start_date, end_date

#[breif]    if before 16:00,return yestoday
#           else return today
#[ret]     date(str)   2019-01-14
def get_date():
    if time_compare_pm4():
        #today
        #print(datetime.date.today())
        return datetime.date.today()
    else:
        #yestoday
        #print(datetime.date.today() - datetime.timedelta(days = 1))
        return datetime.date.today() - datetime.timedelta(days = 1)

#[breif]    get the previous day of the given date 
#[input]    date(str)       20190114
#[ret]      pre_day(str)    2019-01-14
def get_pre_date(date):
    date = transfer_date_format(today)
    #previous day
    #print(datetime.date.today() - datetime.timedelta(days = 1))
    return datetime.date.today() - datetime.timedelta(days = 1)
        
#[breif]    get x trade days backwards from today
#[input]    x(int)      amount of days      5
#[Return]   str_start_date(str)  2018-01-01
#           str_end_date(str)    2018-12-11
def get_x_trade_days(x):
    '''
    input parameters：
    exchange	str	    N	    交易所 SSE上交所 SZSE深交所
    start_date	str	    N	    开始日期
    end_date	str	    N	    结束日期
    is_open	    int	    N	    是否交易 0休市 1交易

    output parameters:
    exchange	    str	Y	    交易所 SSE上交所 SZSE深交所
    cal_date	    str	Y	    日历日期
    is_open	        int	Y	    是否交易 0休市 1交易
    pretrade_date	str	N	    上一个交易日

    '''
    pro = ts.pro_api()
    calendar = pro.trade_cal(exchange='', start_date='20190101', end_date='20191231', is_open = '1')
    #print(calendar)
    cal_date = calendar['cal_date']

    today = transfer_date_format(get_date())
    '''
    while today not in calendar:
        today = datetime.datetime.strptime(today, '%Y-%m-%d') - datetime.timedelta(days = 1)
    
    today = transfer_date_format(today)
    print('today is %s' % today)
    '''
    
    i = 0
    while (i < cal_date.shape[0]):
        if cal_date[i] == today:
            break
        else:
            i += 1

    if i < x:
        print ('x is too small to get date!')
        return (None)
    
    print('i is %d' % i)
    start_date = transfer_date_format(cal_date[i - x + 1])
    end_date = get_date()
    print(end_date)

    #start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = end_date.strftime("%Y-%m-%d")
    
    print('\nstart_date: %s\nend_date: %s\n' % (start_date, end_date))
    
    return start_date, end_date

#[Return]   today(str)  2018-01-01
def get_today():
    today = datetime.date.today()
    print(today)
    return(today)
    
if __name__ == "__main__":

    get_x_trade_days(20)

    
