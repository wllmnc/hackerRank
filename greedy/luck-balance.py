#https://www.hackerrank.com/challenges/luck-balance
# Enter your code here. Read input from STDIN. Print output to STDOUT

N,K=map(int,raw_input().split(" "))
aT={}
for i in xrange(N):
    l,t=map(int,raw_input().split(" "))
    if t in aT:
        aT[t].append(l)
    else:
        aT[t]=[l]
sum_=0
for index in aT:
    aT[index].sort()
    if index==0:
        for item in aT[index]:
            sum_=sum_+item   
    if index==1:
        realK=K if len(aT[index])>K else len(aT[index])
        for i in range(1,realK+1):            
            sum_=sum_+aT[index][len(aT[index])-i]
        for i in range(0,len(aT[index])-realK):
            sum_=sum_-aT[index][i]
    
print sum_
