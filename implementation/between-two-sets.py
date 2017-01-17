#https://www.hackerrank.com/challenges/between-two-sets
#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))
count=0
for i in range(a[n-1],b[0]+1):
    candidate=True
    for item in a:
        if i%item!=0:
            candidate=False
            break
    if candidate:
        for item in b:
            if item%i!=0:
                candidate=False
                break
    count=count+(1 if candidate else 0)

print count
