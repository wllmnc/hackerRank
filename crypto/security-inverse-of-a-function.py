# https://www.hackerrank.com/challenges/security-inverse-of-a-function
n=int(raw_input())
ar=map(int,raw_input().split())
for i in range(0,n):
   #print index of i in ar
   print ar.index(i+1)+1