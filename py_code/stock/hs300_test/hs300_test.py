import tushare as ts
import datetime
import pandas as pd

d = ts.get_hist_data('hs300', start = '2017-01-01', end = '2019-06-11')
#按时间升序排列
d = d.sort_index()

'''    
class Exchage:
    def _init_(self):
        #slef.num            =   '000'       
        slef.date_buy       =   ''   
        slef.vol_buy        =   0  
        slef.price_buy      =   0
        slef.date_sell      =   ''  
        slef.vol_sell       =   0 
        slef.price_sell     =   0
        slef.balance        =   0
'''        
g_total = 10000
g_exchange = {}
g_num = 0
g_vol = 0
Flag_Hold_Stock = 0     #0:no stock; 1:holding stock

#[input]    stock_info(Series)
def get_vol_hold(stock_info):

    M = 1000000
    p = 1
    
    '''
    仓位            10           8            6               4           2           1
    volume        >3000000      >2500000     >2000000    >1500000     >1000000     <1000000
    '''
    if stock_info > 3 * M:
        p = 10
    elif stock_info > 2.5 * M and stock_info < 3 * M:
        p = 8
    elif stock_info > 2 * M and stock_info < 2.5 * M:
        p = 6
    elif stock_info > 1.5 * M and stock_info < 2 * M:
        p = 4
    elif stock_info > 1 * M and stock_info < 1.5 * M:
        p = 2
    else:
        p = 1
    
    return g_total * p / 10
  
#[input]    vol_now(int)            today,the vol that we real holding
#           vol_new(int)            today,the vol that we should holding  
#           stock_info(Series)      to calculate the middle price of hs300, (high + low) / 2

def buy_hs300(key, stock_info):
    global g_total, g_vol, Flag_Hold_Stock

    Flag_Hold_Stock = 1
    
    price = (stock_info.high + stock_info.low) / 2 / 100
    
    g_vol = g_total / price
    
    g_total -= (g_vol * price)
    
    print('%s: Buy      %d\n' % (key, g_vol))
    
    return g_vol
    
#[input]    vol_now(int)            today,the vol that we real holding
#           vol_new(int)            today,the vol that we should holding  
#           stock_info(Series)      to calculate the middle price of hs300, (high - low) / 2

def sell_hs300(key, stock_info):
    
    global g_total, g_vol, Flag_Hold_Stock
    
    Flag_Hold_Stock = 0
    
    price = (stock_info.high + stock_info.low) / 2 / 100
    
    g_total += g_vol * price
    
    print('%s: Sell     %d\n' % (key, g_vol))
    
    return g_vol
       

if __name__ == '__main__':
   
    print('Date        Operate  Vol')
    '''
                       open     high    close      low      volume  price_change  p_change       ma5      ma10      ma20      v_ma5     v_ma10      v_ma20
            date
            2019-06-11  3617.52  3723.14  3719.28  3617.52  1434828.00        108.54      3.01  3618.056  3632.943  3642.171  994262.75  992521.07  1028851.53
    '''
    ma5_pre = 0
    i = 0
    j = 0
    for k, v in d.iterrows():    
        if v.ma5 > v.ma10:
            if Flag_Hold_Stock == 0:
                buy_hs300(k, v)
            
            
        elif v.ma5 < ma5_pre:
            if Flag_Hold_Stock == 1:
                sell_hs300(k, v)
                i += 1
                
        elif v.ma5 < v.ma10:
            pass
                
        else:
            print('ERROR!!\n')
            pass
            
        ma5_pre = v.ma5
        
        if Flag_Hold_Stock == 0:
            j += 1
    
    g_total = round(g_total, 2)
    p = (d.iloc[-1].close - d.iloc[0].close) / d.iloc[0].close
    
    print('\n')
    print('Idle Days: %d' % j)
    print('Operate: %d' % i)
    print('HS300: %f%%' % round(p * 100, 2))
    print('Total: ', g_total)
    
    
    
    
        
        