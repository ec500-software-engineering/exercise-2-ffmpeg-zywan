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

### Estimation     
My labtop is 2014mid macbook pro, there is a 8 core cpu. when I run the code to convert one video, the machine will make use of all its power to do that by default.   
It seems that the machine could run 10 such tasks at the same time.   
