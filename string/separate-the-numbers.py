#!/bin/python
#https://www.hackerrank.com/challenges/separate-the-numbers
import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    check = True
    for i in range(1,len(s)//2+1):
        n = int(s[:i])
        if ''.join(map(str, [n+j for j in range(len(s)//i)]))[:len(s)] == s:
            print("YES "+str(n))
            check = False
            break
    if check:            
        print('NO')
