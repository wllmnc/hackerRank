#https://www.hackerrank.com/contests/w30/challenges/find-the-minimum-number
#!/bin/python

import sys
def printMin(val):
    return "int" if val==1 else "min(int, "+printMin(val-1)+")"        
print printMin(int(raw_input().strip()))
