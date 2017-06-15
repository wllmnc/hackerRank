#!/bin/python
#https://www.hackerrank.com/contests/w33/challenges/transform-to-palindrome
import sys



def getTransform(destination,path):
    ans=-1
    last_=path[len(path)-1]
    if last_ in paths:
        for candidate in paths[last_]:
            if candidate not in path:
                if candidate ==destination:
                    return candidate
                else:
                    path.append(candidate)
                    return getTransform(destination,path)
    return ans

def getMinimunMovs(a,i_,j_):
    ans_=0
    i,j=i_,j_
    noItems=[]
    while(i!=j and j>i):
        if a[i]!=a[j]:
            prev1_=getTransform(a[j],[a[i]])
            prev2_=getTransform(a[i],[a[j]])
            if prev1_+prev2_==-2:
                if j-i==1:
                    ans_=1
                else:
                    ans1=getMinimunMovs(a,i+1,j)
                    ans1= ans1 if ans1>=0 else n+1
                    ans2=getMinimunMovs(a,i,j-1)
                    ans2=ans2 if ans2>=0 else n+1
                    ans_=1+min(ans1,ans2)
                    i=j-1
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
#print paths
a = map(int, raw_input().strip().split(' '))
print len(a)-getMinimunMovs(a,0,len(a)-1)
