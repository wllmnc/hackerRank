#https://www.hackerrank.com/contests/w30/challenges/candy-replenishing-robot
#!/bin/python

import sys

(n,t),c=  map(int, raw_input().strip().split(' ')),map(int, raw_input().strip().split(' '))
i,ans,nc=0,0,n
while i<t-1:
    nc=nc-c[i]
    ans,nc=(ans+n-nc,n) if nc<5 else (ans,nc)
    i=i+1
print ans
