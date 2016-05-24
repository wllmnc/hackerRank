#https://www.hackerrank.com/challenges/collections-counter
n,ar,nc=int(raw_input()),map(int,raw_input().split()),int(raw_input())
sum=0
for (size,price) in [map(int,raw_input().split()) for _ in range(0,nc)]:
    if size in ar:
        sum=sum+price
        ar.remove(size)

print sum