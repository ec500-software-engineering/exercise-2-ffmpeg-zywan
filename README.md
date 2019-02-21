# exercise-2-ffmpeg-zywan
## This exercise it to use ffmpeg and multiThread to convert the video simultaneously.       
### Basicly, I use two different method to implement it. --> main.py and convert.py
##### In main.py      
I Create a class named MyThread. And in run function, I check the task queue.      
If the queue is not empty, then I get the task from the queue and run a thread to handle it.
##### In convert.py
I use two function. one is caller and the other is convert.       
The function of caller is to put the task into the queue and in convert function,     
the task will be extracted from queue and begin a thread to handle that task.     
