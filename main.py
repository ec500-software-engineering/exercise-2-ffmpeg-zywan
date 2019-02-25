import subprocess
import multiprocessing
import os
import json
import time

class MyProcess:
    '''
    class for converting the videos
    '''
    def run(self, inputfile):
        # get all the video file name
        file_name_list = inputfile.split('.')
        task = ['ffmpeg',
                '-i',
                inputfile,
                '-r',
                '30',
                '-s',
                'hd480',
                '-b:v',
                '1024k',
                '-loglevel',
                'quiet',
                file_name_list[0] + '_480p' + '.' + file_name_list[-1],
                '-r',
                '30',
                '-s',
                'hd720',
                '-b:v',
                '2048k',
                '-loglevel',
                'quiet',
                file_name_list[0] + '_720p' + '.' + file_name_list[-1]]
        subprocess.call(task)

        print("mission complete")

    def convert(self):
        # create a processing pool
        task_pool = multiprocessing.Pool()
        Files = os.listdir()

        for file in Files:
            file_name_list = file.split('.')
            if file_name_list[-1] == 'mp4' or file_name_list[-1] == 'mov':
                task_pool.apply_async(self.run, args=(file,))

        self.get_process_info(task_pool)
        task_pool.close()
        task_pool.join()

    def get_process_info(self,task_pool):

        print("There are {} Cpus in this machine.".format(multiprocessing.cpu_count()))
        while True:
            print('All living children of current process: ', multiprocessing.active_children())
            process_num = len(task_pool._cache)
            print("There are currently {} processes running.".format(process_num))
            if (process_num==0):
                break
            time.sleep(5)


def ffprobe(file_name)->dict:
    """ get media metadata """
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                    '-print_format', 'json',
                                    '-show_streams',
                                    '-show_format',
                                    file_name])
    return json.loads(meta)

def main():
    test = MyProcess()
    test.convert()

if __name__ == '__main__':
    main()
