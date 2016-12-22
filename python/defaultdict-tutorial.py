# https://www.hackerrank.com/challenges/defaultdict-tutorial
from collections import defaultdict
d = defaultdict(int)
(n,m)=map(int,(raw_input().split(" ")))
A=[]
B=[]
for _ in xrange(n):
    A.append(raw_input())
for _ in xrange(m):
    B.append(raw_input())
for b in B:
    if b in A:
        for i in xrange(len(A)):
            if b == A[i]:
                print i+1,
        print " "
    else:
        print -1
    
        
