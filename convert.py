import subprocess
import threading
from queue import Queue
def caller(q, num):
	name = ['480p_'+str(num)+'.mp4', '720p_'+str(num)+'.mp4']
	task = ['ffmpeg', '-i', 'video.mp4',
		  	'-r', '30', '-s', 'hd480', '-b:v', '1024k', '-loglevel', 'quiet', name[0],
			'-r', '30', '-s', 'hd720', '-b:v', '2048k', '-loglevel', 'quiet', name[1]]
	q.put(task)
	print(task, 'is ready')


def convert(q):
	print('There are ', threading.activeCount(), 'threads running')
	if not q.empty():
		task = q.get()
		subprocess.call(task)
def main():
	q = Queue()
	i = 1
	while i<10:
		thread_caller = threading.Thread(target= caller, args = (q,i,))
		thread_convert = threading.Thread(target = convert, args=(q,))
		thread_caller.start()
		thread_convert.start()
		i += 1
	thread_caller.join()
	thread_convert.join()
	q.join()
	print('all done')


if __name__ == '__main__':
	main()