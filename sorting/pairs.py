#!/usr/bin/py
#https://www.hackerrank.com/challenges/pairs
import math 
def pairs(a,k):
    return len(set(a) & set(x + k for x in a))
    
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
