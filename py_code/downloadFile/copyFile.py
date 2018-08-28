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
1、str(e)

返回字符串类型，只给出异常信息，不包括异常信息的类型，如1/0的异常信息

'integer division or modulo by zero'
2、repr(e)

给出较全的异常信息，包括异常信息的类型，如1/0的异常信息

"ZeroDivisionError('integer division or modulo by zero',)"
3、e.message

获得的信息同str(e)

4、采用traceback模块

　　需要导入traceback模块，此时获取的信息最全，与python命令行运行程序出现错误信息一致。使用traceback.print_exc()打印异常信息到标准错误，就像没有获取一样，或者使用traceback.format_exc()将同样的输出获取为字符串。你可以向这些函数传递各种各样的参数来限制输出，或者重新打印到像文件类型的对象。
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

import shutil,os,re,time,traceback
from unrar import rarfile

ERROR_CITY_WRONG 	= 0
ERROR_VERSION_WRONG = 1

FILE_EXIST 		= 0
FILE_NOT_EXIST 	= 1

targetDir = r'E:\2_Log\pct'

def getVersion(string):
	#digital = re.findall(r"\d\d\d\d+", string, re.I)
	version = re.findall('band\d+_(\w+)', string, re.I)

	print(version) 
	return version.lower()

def get_filename(city,version,developer):
	if 'sz' == city:
		sourceDir = r'Z:\qzhang\PCT_log'
	elif 'bj' == city:
		#sourceDir = r'Z:\tools\temp\PCT_log'
		sourceDir = r'X:\log_dir\PCT_log\北京Log'
	else:
		print('\nCity wrong!')
		return ERROR_CITY_WRONG

	file = None
	for fileName in os.listdir(sourceDir):
		#version_read = getVersion(fileName)
		if ('0' == developer):
			if(version in fileName) and (city in fileName):
				file = fileName
				break
		elif (0 == int(version)):
			if(city in fileName) and (developer in fileName):
				file = fileName
				break
		else:
			if (version in fileName) and (city in fileName) and (developer in fileName):
				file = fileName
				break
	
	if None == file:
		print('\nVersion wrong!')
		return ERROR_VERSION_WRONG

	print('The file name: %s' % (file))
	file_dir = None
	file_dir = sourceDir + '\\' + file
        
	return file_dir

def copy_file(sourceFile):
	global targetDir
	print("Source file :%s" % (sourceFile))
	print("Target dir: %s" % (targetDir))
	
	print('Coping file .......')
	shutil.copy(sourceFile,  targetDir)
	print('Coppy %s successful!' % (sourceFile))
	
	print("Sleep 3s .....")
	time.sleep(3)
	
	return
	
def check_file_exist(city,version,developer):
	global targetDir
	ret = FILE_NOT_EXIST
	for fileName in os.listdir(targetDir):
		if os.path.splitext(fileName)[1] == '.rar' or os.path.splitext(fileName)[1] =='.zip':
			#print(p)
			#version_read = getVersion(fileName)
			
			if ('0' == developer):
				if(version in fileName) and (city in fileName):
					ret = FILE_EXIST
					break
			elif (0 == int(version)):
				if(city in fileName) and (developer in fileName):
					ret = FILE_EXIST
					break
			else:
				if (version in fileName) and (city in fileName) and (developer in fileName):
					ret = FILE_EXIST
					break
	
	return ret
	
def deleteFile(curFolder):
	file_retain = []
	curFolder = curFolder + '\\' + r'PCTTest'
	print("Delete redandent files ....")
	for p in os.listdir(curFolder):
		# save these log
		if (('TC_9' in p) or ('TC_10' in p) or ('TC_12' in p)) and (('Passed' not in p) and ('UNKNOWN' not in p)):
			#print(p)
			file_retain.append(p)
		else:
			# remove other log
			shutil.rmtree(curFolder + '\\' + p)
			#print(f"{curFolder}\\{p}")
	print("Delete redandent files finish!\n")
	
	print("The retain files:")
	for file in file_retain:
		print(file)
	
	return
	
def unrarFile(rarFile):
	file = targetDir + '\\' + rarFile.split('\\')[-1]
	dir = file.split('.')[0]
	
	try:
		if os.path.exists(dir):
			print("%s exist!"  % dir)
			pass
		else:
			os.mkdir(dir)
		
		print("Unrar files .....")
		file_rar = rarfile.RarFile(rarFile)
		file_rar.extractall(dir)
		print("Unrar files successful!")
		print("Sleep 3s .....\n")
		time.sleep(3)
		
		return dir
	except:
		#print("Unrar file fail!")
		traceback.print_exc()
	
def main():
	try:
		city,version,developer = input("please input city('sz' or 'bj') and version:\n").split(',')
	except:
		print(r'Please split by ","')
	
	check_result = check_file_exist(city, version, developer)
	if FILE_EXIST == check_result:
		print("File already exist!")
		return
		
	file_dir = get_filename(city,version, developer)
	print("\n%s\n" % file_dir)
	if (ERROR_CITY_WRONG != file_dir) and (ERROR_VERSION_WRONG != file_dir) and (FILE_EXIST != check_result):
		#copy_file(file_dir)
		pass
	else:
		return
	
	dir = unrarFile(file_dir)
	
	if 'sz' == city:
		deleteFile(dir)
	
	return
	
if __name__ == "__main__":		
	main()	
		
		