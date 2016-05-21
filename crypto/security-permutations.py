# https://www.hackerrank.com/challenges/security-tutorial-permutations
n=int(raw_input())
f=map(int,raw_input().split())

for i in range(0,n):
    print f[f[i]-1]