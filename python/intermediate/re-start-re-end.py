##Problem:
##     https://www.hackerrank.com/challenges/re-start-re-end/problem
## Approach:
##     I've been using the re.search function, iterating a substring, however there a couple or corner cases such patter of one letter or no match
## Solution:
import re
input_ = input()
pattern = input()
x = 0
subString = input_[x: len(input_)]
while x < len(input_):
    m = re.search(pattern, subString)
    if(m):
        endIndex = x + m.end() - 1
        print((x+m.start(), endIndex))
        x =  endIndex  + (1 if 1 == len(pattern) else 0 )
        subString = input_[x :len(input_)]
    else:
        if (input_ == subString):
            print((-1,-1))
        break;
