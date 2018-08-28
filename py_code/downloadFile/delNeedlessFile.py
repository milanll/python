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
'''
shutil.copyfile( src, dst)   #从源src复制到dst中去。 如果当前的dst已存在的话就会被覆盖掉
shutil.move( src, dst)  #移动文件或重命名
shutil.copymode( src, dst) #只是会复制其权限其他的东西是不会被复制的
shutil.copystat( src, dst) #复制权限、最后访问时间、最后修改时间
shutil.copy( src, dst)  #复制一个文件到一个文件或一个目录
shutil.copy2( src, dst)  #在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2( src, dst)  #如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copytree( olddir, newdir, True/Flase) #把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.rmtree( src )   #递归删除一个目录以及目录内的所有内容
'''
'''
shutil.copyfile( src, dst)   #从源src复制到dst中去。 如果当前的dst已存在的话就会被覆盖掉
shutil.move( src, dst)  #移动文件或重命名
shutil.copymode( src, dst) #只是会复制其权限其他的东西是不会被复制的
shutil.copystat( src, dst) #复制权限、最后访问时间、最后修改时间
shutil.copy( src, dst)  #复制一个文件到一个文件或一个目录
shutil.copy2( src, dst)  #在copy上的基础上再复制文件最后访问时间与修改时间也复制过来了，类似于cp –p的东西
shutil.copy2( src, dst)  #如果两个位置的文件系统是一样的话相当于是rename操作，只是改名；如果是不在相同的文件系统的话就是做move操作
shutil.copytree( olddir, newdir, True/Flase) #把olddir拷贝一份newdir，如果第3个参数是True，则复制目录时将保持文件夹下的符号连接，如果第3个参数是False，则将在复制的目录下生成物理副本来替代符号连接
shutil.rmtree( src )   #递归删除一个目录以及目录内的所有内容
'''
import shutil,os,re,sys

OK = 1

ERROR_CITY_WRONG 	= 0
ERROR_VERSION_WRONG = 1

targetDir = r'E:\Log\pct'

def getVersion(string):
	#string = u'PCT_sz_band3_212R6424'
	#string = string.encode('unicode')

	#digital = re.findall(r"\d\d\d\d+?\d*", string, re.I)
	#print(string)
	digital = re.findall(r"\d\d\d\d+", string, re.I)

	if len(digital) == 0:
		version = 0
	else:
		version = int(digital[0])
	#print(version) 
	return version

def checkCity(city):
	if ('sz' == city) or ('bj' == city):
		return OK
	else:
		return ERROR_CITY_WRONG
		
def checkVersion(city, version, curFolder):
	for p in os.listdir(curFolder):
		if (os.path.splitext(p)[1] != '.rar') and (os.path.splitext(p)[1] !='.zip'):
			if city in p:
				if version == getVersion(p):
					return OK
				
	return 	ERROR_VERSION_WRONG
	
def findFolder(city, version):
	folder = None
	for p in os.listdir(targetDir):
		if (os.path.splitext(p)[1] != '.rar') and (os.path.splitext(p)[1] !='.zip'):
			if (city in p) and (version in p):
				folder = p
				break;
	if None != folder:
		folder = targetDir + '\\' + folder + r'\PCTTest'
	
	return folder
	
def deleteFile(curFolder):
	for p in os.listdir(curFolder):
		# save these log
		if (('TC_9' in p) or ('TC_10' in p) or ('TC_12' in p)) and (('Passed' not in p) and ('UNKNOWN' not in p)):
			print(p)
		else:
			# remove other log
			shutil.rmtree(curFolder + '\\' + p)

	
if __name__ == "__main__":
	try:
		city,version= input("please input city('sz' or 'bj') and version:\n").split(',')
	except:
		print(r'split by ","')
		
	if OK != checkCity(city):
		print("\nCity Wrong!")
		sys.exit()
	
	curFolder = findFolder(city, version)
	if None == curFolder:
		print("\nVersion Wrong!")
		sys.exit()
		
	deleteFile(curFolder)
	
	
	
	
	