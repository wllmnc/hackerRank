#!/bin/python
#https://www.hackerrank.com/challenges/cut-the-sticks
import sys

n,arr = int(raw_input().strip()),map(int,raw_input().strip().split(' '))
minN=0
while n>0:
    print n
    for i in range(1,1001):
        if i in arr:
            minN=i
            break
    icount=0
    while minN in arr:
        arr.remove(minN)
        icount=icount+1
    for i in xrange(len(arr)):
        arr[i]=arr[i]-minN
    #print arr
    n=n-icount
    
