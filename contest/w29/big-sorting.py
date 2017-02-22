#https://www.hackerrank.com/contests/w29/challenges/big-sorting
#!/bin/python

import sys


n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted.append(int(raw_input().strip()))
unsorted.sort()
for item in unsorted:
    print item
# your code goes here
