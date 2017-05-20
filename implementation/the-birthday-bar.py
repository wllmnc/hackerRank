#!/bin/python
#https://www.hackerrank.com/challenges/the-birthday-bar
import sys

def getWays(squares, d, m):
    tp = (len(squares)-m) + 1
    return len([1 for i in range(tp) if sum(squares[i:i+m])==d])

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d,m = raw_input().strip().split(' ')
d,m = [int(d),int(m)]
result = getWays(s, d, m)
print(result)
