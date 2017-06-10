#!/bin/python
#https://www.hackerrank.com/challenges/circular-array-rotation
import sys


[n,k,q] = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
a = a[n-(k%n):n]+a[0:n-(k%n)]
for a0 in xrange(q):
    m = int(raw_input().strip())
    print a[m]
