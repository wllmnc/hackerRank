#https://www.hackerrank.com/challenges/swap-nodes-algo
import sys
nodes={}
nodesBydepth={}

def printOrder(root):
    (left,right)=nodes[root]
    if left!=-1:
        printOrder(left)
    print root,
    if right!=-1:
        printOrder(right)    

def InserNodeBydepth(root,depth):
    if depth in nodesBydepth:
        nodesBydepth[depth].append(root)
    else:
        nodesBydepth[depth]=[root]
    (left,right)=nodes[root]
    if left!=-1:
        InserNodeBydepth(left,depth+1)
    if right!=-1:
        InserNodeBydepth(right,depth+1)   

def swap(k):
    (a,b)=nodes[k]
    nodes[k]=(b,a)

sys.setrecursionlimit(15000)
n = int(raw_input())
i=0
while i<n:
    nodes[i+1]=map(int,raw_input().split())
    i=i+1

InserNodeBydepth(1,1)

for i in xrange(0,int(raw_input())):
    k=long(raw_input())
    i=1
    while i*k in nodesBydepth:
        for node in nodesBydepth[i*k]:
            swap(node)
        i=i+1   
    printOrder(1);
    print ""
    
    
