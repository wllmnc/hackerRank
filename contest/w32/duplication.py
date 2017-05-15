#https://www.hackerrank.com/contests/w32/challenges/duplication
#!/bin/python

import sys

def duplication(x):
    sinit="{0:b}".format(0)
    while(len(sinit)<x+1):        
        tsinitial=[1 - int(i) for i in sinit]        
        sinit=sinit+ ''.join(str(e) for e in tsinitial)             
    return sinit[x]
q = int(raw_input().strip())
for a0 in xrange(q):
    x = int(raw_input().strip())
    result = duplication(x)
    print(result)
