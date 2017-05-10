#https://www.hackerrank.com/challenges/maximum-subarray-sum
import bisect
t=int(raw_input())

def getmax(arr_, m):
    max_=0
    found = []
    for i in range(len(arr_)):
        x = arr_[i]
        j = bisect.bisect_right(found, x)
        max_ = max(max_, x)
        if j < i: 
            max_ = max(max_, (arr_[i] - found[j]) % m)
        found.insert(j, x)            
    return max_    

while(t):
    (n,c),arr_=(map(int,raw_input().split(" "))),map(int,raw_input().split(" "))
    arr_[0]=arr_[0]%c
    for i in xrange(1,n):                
        arr_[i]=(arr_[i]+arr_[i-1])%c
    print getmax(arr_,c)
    t=t-1
    
