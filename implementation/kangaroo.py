#!/bin/python
#https://www.hackerrank.com/challenges/kangaroo
import sys
x1,v1,x2,v2 = map(int,raw_input().strip().split(' '))
print "YES" if (v1 > v2 and  not ((x2-x1)%(v1-v2))) else "NO"
