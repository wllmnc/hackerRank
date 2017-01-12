#https://www.hackerrank.com/contests/w28/challenges/lucky-number-eight
#!/bin/python

import sys
import itertools

    
def getSetCombinations(base):
    stuff =[str(i) for i in str(base)]
    count=0
    for L in range(1, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            s =  subset
            s = ''.join(s)
            s = int(s)
            count= count +(1 if s^7==s+7 else 0)
    return count
    
n = int(raw_input().strip())
number = raw_input().strip()
count=getSetCombinations(number)
print count%(pow(10,7)+7)
# your code goes here
