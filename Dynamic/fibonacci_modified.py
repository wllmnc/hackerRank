# https://www.hackerrank.com/challenges/fibonacci-modified
# Enter your code here. Read input from STDIN. Print output to STDOUT
(A,B,N)=map(int,raw_input().split())


def finboModified(n):
    if(n==1):
        return B
    elif(n==0):
        return A
    else:
        return pow(finboModified(n-1),2)+finboModified(n-2)

print finboModified(N-1)