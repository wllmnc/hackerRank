#solution1
#!/bin/python

import sys


s = raw_input().strip().split(" ")
for i in range(len(s)/2):
    word_=s[len(s)-i-1]
    s[len(s)-i-1]=s[i]
    s[i]=word_
print " ".join(s)

#solution2
#!/bin/python

import sys


s = raw_input().strip().split(",")
s=map(int,s)
def getMissingNumber(array_):
    next_=1
    max_=0
    hm_ints={}
    for item in array_:
        if item>max_:
            max_=item;
        hm_ints[item]=1
    i=0
    for i in range(1,max_):
        if not i in hm_ints:
            next_=i
            break;
    if i==max_-1:
        next_=max_+1
    return next_

	
	
#solution3
	
#!/bin/python

import sys

def getIslandSize(i_ , j_ ,matrix_):
    count=1
    n=len(matrix_)
    #left
    for j in range(1,j_):
        if matrix_[i_][j_-j]==1:
            count=count+1
        else:
            break
    #right
    for j in range(j_+1,n-j_):
        if matrix_[i_][j_+j]==1:
            count=count+1
        else:
            break
    #top
    for i in range(1,i_):
        if matrix_[i_-i][j_]==1:
            count=count+1
        else:
            break
    #bottom
    for i in range(i_+1,n-i_):
        if matrix_[i_+i][j_]==1:
            count=count+1
        else:
            break
    return count

def getBiggestIsland(matrix_):
    n=len(matrix_)
    i,j=0,0
    max_=0
    for row_ in matrix_:
        j=0
        for colum_ in row_:
            if colum_==1:
                candidate_=getIslandSize(i,j,matrix_)
                max_=max_ if max_>candidate_ else candidate_
            j=j+1
        i=i+1
    return max_


n= int(raw_input())
m=[]
for i in range(n): 
    m.append(map(int,raw_input().strip().split(" ")))
print getBiggestIsland(m)
            
#solution 4

#!/bin/python

import sys

def getMaxArray(x):
    x=list(x)
    return ''.join(sorted((str(n) for n in x),cmp=lambda x,y:cmp(y+x, x+y)))
s = raw_input().strip().split(",")
sizeItems={}
for item in s:
    n=item.strip()[0]
    if n in sizeItems:
        sizeItems[n].append(int(item))
    else:
        sizeItems[n]=[int(item)]
keys_=sizeItems.keys()
keys_.sort()
ans=""
for i in range(len(keys_)):
    arr_=sizeItems[keys_[len(keys_)-1-i]]
    arr_.sort()
    ans=ans+str( getMaxArray(arr_))
print ans
