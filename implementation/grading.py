#https://www.hackerrank.com/challenges/grading
#!/bin/python

import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    print grade if grade<38 else (grade+(abs(5-grade%5)) if abs(5-grade%5)<3 else grade)
    # your code goes here
