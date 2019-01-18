import os
import time
import datetime

from _date import time_compare_pm4

#[Breif]    Cacultate the time(s) from now to 16:10 of next day
def get_timer_value():
    """Return the day of the week as an integer, where Monday is 0 and
            Sunday is 6.

            :rtype: int
    """

    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    days_3 = datetime.timedelta(days=1)
    wd = today.weekday()

    if(wd == 4):
        tomorrow = today + days_3
    else:
        tomorrow = today + oneday

    str_tomorrow_time_16 = time.strptime(str(tomorrow), '%Y-%m-%d')
    tomorrow_0000 = time.mktime(str_tomorrow_time_16)
    tomorrow_1610 = tomorrow_0000 + 60*60*16 + 60*10

    print (tomorrow_1610)

    now = time.mktime(time.localtime())

    print(now)

    return tomorrow_1610 - now


#[Breif]    run get_stock_big_amount.py at 16:10 every day
def exc_stock_sel():
    while True:
        #after 16:00, run get_stock_big_amount.py
        if time_compare_pm4():
            os.system('py get_stock_big_amount.py')

            #sleep, until 16:10 next day
            timer_value = get_timer_value()
            time.sleep(timer_value)

        #before 16:00, sleep 10 min
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            time.sleep(10 * 60)


if __name__ == '__main__':
    exc_stock_sel()