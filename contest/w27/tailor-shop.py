#https://www.hackerrank.com/contests/w27/challenges/tailor-shop
#!/bin/python3

import sys


n,p = input().strip().split(' ')
n,p = [int(n),int(p)]
items={}
a = [int(a_temp) for a_temp in input().strip().split(' ')]
# your code goes here
plus=0
for item in a:
    val=int(item/p) + (item % p!=0)
    origin=val
    while val in items:
        val=items[val]+1
    items[origin]=val
    if origin!=val:
        items[val]=origin-1
    plus=plus+val
print(plus)
