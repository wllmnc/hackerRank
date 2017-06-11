#!/bin/python
#https://www.hackerrank.com/challenges/big-sorting
import sys


n = int(raw_input().strip())
unsorted = {}

for _ in xrange(n):
    unsorted_t = str(raw_input().strip())
    len_=len(unsorted_t)
    
    if not len_ in unsorted:
        unsorted[len_]=[]
        
    unsorted[len_].append(unsorted_t)
    
for key in sorted(unsorted):
    for value in sorted(unsorted[key]):
        print value
# your code goes here


