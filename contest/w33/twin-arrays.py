#https://www.hackerrank.com/contests/w33/challenges/twin-arrays
#!/bin/python
import sys

def twinArrays(ar1, ar2):
    A = dict((ar1[i],i) for i in range(len(ar1)))
    B = dict((ar2[i],i) for i in range(len(ar2)))
    ar1.sort()
    ar2.sort()
    sum_=ar2[0]+ar1[0]
    if A[ar1[0]]== B[ar2[0]]:        
        if ar1[0]>ar2[0]:
            sum_=ar2[0]+ar1[1]
        elif ar1[0]==ar2[0] :
            sum_=ar2[0]+min(ar1[1],ar2[1])
        else:
            sum_=ar1[0]+ar2[1]   
    return sum_
    

n = int(raw_input().strip())
ar1 = map(int, raw_input().strip().split(' '))
ar2 = map(int, raw_input().strip().split(' '))

result = twinArrays(ar1, ar2)
print(result)
