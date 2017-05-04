# Function to find the maximum contiguous subarray
from sys import maxint
def maxSubArraySum(a):
    max_so_far,max_ending_here = -maxint - 1, 0
    for item in a:
        max_ending_here = max_ending_here + item
        max_so_far = max_ending_here if (max_so_far < max_ending_here) else max_so_far
        max_ending_here = 0 if max_ending_here < 0 else max_ending_here
    return max_so_far

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print "MCS is", maxSubArraySum(a)
  
