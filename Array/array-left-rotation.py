# Enter your code here. Read input from STDIN. Print output to STDOUT
#https://www.hackerrank.com/challenges/array-left-rotation?h_r=next-challenge&h_v=zen
n,d=map(int,raw_input().split())
sInts=raw_input().split()

for i in (map(int,sInts[d:])):
    print i,

for i in (map(int,sInts[:d])):
    print i,
