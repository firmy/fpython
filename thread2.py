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
        count = 0
        while not self.thread_stop:
            count += 1
            cnt = "thread object(%d),Time:%s\n" %(self.thread_num,time.ctime())
            writeFile(self.file,cnt)
            time.sleep(self.interval)
            if(count>5):
                self.thread_stop = True

    def stop(self):
        self.thread_stop = True


def test():
    array = range(5)
    threadlist = []
    for i in array:
        #create thread
       th = timer(i,i,str(i)+".txt")
       #start thread
       th.start()
       #record thread_id
       threadlist.append([th,th.ident])

    list = [x[0].ident for x in threadlist]
    icount=0
    while 1:
        thidnum = [x.ident for x in threading.enumerate()]
        print 'thidnume:%s' % str(thidnum)
        print 'thidlist:%s' % str(list)

        for thread in threadlist:
            thid = thread[0].ident
            info =thid,'isalive=',thread[0].isAlive()
            print info
        
        time.sleep(2)


    
    time.sleep(30)
    #todo how to check the thread has ran over
    #http://askandstudy.blog.163.com/blog/static/1997520582012143144847/
#    thread1.stop()
#    thread2.stop()

if __name__ == '__main__':
    test()
