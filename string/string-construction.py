#!/bin/python
#https://www.hackerrank.com/challenges/string-construction
import sys

for a0 in xrange(int(raw_input().strip())):
    s = raw_input().strip()
    cost=0
    for i in range(97,123):
        cost= cost + (1  if chr(i) in s else 0)
    print cost
