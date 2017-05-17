#!/bin/python
#https://www.hackerrank.com/challenges/xor-se
import sys

def G(x):
    a = x % 8;
    return x if a == 0 or a== 1 else ( 2 if a == 2 or a== 3 else (x+2 if a == 4 or a== 5 else 0) )

Q = int(raw_input().strip())
for a0 in xrange(Q):
    L,R = raw_input().strip().split(' ')
    L,R = [long(L),long(R)]
    ans=G(R)^G(L-1);
    print ans   
    
