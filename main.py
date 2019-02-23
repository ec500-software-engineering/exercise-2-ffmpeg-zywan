import subprocess
import multiprocessing 
import os
import json

class MyProcess:

	def run(self, inputfile):
		file_name_list = inputfile.split('.')
		task = ['ffmpeg', '-i', inputfile,
	  		'-r', '30', '-s', 'hd480', '-b:v', '1024k', '-loglevel', 'quiet', file_name_list[0]+'_480p'+'.'+file_name_list[-1],
			'-r', '30', '-s', 'hd720', '-b:v', '2048k', '-loglevel', 'quiet', file_name_list[0]+'_720p'+'.'+file_name_list[-1]]
		subprocess.call(task)

		print("mission complete")


	def convert(self):

		task_pool = multiprocessing.Pool()
		Files = os.listdir()
		for file in Files: 
			file_name_list = file.split('.')
			if file_name_list[-1] == 'mp4' or file_name_list[-1] == 'mov':
				task_pool.apply_async(self.run, args=(file,))
		
		task_pool.close()
		task_pool.join()


def ffprobe(file_name) -> dict:
	""" get media metadata """
	meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                	'-print_format', 'json',
                                	'-show_streams',
                                	'-show_format',
                                	file_name])
	return json.loads(meta)

