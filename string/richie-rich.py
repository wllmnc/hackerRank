#!/bin/python
#https://www.hackerrank.com/challenges/richie-rich/
import math
import sys


n,k = map(int,raw_input().strip().split(' '))
numbers = map(int, list(raw_input().strip()))
if n<=k:
    s=""
    for i in xrange(n):
        s=s+"9"
    print int(s)
else:    
    i=0
    #looking for the different elements
    changes=[]    
    n2= n/2 if n%2==0 else (n-1)/2
    #print n2
    tz=0
    aToImprove=[]
    for i in xrange(n2):
        j=n-i-1
        if numbers[i]!=numbers[j]:
            #(1 if (numbers[i]==9 or numbers[j]==9) else 2)
            #text_file.write("%s\t%s , %s %s\n" % (i,str(numbers[i]),str(numbers[j]),z)) 
            changes.append((i,j,1 if (numbers[i]==9 or numbers[j]==9) else 2))
            tz=tz+1
            aToImprove.append(1 if (numbers[i]==9 or numbers[j]==9) else 2)
        else:
            aToImprove.append(0)
    #print tz
    #if we have changes to do and we have changes
    improve=k-tz
    if tz<=k:
        a=0
        for i in xrange(len(aToImprove)):
            j=n-i-1
            op=aToImprove[i]
            if op==0:
				if numbers[i]!=9 and improve>1:
					numbers[i]=9
					numbers[j]=9
					improve=improve-2
            else: 
				if improve>0:
					
					numbers[i]=9
					numbers[j]=9
					if op==2:
						improve=improve-1
					k=k-1
				else:
					k=k-1
					if numbers[i]>numbers[j]:
						numbers[j]=numbers[i]
					else:
						numbers[i]=numbers[j]
        if improve==1 and n%2!=0:
            numbers[(n-1)/2]=9
        s1=map(str,numbers)
        s1="".join(s1)
        print s1
    else:
        print -1
