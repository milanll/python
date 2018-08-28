
from ftplib import FTP
import time
import tarfile

from ftplib import FTP

def ftpconnect(host, username, password):
	ftp = FTP()
	ftp.connect(host, 21)
	ftp.login(username, password)
	#print(ftp.getwelcome())
	#print(ftp.dir())
	return ftp

def downloadfile(ftp, remotepath, localpath):
	bufsize = 1024

	fp = open(localpath, 'wb')
	ftp.cwd(remotepath)
	#print(ftp.dir())
	
	print('Downloading file ...')
	ftp.retrbinary('RETR PCT_sz_band3_R8410.rar', fp.write, bufsize)
	
	ftp.set_debuglevel(0)
	fp.close()
	print('Download file successful!')

def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR'+remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == '__main__':
	host = '124.205.119.38'
	username = 'ftplog'
	password = 'simplnano123'
	
	#remotepath = 'log_dir/PCT_log/PCT-bj_band3_R9072.rar'
	remotepath = 'log_dir/PCT_log'
	localpath  = r'E:\2_Log\pct\PCT_sz_band3_R8410.rar'
	
	ftp = ftpconnect(host, username, password)

	if ftp is None:
		print('ftp connect fail!')
		
	downloadfile(ftp, remotepath, localpath)
    #uploadfile(ftp, "***", "***")

	ftp.quit()


	
	

