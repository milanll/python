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
        return str(date)[0:4] + str(date)[5:7] + str(date)[8:10]
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

#[breif]    get the trade calendar of this year
#[return]   calendar(DataFrame)
def get_trade_calendar():
    pro = ts.pro_api()

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    
    start = str(year) + '0101'
    end = str(year) + '1231'
    
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
    
    #exchange  cal_date     is_open
    #     SSE  20190102        1
    calendar = pro.trade_cal(exchange='SSE', start_date=start, end_date=end, is_open = '1')
    
    return calendar

#[input]    in_date(str)      20190101    
#[return]   ret_date(str)     20190101
def get_pre_trade_day(in_date):
    date = datetime.datetime.strptime(transfer_date_format(in_date), "%Y-%m-%d")
    pre_date = date - datetime.timedelta(days = 1)
    ret_date = transfer_date_format(pre_date)
    
    return ret_date
       
#[breif]    
#           if before 16:00,
#               return previous trade day               
#           else 
#               if today is trade day
#                   return today
#               else
#                   reurn the previous trade day
#[ret]     date(str)   20190114
def get_trade_date():
    cal = get_trade_calendar()
    date_today = datetime.date.today()
    today = transfer_date_format(date_today)
    
    #after 16:00
    if time_compare_pm4():
        if today in cal['cal_date'].values:
            return today
        else:
            d = get_pre_trade_day(today)
            while d not in cal['cal_date'].values:
                d = get_pre_trade_day(d)
            return d
       
    #before 16:00
    else:
        d = get_pre_trade_day(today)
        while d not in cal['cal_date'].values:
            d = get_pre_trade_day(d)           
        return d
        
    
    return None
        
#[breif]    get x trade days backwards from today
#[input]    x(int)      amount of days      5
#[Return]   str_start_date(str)  2018-01-01
#           str_end_date(str)    2018-12-11
def get_x_trade_days(x):

    calendar = get_trade_calendar()
    cal_date = calendar['cal_date']

    today = get_trade_date()

    i = 0
    while (i < cal_date.shape[0]):
        if cal_date[i] == today:
            break
        else:
            i += 1

    if i < x:
        print ('x is too small to get date!')
        return (None)
    
    #print('i is %d' % i)
    start_date = transfer_date_format(cal_date[i - x + 1])
    end_date = transfer_date_format(get_trade_date())
    #print(end_date)

    #start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    
    #print('\nstart_date: %s\nend_date: %s\n' % (start_date, end_date))
    
    return start_date, end_date

#[Return]   today(str)  2018-01-01
def get_today():
    today = datetime.date.today()
    print(today)
    return(today)
    
if __name__ == "__main__":

    pass

    
