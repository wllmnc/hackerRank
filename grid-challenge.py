#https://www.hackerrank.com/challenges/grid-challenge
def mod_(i):
    return i-96
t=int(raw_input())

for _ in range(t):
    ans="YES"
    last_raw=-1
    last_col=-1
    n=int(raw_input())
    prev_=[]
    for _ in range(n):
        prev_.append(-1)
    for _ in range(n):        
        arr_=map(mod_,map(ord,list(raw_input().strip())))
        arr_.sort()
        for i in range(n):
            if arr_[i]<prev_[i]:
                ans="NO"
                break
        #print arr_
        prev_=arr_
    print ans
    
