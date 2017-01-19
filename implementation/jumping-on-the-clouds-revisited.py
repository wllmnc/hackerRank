#https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))
E=100
i=0
while E>0:  
    E=E-1-(2 if c[i]==1 else 0)    
    i=(i+k)%n  
    if i==0:
        break
print E
