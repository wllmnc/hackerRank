#!/bin/python
#https://www.hackerrank.com/challenges/find-digits
import sys
from sets import Set

t = int(raw_input().strip())
for a0 in xrange(t):
    s=raw_input().strip()
    n = int(s)
    sT=map(int,list(s))
    sS=Set(sT)    
    count=0
    aItems=[]
    for i in sS:
        if i>0 and n%i==0:
            aItems.append(i)
    for i in aItems:
        while i in sT:
            sT.remove(i)
            count=count+1
    print count
