#!/bin/python
#https://www.hackerrank.com/challenges/breaking-best-and-worst-records
import sys

def getRecord(s):
    max_,min_,ansmx_,ansmn_=s[0],s[0],0,0
    for item in s:
        (max_,ansmx_)= (item, ansmx_+1) if item>max_ else (max_,ansmx_)
        (min_,ansmn_)= (item, ansmn_+1) if item<min_ else (min_,ansmn_)
    return (ansmx_,ansmn_)

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
