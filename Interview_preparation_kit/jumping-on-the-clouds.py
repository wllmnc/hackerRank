##problem
##    https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
## code solution

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    response = 0
    i = 0
    while i < len(c): 
        if (0==c[i]):
            if (i+2 < len(c)):
                response = response + (1 if (0 == c[i+1] or 0 == c[i+2]) else 0)
                i = i + (1 if ( 0==c[i+1] and 0 == c[i+2]) else 0)
            elif (i+1 < len(c)):
                response = response + (1 if 0 == c[i+1] else 0)
        i = i + 1
    return response

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
