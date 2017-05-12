#!/bin/python
#https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array
import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
a.sort()

min_ = a[len(a)-1]
for i in range(0,n-1):
        min_ = abs(a[i] - a[i-1]) if abs(a[i] - a[i-1]) <= min_ else min_
print min_
