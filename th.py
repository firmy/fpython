#!/usr/bin/env python
#coding=utf-8

import threading
import time
import os
from file import writeFile

### 任务操作类,执行任务
class timer(threading.Thread,file):
    ##初始化任务属性
    def __init__(self,num,interval,file):
        threading.Thread.__init__(self)
        self.thread_num = num
        self.interval = interval
        self.file = file
        self.thread_stop = False
    ##执行任务，把线程内容写到文件中
    def run(self):
        count = 0
        while not self.thread_stop:
            count += 1
            cnt = "thread object(%d),Time:%s\n" %(self.thread_num,time.ctime())
            #do what you want to do
            writeFile(self.file,cnt)
            time.sleep(self.interval)
            if(count>3):
                self.thread_stop = True
    ##停止写入
    def stop(self):
        self.thread_stop = True

##多线程操作测试方法
def test(threads):
    array = range(threads)
    threadlist = []
    #生成线程队列
    for i in array:
        #create thread
       th = timer(i,1,str(i+1)+".txt")  
       threadlist.append(th)
    #启动线程队列  
    for i in threadlist:
        print i
        i.start()
    
    
    stop = 1
    while stop:
        #线程还没有执行完
        if threadlist:
            print "------------"
            #检查队列活跃情况
            for thread in threadlist:
                if not thread.isAlive():
                    #线程操作执行完毕，移出队列
                    threadlist.remove(thread)  
                    #打印活跃的线程队列
                    for i in threadlist:
                        print i,i.ident
           
            time.sleep(2)
        else:
            stop = 0
            print "run over"

    print "game over"

##奔跑吧少年
if __name__ == '__main__':
    test(50)
