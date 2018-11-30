
import csv, traceback
from copy import deepcopy

#[input]    file(str)   a file(word.txt)
#[return]   words(dict) a dict of the file content
def get_words_dict(file):

    words = {}
    dict_1 = {}
    dict_2 = {}
    dict_3 = {}
    dict_4 = {}
    dict_3_temp = {}
    dict_2_temp = {}
    
    try:
        f = open(file, 'r', encoding = 'utf-8')
        reader = csv.reader(f)
        flag_first = True
        # 0     1         2         3               4                       5                   6
        #1-1,  unit-4,	课文,		1,		秋气了树叶片大飞会个,		了子大人,		好了-行了-走了-子女-日子-儿子-大人-人手-人们-大火-大手-大小
        for l in reader:
            dict_4.clear()
            l[4] = l[4].strip().strip('\t')
            dict_4['蓝线字'] = l[4]
            
            l[5] = l[5].strip().strip('\t')
            dict_4['田字格字'] = l[5]
            
            l[6] = l[6].strip().strip('\t')
            dict_4['扩词表'] = l[6]

            
            #第几课
            dict_3.clear()
            l[3] = l[3].strip().strip('\t')
            dict_3[l[3]] = dict_4
            dict_3_temp = deepcopy(dict_3)
            
            
            #第几单元
            l[1] = l[1].strip().strip('\t')
            #新的单元
            if l[1] not in dict_2.keys():

                #读取完一个单元的数据后，向dict_1更新一次。
                #j==0时是第一次读取，不用向dict_1更新。
                if flag_first:
                    flag_first = False
                else:
                    dict_2_temp = deepcopy(dict_2)
                    
                    #年级-学期
                    l[0] = l[0].strip().strip('\t')
                    if l[0] not in dict_1.keys():
                        dict_1[l[0]] = dict_2_temp
                    else:
                        dict_1[l[0]].update(dict_2_temp)

                dict_2[l[1]] = dict_3_temp
                
            else:
                dict_2[l[1]].update(dict_3_temp)
        
        #将最后一个单元加进去
        dict_2_temp = deepcopy(dict_2)
        l[0] = l[0].strip().strip('\t')
        #新的学期
        if l[0] not in dict_1.keys():
            dict_1[l[0]] = dict_2_temp
        else:
            dict_1[l[0]].update(dict_2_temp)
            
    except:
        print(traceback.print_exc())
    
    
    words = dict_1
    return words

#根据下拉菜单中的unit，选择字和词语
def get_words_according_to_unit(words):

    unit = 'unit-5'
    characters = []
    chinese = []
    chinese_extend = []
    
    if unit == 'unit-all':
        pass
    else:
        for (k, v) in words.items():
            for (k1, v1) in v.items():
                if unit == k1:
                    #读汉字和词语
                    for (k3, v3) in v1.items():
                        #读入蓝线字
                        for l in v3['蓝线字']:
                            characters.append(l)
                        #读入田字格字    
                        for t in v3['田字格字']:
                            if t != '0':
                                chinese.append(t)
                        #读入扩词表        
                        k1 = v3['扩词表']
                        if k1 != '0':
                            k2 = k1.split('-') 
                            for k in k2:
                                chinese_extend.append(k)
    
    len_char = len(characters)
    len_chinese = len(chinese)            
    len_chinese_extend = len(chinese_extend)
    
    print(characters)
    
    return
if __name__ == '__main__':

    dict = get_words_dict('word.txt')
    get_words_according_to_unit(dict)

    