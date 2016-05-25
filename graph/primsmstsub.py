#https://www.hackerrank.com/challenges/primsmstsub
from collections import namedtuple
Node=namedtuple('node','origin next weight')
n,m=map(int,raw_input().split())
dicNodes={}
for node in [Node(item[0],item[1],item[2]) for item in [map(int,raw_input().split()) for _ in xrange(m)]]:
    if node.origin in dicNodes.keys():
        
        if node.origin in dicNodes[node.origin].keys():
            dicNodes[node.origin][node.next].append(node.weight)
        else:
            dicNodes[node.origin][node.next]=[node.weight]
    else:
        dicNodes[node.origin]={node.next:[node.weight]}
        
    if node.next in  dicNodes.keys():
        if node.origin in dicNodes[node.next].keys():
            dicNodes[node.next][node.origin].append(node.weight)
        else:
            dicNodes[node.next][node.origin]=[node.weight]
    else:
        dicNodes[node.next]={node.origin:[node.weight]}

InitNode=int(raw_input())
ar=dicNodes[InitNode]
dicNodesActives={InitNode:0}
while len(dicNodesActives.keys())<n:
    minValue=pow(10,5)
    for key in ar:
        for w in ar[key]:
            if w<minValue:
                (nodeRef,minValue)=(key,w)
    del ar[nodeRef]
    dicNodesActives[nodeRef]=minValue
    for key in dicNodes[nodeRef].keys():
        if key in ar:
            minVal=ar[key][0]
            for item in dicNodes[nodeRef][key]:
                if minVal>item:
                    minVal=item
            ar[key][0]=minVal
        else:
            ar[key]=dicNodes[nodeRef][key]
    for node in dicNodesActives.keys():
        if node in ar:
            del ar[node]
        
print sum(dicNodesActives.values())