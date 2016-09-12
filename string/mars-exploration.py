#!/bin/python
#https://www.hackerrank.com/challenges/mars-exploration
import sys
s = raw_input().strip()
count=0
i=0
while i<len(s):
    S,O,S1=s[i],s[i+1],s[i+2]
    count = count + (1 if S!='S' else 0)
    count = count + (1 if O!='O' else 0)
    count = count + (1 if S1!='S' else 0)
    i=i+3
print count
