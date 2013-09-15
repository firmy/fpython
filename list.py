#!/usr/bin/env python
#coding=utf-8
print "hello firmy"
print "北京欢迎你"
word="abcdefg"
a=word[2]
print "a is: "+a
b=word[1:3]
print "b is: "+b # index 1 and 2 elements of word.
c=word[:2]
print "c is: "+c # index 0 and 1 elements of word.
d=word[0:]
print "d is: "+d # All elements of word.
e=word[:2]+word[2:]
print "e is: "+e # All elements of word.
f=word[-1]
print "f is: "+f # The last elements of word.
g=word[-4:-2]
print "g is: "+g # index 3 and 4 elements of word.
h=word[-2:]
print "h is: "+h # The last two elements.
i=word[:-2]
print "i is: "+i # Everything except the last two characters
l=len(word)
print "Length of word is: "+ str(l)
raw_input("press enter key to close this window...")

