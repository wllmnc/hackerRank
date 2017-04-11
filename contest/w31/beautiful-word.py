#!/bin/python
#https://www.hackerrank.com/contests/w31/challenges/beautiful-word
import sys


w = raw_input().strip()
# Print 'Yes' if the word is beautiful or 'No' if it is not.
vowels="aeiouy"
for i in range(len(w)):
    char_=w[i]
    next_=i+1
    if next_<len(w):
        #print char_,w[next_] ,(char_ in vowels and w[next_] in vowels), (char_==w[next_])
        if (char_ in vowels and w[next_] in vowels) or (char_==w[next_]):
            break
#print i,len(w)
print "Yes" if i==len(w)-1 else "No"
