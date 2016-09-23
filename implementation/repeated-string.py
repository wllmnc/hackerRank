#!/bin/python
#https://www.hackerrank.com/challenges/repeated-string
import sys


s,n = raw_input().strip(),long(raw_input().strip())
countA=0
for c in s:
    countA=countA+ ( 1 if c=='a' else 0)
b=int((n-len(s))/len(s))+1
res=n-b*(len(s))
ind=0
for i in xrange(res):
    ind=ind+(1 if s[i]=='a' else 0)
print countA*(b)+ind
        
