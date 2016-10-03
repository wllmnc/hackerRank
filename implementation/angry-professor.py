#!/bin/python
#https://www.hackerrank.com/challenges/angry-professor
import sys

for a0 in xrange(int(raw_input().strip())):
    n,k = map(int,raw_input().strip().split(' '))
    present=0
    for i in map(int,raw_input().strip().split(' ')):
        present= present + (1 if i<=0 else 0)    
    print ("YES" if k>present else "NO")
