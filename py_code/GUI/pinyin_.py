
import traceback, sys, re

yunmu = ( 'ang','eng','ing','ong','an','en','in','un','ai','ei','ao','ou','iu','er','en','a','o','e','i','u', 'v')
sheng = {'a':'ā á ǎ à','o':'ō ó ǒ ò','e':'ē é ě è','i':'ī í ǐ ì','u':'ū ú ǔ ù', 'v':'ǖ ǘ ǚ ǜ'}
    
def getPy(py, ym):
    t = py[-1:].encode('ascii','ignore')#‘码表’中返回的拼音字符串最后一位是数字，表示音调值
    t2 = "%d" % ord(t)
    t3 = (int(t2) - 48)%4 -1
    py2 = py[:-len(ym)-1]#声母
    if ym == "iu":#如果韵母是iu
        letter = sheng[ym[1]].split(' ')[t3]#音调字母要标在u上
        ym = ym[0] + letter
    else:                
        letter = sheng[ym[0]].split(' ')[t3]#其它情况，音调标在第一个字母上
        ym = letter + ym[1:]
    py = py2 + ym
    return py

def get_mandarin_dict():
    fileName = 'Mandarin.dat'
    dict = {}
    try:
        f = open(fileName)
        for line in f:
            k, v = line.split('\t')
            dict[k] = v
    except:
        print(traceback.print_exc())
        sys.exit()
        
    return dict
        
def pinyin_(chars): 
    result = []
    dict = get_mandarin_dict()
    for char in chars:#chars为传入的中文字符串
        key = "%X" % ord(char)#将汉字转为utf16编码，“码表”文件中用的是这个编码
        try:
            py = dict[key].split(" ")[0].strip().lower()#只取查到的拼音第一个值（当有多音字的时候），同时将结果转为小写
            for ym in yunmu:
                if re.search(ym, py):#匹配
                    py = getPy(py, ym)
                    break#只取第一个结果
            result.append(py)
        except:
            print(traceback.print_exc())
    return " ".join(result)
    
if __name__ == '__main__':
    str = cnCode(u'部队')
    print(str)