#https://www.hackerrank.com/challenges/minimum-distances
#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))
distances={}
count=-1;
for item in A:
    count=1+count
    if item in distances:
        distances[item].append(count)
    else:
        distances[item]=[count]
    distances[item].sort()
min=-1
for key in distances.keys():
    coords=distances[key]
    if len(coords)>1:
        (a,b)=coords[0:2]
        if min<0 or min>(b-a):
            min=b-a
print(min)
        
