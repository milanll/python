from unrar import rarfile
import os, time, traceback

rarFile = r'E:\Log\pct\PCT_bj_band3_zpj.rar'
targetDir = r'E:\Log\pct'

def unrarFile():
	file = targetDir + '\\' + rarFile.split('\\')[-1]
	dir = file.split('.')[0]
	
	try:
		if os.path.exists(dir):
			print("%s exist!"  % dir)
			pass
		else:
			os.mkdir(dir)
		
		print("Unrar file .....")
		file = rarfile.RarFile(rarFile)
		file.extractall(dir)
		print("Unrar file successful!")
		print("Sleep 3s .....")
		time.sleep(3)
		
		return dir
	except:
		#print("Unrar file fail!")
		traceback.print_exc()

if __name__ == '__main__':
	unrarFile()