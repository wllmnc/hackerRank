#!/bin/python
#https://www.hackerrank.com/contests/w24/challenges/apple-and-orange/
import sys


s,t = map(int,raw_input().strip().split(' '))
a,b = map(int,raw_input().strip().split(' '))
m,n = map(int,raw_input().strip().split(' '))
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
applesGain,orangeGain=0,0
for _apple in apple:
    applesGain=applesGain+(1 if s<=a+_apple and a+_apple<=t else 0)
for _orange in orange:
    orangeGain=orangeGain+(1 if s<=b+_orange and b+_orange<=t else 0)
print applesGain
print orangeGain
