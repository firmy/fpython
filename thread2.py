#!/usr/bin/env python
#coding=utf-8

import threading
import time
from file import writeFile

class timer(threading.Thread,file):
    def __init__(self,num,interval,file):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.file = file
        self.thread_stop = False

    def run(self):
        while not self.thread_stop:
            cnt = "thread object(%d),Time:%s\n" %(self.thread_num,time.ctime())
            writeFile(self.file,cnt)
            time.sleep(self.interval)

    def stop(self):
        self.thread_stop = True


def test():
    array = range(5)
    for i in array:
       timer(i,1,str(i)+".txt").start()
    
    time.sleep(30)
    #todo how to check the thread has ran over
    #http://askandstudy.blog.163.com/blog/static/1997520582012143144847/
#    thread1.stop()
#    thread2.stop()

if __name__ == '__main__':
    test()
