#!/usr/bin/env python
#coding=utf-8
# simple file i/o option


def writeFile(file,cnt):
    fp = open(file,"a")
    fp.write(cnt)
    fp.close()

def readFile(file):
    fp = open(file_path,"r+")
    for line in fp.xreadlines():
        print line
    fp.close()

def test():
    print "aaaaa"

def add(a,b):
    return a+b


if __name__ == '__main__':
    file_path = './a.txt'
    cnt = "hello firmy\n" 
    writeFile(file_path,cnt)
    readFile(file_path)
