'''
在Python中，文件操作主要来自os模块，主要方法如下：
os.listdir(dirname)：列出dirname下的目录和文件
os.getcwd()：获得当前工作目录
os.curdir:返回当前目录（'.')
os.chdir(dirname):改变工作目录到dirname
os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
os.path.exists(name):判断是否存在文件或目录name
os.path.getsize(name):获得文件大小，如果name是目录返回0L
os.path.abspath(name):获得绝对路径
os.path.normpath(path):规范path字符串形式
os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.splitext():分离文件名与扩展名
os.path.join(path,name):连接目录与文件名或目录
os.path.basename(path):返回文件名
os.path.dirname(path):返回文件路径
os.remove(dir) #dir为要删除的文件夹或者文件路径
os.rmdir(path) #path要删除的目录的路径。需要说明的是，使用os.rmdir删除的目录必须为空目录，否则函数出错。
os.path.getmtime(name) ＃获取文件的修改时间 
os.stat(path).st_mtime＃获取文件的修改时间
os.stat(path).st_ctime #获取文件修改时间
os.path.getctime(name)#获取文件的创建时间
'''
import shutil,os,datetime,time,re,sys

import configParser

def getDigitalFromStr(string):
    #string = u'PCT_sz_band3_212R6424'
    #string = string.encode('unicode')

    #digital = re.findall(r"\d\d\d\d+?\d*", string, re.I)
    digital = re.findall(r"\d\d\d\d", string, re.I)
    
    if len(digital) == 0:
        version = 0
    else:
        version = int(digital[0])
    print(version) 
    return version

def get_filename():
    sourceDir = r'Z:\qzhang\PCT_log'

    oldVersion = configParser.readConfig(r'C:\Users\happy\code\version.conf','version','version')
    print('The old version: %s' % (oldVersion))
    
    file = None
    maxVersion = oldVersion
    
    for fileName in os.listdir(sourceDir):
        Version = getDigitalFromStr(fileName)
        if int(oldVersion) < Version:
            maxVersion = Version
            file = fileName
            configParser.writeConfig(r'C:\Users\happy\code\version.conf','version','version',f'{maxVersion}')

    print('The max version: %s\nFile name: %s' % (maxVersion,file))
    
    if file:
        file = sourceDir + '\\' + file
        
    return file

def copy_file(sourceFile):
    targetDir = r'E:\Log\pct'
    print("Target dir: %s" % (targetDir))
    print(sourceFile)
    
    print('Coping file .......')
    shutil.copy(sourceFile,  targetDir)
    print('Coppy %s successful!' % (sourceFile))

    '''
    for p in os.listdir(targetDir):
        if os.path.splitext(p)[1] == '.rar' or '.zip':
            print(p)
    '''
if __name__ == "__main__":
    file_dir = get_filename()
    if(file_dir):
        print("Source file :%s" % (file_dir))
        copy_file(file_dir)
    else:
        print('\nLog file not update!')