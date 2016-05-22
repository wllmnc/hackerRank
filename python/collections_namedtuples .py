#https://www.hackerrank.com/challenges/py-collections-namedtuple
from collections import namedtuple
n, student=int(raw_input()), namedtuple('student',raw_input())
print "%.2f"% (sum([float(Student.MARKS) for Student in [student(*raw_input().split()) for _ in xrange(n)]])/n)
 