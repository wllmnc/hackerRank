//https://www.hackerrank.com/challenges/2d-array?h_r=next-challenge&h_v=zen

#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)
#the minimun values are -9 and the minimum value could be 7(hourglass)*-9=-63
sum=-63
for i in range(0,4):
    for j in range(0,4):
        # definition of sum of hourglass
        sumT=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]+arr[i+1][j+1]
        if( sumT>sum):
            sum=sumT 
print sum
    