#!/bin/python
#https://www.hackerrank.com/challenges/marcs-cakewalk
import sys


n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))
# your code goes here
calories.sort()
ans=0
for i in xrange(n):
    ans=ans+(calories[n-i-1]*pow(2,i))
print ans
