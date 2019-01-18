import datetime
import time

DAYS = 60

#[Return]   True    After 16:00
#           False   Before 16:00
def time_compare_pm4():
    str_Time_16 = time.strftime("%Y%m%d",time.localtime()) + '160000'
    str_Time_now = time.strftime("%Y%m%d%H%M%S",time.localtime())

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

#[breif]    if before 16:00,return yestoday
#           else return today
#[date]     date(str)   2019-01-14
def get_date():
    if time_compare_pm4():
        #today
        return datetime.date.today()
    else:
        #yestoday
        return datetime.date.today() - datetime.timedelta(days = 1)


if __name__ == "__main__":
    #str_start_date, end_date = get_period()
    date = get_date()
    print(date)