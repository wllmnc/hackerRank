#https://www.hackerrank.com/contests/w33/challenges/pattern-count
#!/bin/python

import sys

def patternCount(s):
    st_=[]
    i=0
    while i<len(s):
        if s[i]=='1':
            if len(st_)>0:
                if st_[len(st_)-1]==1:
                    st_.pop()
                elif st_[len(st_)-1]==0:
                    st_.pop()
                    st_.append(2)            
            st_.append(1)
        elif s[i]=='0':
            if len(st_)>0:
                if st_[len(st_)-1]==1:
                    st_.pop()
                    st_.append(0)
        else:
            if len(st_)>0:
                if st_[len(st_)-1]==1 or st_[len(st_)-1]==0:
                    st_.pop()
        i+=1     
    if len(st_)>0:    
        if st_[len(st_)-1]!=2:
            st_.pop()
    return len(st_)

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = patternCount(s)
    print(result)

