import random

#x = random.random()
#y = random.random()
#print(x,y*10)
# random.random()随机生成一个[0:1)的随机数

i = 0

#1135过程中第几次
count_1135 = 1

#账户余额
total = 100

#加权的权值
weighting = 0

#出现0的连续次数
num_0 = 0

#下一把是否要投注
flag = 0

while(i < 1600):
    # random.randint()随机生成一个[0:10]的整数
    m = random.randint(0,1)
    
    weighting = 0
    
    if m == 0:
        num_0 += 1
    
    
    if flag:
        flag = 0
        
        #前2次
        if(count_1135 == 1 or count_1135 == 2):
            weighting = 1
        elif(count_1135 == 3):
            weighting = 3
        elif(count_1135 == 4):
            weighting = 5
        
        #结果是1，盈利
        if(m == 1):
            total += weighting
            
            #盈利，连续投1
            count_1135 = 1
            
        #结果是0，亏损    
        else:
            total -= weighting
            
            #亏损，阶段+1
            count_1135 += 1
            
            #亏损连续超过4次，从头开始
            if(count_1135 > 4):
                count_1135 = 1
                
    if num_0 == 3 or count_1135 != 1:
    
        num_0 = 0
        flag = 1
        
    print('第 %d 次，结果: %d，下注: %d，账户余额: %d' % (i+1, m, weighting, total))
            
    i += 1
    
    
    

    
print('账户余额', total)
      
