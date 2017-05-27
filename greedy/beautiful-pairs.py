#https://www.hackerrank.com/challenges/beautiful-pairs
n = int(raw_input())
arrA_= map(int,raw_input().split(" "))
arrB_= map(int,raw_input().split(" "))
sum_ = 0
for i in xrange(0,n):
    v=arrB_[i]
    if v in arrA_:
        sum_+=1
        arrA_.remove(v)
print sum_+1 if sum_<n else sum_-1
