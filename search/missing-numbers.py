# https://www.hackerrank.com/challenges/missing-numbers
n1,a1,n2,a2=int(raw_input()), map(int,raw_input().split(" ")) , int(raw_input()), map(int,raw_input().split(" "))
h1,h2={},{}
for item in a1:
    if item in h1:
        h1[item]=h1[item]+1
    else:
        h1[item]=1
for item in a2:
    if item in h2:
        h2[item]=h2[item]+1
    else:
        h2[item]=1
ar=h1.keys()
ar.sort()
for item in ar:
    if item in h2:
        if h1[item]!=h2[item]:
            print item,
    else:
        print item,
