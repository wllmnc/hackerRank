#https://www.hackerrank.com/challenges/cipher
n,k=map(int,raw_input().split(" "))
arr_=map(int,raw_input())
ans_=""
for i in xrange(n+k-1):
    j=i
    ans=0
    while(j>=0 and j>i-k):
            if j<n:
                #print arr_[j],
                ans=ans ^ arr_[j]
            j=j-1            
    #print ""
    ans_=ans_+str(ans)    
print ans_
