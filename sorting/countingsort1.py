#https://www.hackerrank.com/challenges/countingsort1
n,aInts=int(raw_input()),map(int,raw_input().split())
hs={}
for item in aInts:
    hs[item]= (hs[item]+1 if item in hs else 1)
for i in xrange(100):
    print (hs[i] if i in hs else 0),
