#!/bin/python

import sys

def getsum(n,t):
    if t==0:
        return 0
    elif t==1:
        return n-1
    else:
        arr_=[0 for _ in xrange(n)]
        for i in xrange(1,t+1):
            j=1
            while(j*i<n):
                arr_[j*i]=0 if  arr_[j*i] else 1
                j+=1
        return sum(arr_)
n,t = int(raw_input().strip()), int(raw_input().strip())
for i in xrange(0,t):
    print i,
    print getsum(n,i)
