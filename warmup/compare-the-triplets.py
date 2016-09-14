#!/bin/python
#https://www.hackerrank.com/challenges/compare-the-triplets
import sys

Alice=map(int,raw_input().strip().split(' '))
Bob=map(int,raw_input().strip().split(' '))
AliceCount,BobCount=0,0
for i in xrange(len(Alice)):
    if Alice[i]>Bob[i]:
        AliceCount=AliceCount+1
    elif Alice[i]<Bob[i]:
        BobCount=BobCount+1
print AliceCount,BobCount
