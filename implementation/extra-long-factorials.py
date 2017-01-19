#https://www.hackerrank.com/challenges/extra-long-factorials
#!/bin/python

import sys

def fact(n):
    return 1 if n<2 else n*fact(n-1)
    
n = int(raw_input().strip())
print fact(n)
