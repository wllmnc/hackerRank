# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/crush

(N,M),max_,x =map(int,raw_input().split(" ")),0,0
list_ = [0]*(N+1)
while(M):
    a,b,k=map(int,raw_input().split(" "))
    list_[a-1] += k
    if((b)<=len(list_)): list_[b] -= k;
    M=M-1 
for i in list_:
   x=x+i;
   if(max_<x): max_=x;
print max_ ;

