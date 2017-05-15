#https://www.hackerrank.com/challenges/maximum-perimeter-triangle
n,A=int(raw_input()),map(int,raw_input().strip().split(" "))
A.sort()

i = n-3
while i >= 0 and (A[i] + A[i+1] <= A[i+2]) :
    i -= 1

if i >= 0 :
    print A[i],A[i+1],A[i+2]
else :
    print(-1)
