import os
import paramiko

class confere_data:
	def __init__(self,
		Host='sftp.confere.com.br',
		User='desafio',
		Port=22,
		Password='N2JiYTcwMGYzNTFiYjZmMTE3YjJlYmNk',
		Home='/confere-data/sftp-users/desafio'):
		client=paramiko.SSHClient()

		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		client.connect(Host,Port, username=User, password=Password)

		self.client = client
		self.update_files()
		self.__serializedata__()

	def files(self):
		ftp = self.client.open_sftp()
		file_list = ftp.listdir()
		ftp.close()
		return file_list

	def update_files(self):
		ftp = self.client.open_sftp()
		files_updated = []

		for each in self.files():
			ex_cur_time = ftp.stat(each).st_mtime
			lc_cur_time = os.stat('downloads/'+each).st_mtime
			if ex_cur_time != lc_cur_time:
				ftp.get(each,'downloads/'+each)
				os.utime('downloads/'+each,(ex_cur_time,ex_cur_time))
				files_updated.append(each)

		ftp.close()
		return files_updated

	def update_file(self,filename):
		ftp = self.client.open_sftp()
		ftp.get(filename,'downloads/'+filename)
		os.utime('downloads/'+filename,(ex_cur_time,ex_cur_time))
		ftp.close()
		return 'File updated'

	def __serializedata__(self):
		for each in os.listdir('downloads/'):
			with open('downloads/'+each) as file:
				

confere_data()