#!/usr/bin/env python
#coding=utf-8

import time
import thread

def timer(no,interval):
    cnt = 0
    while cnt<10:
        print "thread:(%d) time %s\n"%(no,time.ctime())
        time.sleep(interval)
        cnt += 1
    thread.exit_thread()

def test2():
    thread.start_new(timer,(1,1))


if __name__ == "__main__":
    test2()
