# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/dynamic-array
N,Q=map(int,raw_input().split())
queries=[]
seqList={}
for i in range(Q):
    queries.append(map(int,raw_input().split()))
for i in range(N):
    seqList[i]=[]
lastAnswer=0

for query,x,y in queries:
    index=(x ^ lastAnswer)% N
    if query==1:        
         seqList[index].append(y)
    else:
        lastAnswer=seqList[index][y%len(seqList[index])]
        print lastAnswer  
