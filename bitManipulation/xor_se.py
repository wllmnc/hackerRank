#!/bin/python

import sys

def getAValue(L):
    #result=0
    init = L-(L % 4)
    print" getValue " + str(L) + " init " + str(init)
    result=init
    #print "getValue " + str(init)
    for i in xrange(init+1,L+1):
        #print i
        result=result^i
    return result

def getAValue2(L):
    result=0
    mod=L%4
    #print "gv2 "+str(L)+" mod="+str(mod)+""
    if(mod==0):
        return L
    if(mod==1):
        return 1
    if(mod==2):
        return L+1
    if(mod==3):
        return 0
    return result

Q = int(raw_input().strip())
for a0 in xrange(Q):
    L,R = raw_input().strip().split(' ')
    L,R = [long(L),long(R)]        
    #L=4*int((R-4)/4)+(L%4)
    result=0
    numElements=R-L+1
    limSL=4-(L%4)
    #print "ne= "+str(numElements)
    i=0
    #print "from "+ str(L)+ " to "+str(L+limSL)
    for i in range(L,L+limSL):
        if i < R+1:
            #print getAValue2(i)
            result=result^getAValue2(i)
    i=i+1
    #i=L+limSL
    cota=R-(R%4)
           

    #print "____cota="+str(cota) + " i " + str(i)
    contW=0
    while(i<cota):
        #print "cota="+str(cota) + " i " + str(i)
        if (i<cota):
            result=result^i
            #print str(i) + " es el elemento 4 ="+ str(i)
        i=i+2
        if (i<cota):
            contW=contW+1
        if (i<cota):
            result=result^i+1 # i+3 es el elemento plus 2 siguiente1
            #print str(i) + " es el elemento 2 ="+ str(i+1)
            i=i+2
    if (contW % 2 == 1):
        #print "xor 1 added"
        result=result^1
    #print "second forfrom "+ str(i)+ " to "+str(R+1)
    for i in range(i,R+1):
        #print getAValue2(i)
        result=result^getAValue2(i)
    #Ap=getAValue2(L-1)
    #result=0
    #print "ap= "+str(Ap)+" value("+str(L)+")="+str(Ap)
    #for i in xrange(L,R+1):
        #print str(i) + ":" + str(Ap^i)
    #    result=result^Ap^i
    #    Ap=Ap^i
    #print "**r:"+str(result)

    print result
#print getAValue(13)