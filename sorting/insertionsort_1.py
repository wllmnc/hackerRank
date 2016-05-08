#https://www.hackerrank.com/challenges/insertionsort1
#!/bin/python
def insertionSort(ar):    
    m=ar[len(ar)-1]
    for i in range(2,len(ar)+1):
        item=ar[len(ar)-i]
        if item<m:
            ar[len(ar)-i+1]=m
            break
        
        ar[len(ar)-i+1]=item
        for item in ar:
            print item,
        print ""
    if i==len(ar) and m<ar[0]:
        ar[0]=m
    for item in ar:
        print item,

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)