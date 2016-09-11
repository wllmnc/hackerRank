#!/bin/python
#https://www.hackerrank.com/challenges/beautiful-binary-string
import sys


n = int(raw_input().strip())
print len(raw_input().strip().split("010"))-1
