#!/bin/python
#https://www.hackerrank.com/challenges/sock-merchant
import sys
from sets import Set

n,c = int(raw_input().strip()),map(int,raw_input().strip().split(' '))
items=Set(c)
sells=0
for item in items:
    count=0
    while item in c:
        count=count+1
        c.remove(item)
        if count%2==0:
            sells=sells+1
print sells
