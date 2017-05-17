#https://www.hackerrank.com/contests/w32/challenges/fight-the-monsters
#!/bin/python

import sys

def getMaxMonsters(n, hit, t, h):
    h.sort()
    n=len(h)
    while(t):
        if(h[0]>0):
            h[0]=h[0]-hit
            t=t-1
        if(h[0]<=0):
            h.remove(h[0]) 
    return n-len(h)
        

n, hit, t = raw_input().strip().split(' ')
n, hit, t = [int(n), int(hit), int(t)]
h = map(int, raw_input().strip().split(' '))
result = getMaxMonsters(n, hit, t, h)
print(result)
