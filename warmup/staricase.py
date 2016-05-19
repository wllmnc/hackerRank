# https://www.hackerrank.com/challenges/staircase/
#!/bin/python

import sys


n = int(raw_input().strip())

for i in range(1,n+1):
    strg=""
    for j in range(0,n-i):
        strg=strg+" "
    for j in range(0,i):
        strg=strg+"#"
    print strg