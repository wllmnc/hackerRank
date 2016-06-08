#https://www.hackerrank.com/challenges/python-mutations
S=raw_input()
(i,c)=raw_input().split()
print S[:int(i)]+c+S[int(i)+1:]