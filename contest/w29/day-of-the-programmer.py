#https://www.hackerrank.com/contests/w29/challenges/day-of-the-programmer
#!/bin/python

import sys


y = int(raw_input().strip())
# your code goes here
day='0'
month='09'
if y<1918:
    day=('12' if y%4==0 else '13')
elif y==1918:
    day='31'
    mont='08'
else:
    day=('12' if ((y%4==0 and y%100!=0) or y%400==0) else '13') 
print(day+'.'+month+'.'+str(y))
