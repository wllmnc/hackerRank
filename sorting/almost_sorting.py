# Enter your code here. Read input from STDIN. Print output to STDOUT

n = map(int, raw_input().strip().split(" "))
arr=map(int, raw_input().strip().split(" "))
preValue=-1
inDisorder=False
index=[0,0,0]
for i in range(0,len(arr)):
    currentValue=arr[i]
    if not inDisorder:
        if preValue>currentValue:
            inDisorder=True
            index=[i-1,i,1]
        preValue=currentValue
    else:
        #si esta en desorden y el valor anterior es menor que el actual
        if preValue>currentValue:
            index[1]=i
            if index[2]== 1 :
                index[2]=2
        else:
            if arr[index[0]]<currentValue:
                index[2]=1
            else:
                index[2]=-1

        preValue=arr[index[1]]

if index[2]>0:
    print "yes"
    if index[2]==1:
        print "swap",
    else:
        print "reverse",
    print str(index[0]+1),
    print str(index[1]+1),
else:
    print "no"