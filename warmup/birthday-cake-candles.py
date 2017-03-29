#!/bin/python
#https://www.hackerrank.com/challenges/birthday-cake-candles
from sets import Set
import sys


n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))
sheight= Set(height)
a= list(sheight)
a.sort()
max_=a[len(a)-1]
count=0
for i in range(n):
    item=height[i]
    if item==max_:
        count=count+1
print count
    
