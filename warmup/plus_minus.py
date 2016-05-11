#https://www.hackerrank.com/challenges/plus-minus
#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
contNegatives=0
contPositives=0
contCeros=0
for item in arr:
    if item==0:
        contCeros=contCeros+1
    elif item<0:
        contNegatives=contNegatives+1
    else:
        contPositives=contPositives+1
print '%.6f' % ((contPositives*1.0)/n)
print '%.6f' % ((contNegatives*1.0)/n)
print '%.6f' % ((contCeros*1.0)/n)