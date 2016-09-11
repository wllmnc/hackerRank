# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/gem-stones
from sets import Set
n,ans=int(raw_input()),0
if n>0:
    aSeta=Set(list(raw_input()))
    for i in xrange(1,n):
        aSeta=aSeta.intersection(Set(list(raw_input())))
    ans = len(aSeta)
print ans
