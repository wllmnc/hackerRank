#!/bin/python
#https://www.hackerrank.com/challenges/divisible-sum-pairs

import sys


n,k = map(int,raw_input().strip().split(' '))
a = map(int,raw_input().strip().split(' '))
count=0
for i in xrange(n):
    for j in xrange(i+1,n):
        count=count+(1 if (a[i]+a[j])%k==0 else 0)
print count
