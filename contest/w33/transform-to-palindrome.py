#!/bin/python
#https://www.hackerrank.com/contests/w33/challenges/transform-to-palindrome
import sys
sys.setrecursionlimit(100000000)
def expandTree(arr_,a):
    ans=arr_
    for item in a:        
        if not item in ans:
            ans.append(item)        
            ans_=expandTree(ans,paths[item])
            for item2 in ans_:
                if not item2 in ans:
                    ans.append(item2)            
    return ans

def istherePath(origin,destination):
    return destination in paths[origin]

def getMinimunMovs(i_,j_):
    ans_=0
    i,j=i_,j_
    while(i<j):
        if a[i]!=a[j]:
            if not istherePath(a[j],a[i]) and not istherePath(a[i],a[j]):
                ans_=1+min(getMinimunMovs(i+1,j),getMinimunMovs(i,j-1))
                break
        i+=1
        j-=1
    return ans_

n,k,m = raw_input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
paths={}

for a0 in xrange(k):
    x,y = raw_input().strip().split(' ')
    x,y = [int(x),int(y)]
    if x in paths:
        paths[x].append(y)
    else:
        paths[x]=[y]
    if y in paths:
        paths[y].append(x)    
    else:
        paths[y]=[x]
        
for item in paths.keys():
    paths[item]=expandTree([],paths[item])

a = map(int, raw_input().strip().split(' '))
print len(a)-getMinimunMovs(0,len(a)-1)
