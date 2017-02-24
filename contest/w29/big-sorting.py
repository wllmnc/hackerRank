#!/bin/python
import collections
import sys

d = {}


n = int(raw_input().strip())
unsorted_i = 0
for unsorted_i in xrange(n):
    value=int(raw_input().strip())
    if value in d:
        d[value]=d[value]+1
    else:
        d[value]=1    
items=d.keys()
items.sort()
for k in items:
    v=d[k]
    while v:
        print k
        v=v-1
# your code goes here
