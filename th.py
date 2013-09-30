#!/usr/bin/env python
#coding=utf-8

import threading
import time
import os
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
            #do what you want to do
            writeFile(self.file,cnt)
            time.sleep(self.interval)
            if(count>2):
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
    
    stop = 1
    while stop:
        if threadlist:
            print "------------"
            for thread in threadlist:
                if not thread[0].isAlive():
                    threadlist.remove(thread)  
                    for i in threadlist:
                        print i[0],i[0].ident
           
            time.sleep(2)
        else:
            stop = 0
            print "run over"

    print "game over"
        
if __name__ == '__main__':
    test()
